from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='post-list'),
    path('<int:pk>/', views.DetailsPost.as_view(), name='post-detail'),

    path('users/', views.UsersView.as_view(), name='user-list'),
    path('user/<int:pk>/', views.UsersDetail.as_view(), name='user-details')
]