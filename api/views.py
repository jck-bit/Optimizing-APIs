from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from posts.serializers import PostSerializer

import requests

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