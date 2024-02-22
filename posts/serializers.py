from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    userId = serializers.IntegerField()
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    body = serializers.CharField()


class Photoserializer(serializers.Serializer):
    id = serializers.IntegerField()
    albumId = serializers.IntegerField() 
    title = serializers.CharField(max_length=200)
    url = serializers.CharField()
    thumbnailUrl = serializers.CharField()