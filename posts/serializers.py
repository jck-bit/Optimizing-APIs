from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    userId = serializers.IntegerField()
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    body = serializers.CharField()
