from django.urls import path
from . import views

urlpatterns = [

    path('list/', views.StudentListView.as_view(), name='get_api'),
    path('create/', views.StudentCreateView.as_view(), name='post_api'),

]
