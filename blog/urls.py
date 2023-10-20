from django.urls import path

from . import views


urlpatterns = [
    path("", views.blog_index, name="index"),
    path("register/", views.register, name="register"),
    path("categories/", views.blog_categories, name="categories"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>", views.blog_category, name="blog_category"),
]
