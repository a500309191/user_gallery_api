from django.urls import path, include
from gallery import views

urlpatterns = [
    path('images/', views.ImageList.as_view()),
    path('myimages/', views.MyImageList.as_view()),
    path('image/create/', views.ImageCreate.as_view()),
    path('image/<int:pk>/', views.ImageDetails.as_view()),
    path('imagesdelete/', views.ImagesDelete.as_view()),
    path('users/', views.UserList.as_view()),
    path('user/create/', views.UserCreate.as_view()),
    path('user/', views.UserDetails.as_view()),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

