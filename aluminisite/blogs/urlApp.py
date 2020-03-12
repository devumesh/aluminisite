from django.urls import path
from . import views
urlpatterns = [
    path('', views.Blogsite.as_view(), name='home'),
    path('<int:pk>/', views.BlogsiteDetail.as_view(), name='detailed'),
    path('new/', views.NewBlog.as_view(), name='newblog'),
    path('edit/<int:pk>/', views.EditBlog.as_view(), name='edit'),
    path('delete/<int:pk>/', views.DeleteBlog.as_view(), name='delete'),
]