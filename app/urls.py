from django.urls import path

from .views import completed, create_obj, obj_completed, objectives

urlpatterns = [
    path('', objectives, name='objectives'),
    path('cmpl/<int:obj_id>/', obj_completed, name='obj_completed'),
    path('create_obj/', create_obj, name='create_obj'),
    path('completed/', completed, name='completed'),
]
