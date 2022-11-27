from gallery.models import Image, User
#from django.contrib.auth.models import User
from gallery.serializers import ImageSerializer, ImageListSerializer, UserSerializer
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from gallery.permissions import IsImageOwner, IsSuperuser


class ImageList(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageListSerializer


class MyImageList(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        images = list(Image.objects.filter(user_id=request.user.id).values())
        for i in images:
            i.pop('user_id')
        return Response(images)

class ImageCreate(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return Response(f"add new image for user {request.user}")


class ImageDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated, IsImageOwner]


class ImagesDelete(mixins.ListModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsSuperuser]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def delete(self, request):
        images = Image.objects.all()
        if images:
            images.delete()
            return Response("all images have been deleted")
        else:
            return Response("there are no images to delete")


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperuser]


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return Response("create new user")


class UserDetails(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        return Response({
            "id": user.id,
            "email": user.email,
            "password": user.password,
            "last_login": user.last_login
        })



