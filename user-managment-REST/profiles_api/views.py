from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API view"""
    
    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview=[
            'Uses HTTP methods as function (get,post,put,patch,delete)',
            'Is similiar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'hello','an_apiview':an_apiview})

