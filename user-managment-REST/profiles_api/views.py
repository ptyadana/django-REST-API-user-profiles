from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview=[
            'Uses HTTP methods as function (get,post,put,patch,delete)',
            'Is similiar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'hello','an_apiview':an_apiview})
    

    def post(self, request):
        """Create a hello message with our name"""

        #best practice to use data=request.data
        serializer = self.serializer_class(data=request.data)

        #validate the data input (example: name is no longer than 10 chars)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message':message})  
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def put(self,request):
        """handle updating an object"""
        return Response({'message':'PUT'})

    def patch(self,request):
        """handle partial updating an object"""
        return Response({'message':'PATCH'})

    def delete(self,request):
        """handle deleting an object"""
        return Response({'message':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a Hello Message"""
        a_viewset = [
            'Uses actions(list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'More functionality with less code'
        ]

        return Response({'message':'Hello', 'a_viewset':a_viewset})

    
    def create(self,request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'

            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Handles getting an object by its id"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handles updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Hanldes updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handles removing an object"""
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and upating user profiles"""
    serializer_class = serializers.UserProfileSerializer

    #get all objects from db
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


