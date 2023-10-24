from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('student', views.studentform, name='studentform'),
    path('<int:id>/', views.studentform, name='studentupdate'),
    path('delete/<int:id>/', views.studentdelete, name='delete'),
    path('list/', views.studentlist, name='studentlist'),
]
