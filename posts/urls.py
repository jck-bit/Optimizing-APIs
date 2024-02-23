from django.urls import path
from .import views

urlpatterns = [
    path('', views.PostsListView.as_view(), name='post-list'),
    path('celery', views.PhotoListViewCelery.as_view(), name='post-list-celery'),
    path('/compression', views.GzipCompressionView.as_view(), name='gzip-compression'),
    path('/not-compressed', views.NotCompressedPayload.as_view(), name='not-compressed'),
]