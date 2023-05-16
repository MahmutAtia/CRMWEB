from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from .models import User
from rest_framework import permissions
from rest_framework.response import Response
# Create your views here.


class RegisterApi(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Testimonials fetched',
            'data': response.data
        })
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)




