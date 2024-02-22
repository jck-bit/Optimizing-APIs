from rest_framework import generics, status
from .serializers import PostSerializer, Photoserializer
from rest_framework.response import Response
import requests
from .tasks import async_log
# Create your views here.


class PostsListView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        try:
            response = requests.get('https://jsonplaceholder.typicode.com/posts')
            response.raise_for_status()
            data = response.json()
            return data
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

       
class PhotoListViewCelery(generics.ListAPIView):
    serializer_class = Photoserializer

    def get_queryset(self):
        try:
            response = requests.get('https://jsonplaceholder.typicode.com/photos')
            response.raise_for_status()
            data = response.json()
            async_log.delay("Log this asynchronously")
            return data

        except Exception as e:
            raise RuntimeError(str(e))