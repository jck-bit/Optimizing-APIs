from django.urls import path
from .import views

urlpatterns = [
    path('', views.PostsListView.as_view(), name='post-list'),
    path('/celery', views.PhotoListViewCelery.as_view(), name='post-list-celery'),
]