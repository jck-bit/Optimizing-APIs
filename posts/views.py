from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers import PostSerializer, Photoserializer
from rest_framework.response import Response
import requests
from .tasks import async_log
import json
import gzip
from django.http import HttpResponse

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
        
#after including the gzip middleware now we want to compresss the requests
class GzipCompressionView(APIView):
    def get(self, request):
        response = requests.get('https://jsonplaceholder.typicode.com/todos')
        response.raise_for_status()
        data = response.json()
        
        #serialize the data to json
        json_data = json.dumps(data).encode('utf-8')

        #compress the data
        compressed_data = gzip.compress(json_data)
        
        #set the response headers to indicate that the content is compressed
        response = HttpResponse(compressed_data, content_type='application/json')
        response['Content-Encoding'] = 'gzip'

        return response
    
#another route without compression

class NotCompressedPayload(APIView):
    def get(self, request):
        response = requests.get('https://jsonplaceholder.typicode.com/todos')
        response.raise_for_status()
        data = response.json()

        return Response(data)
    

