from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listing, name='create_listing'),
    path("lising/<int:pk>", views.show_listing, name='listing_view'),
    path("listing/close/<int:pk>", views.close_listing, name='close_listing'),
    path("listing/comment/<int:pk>", views.comment, name='comment'),
    path("listing/watch/<int:pk>", views.watch_list, name='watch_list'),
    path("listing/watch/stop/<int:pk>", views.stop_watch, name='stop_watch'),
    path("watchlist", views.show_watch_list, name='show_watch_list'),
    path("categories", views.show_categories, name='show_categories'),
    path("category/<int:pk>", views.show_category_listing, name='show_category_listing'),
]
