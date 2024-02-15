from django.shortcuts import render
from rest_framework  import viewsets
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken 

from . import serializers
from . import models
from . import permissions

# Create your views here.

class HelloApiView(APIView):
    """Test Api"""
    
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """returns a list of api feature"""
        
        an_apiview = [
            'uses http function like get, post put',
            'it is a traditional djanngo view',
            'it is mapped manually to urls'
        ]
        
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create hello message with our name"""
        
        serializer = serializers.HelloSerializer(data=request.data)
        
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk=None):
        """Handle updating an object and returning it"""
        return Response({'method': 'put'})
        
    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'patch'})
        
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        """Return a list of viewset."""
        
        apiviewset = [
            'doesnt make use of http function',
            'rather it use list, create, update, delete',
            'its from rest_framework',
            'automatically maps to url using router'
        ]
        
        return Response({'message': 'say-hello', 'apiviewset':apiviewset})
    
    def create(self, request):
        """create hello message"""
        serializer = serializers.HelloSerializer(data=request.data)
        
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request,pk=None):
        """return specific object by its id"""
        return Response({'http_method': 'GET '})
    
    def  update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})
    
    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        """Remove an object by its id"""
        return Response({'http_method': 'DELETE'})
    

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""
    
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_class = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
    
    
class LoginViewSet(viewsets.ViewSet):
    """checks email and password and returns an auth token"""
    
    serializer_class = AuthTokenSerializer
    
    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token""" 
        
        return ObtainAuthToken().post(request)
    