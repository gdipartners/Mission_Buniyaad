from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('uploadcontent', views.uploadcontent,name='uploadcontent'),
    path('view_content/<int:id>', views.view_content,name='view_content'),
    # path('upload_recommended', views.upload_recommended,name='recommended'),
]
