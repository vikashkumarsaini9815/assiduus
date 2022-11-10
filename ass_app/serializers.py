from rest_framework import serializers
from .models import User, Message




class MessageSerializer(serializers.ModelSerializer):
   # medias=MediaSerializer(many=True, read_only=True)
    class Meta:
        model = Message
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    message=MessageSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['username','emails']

