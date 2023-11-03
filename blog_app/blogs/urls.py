from django.urls import path

from . import views

app_name = "blogs"
urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("<int:id>/", views.post_detail, name='post_detail'),
    path("<int:id>/share/", views.post_share, name="post_share"),
]
