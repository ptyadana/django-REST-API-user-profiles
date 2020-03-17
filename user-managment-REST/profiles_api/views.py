from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

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
