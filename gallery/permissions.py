from rest_framework import permissions


# class IsOwner(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.email == str(request.user)

class IsImageOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user_id == int(request.user.id)

class IsSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

