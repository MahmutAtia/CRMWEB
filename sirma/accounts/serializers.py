from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model


from accounts.models import User
from rest_framework import serializers

User = get_user_model()

class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id","email","name","password"]



class SpecialUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","email","name","is_active","is_staff"]