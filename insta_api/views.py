from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from insta_api import serializers



class HelloApiView(APIView):
    """ Test API view """
    serializer_class = serializers.HelloSerializers

    def get(self, request, format= None):
        """returns a list of API View"""
        an_apiview = [
                 'Uses HTTP methods as functional (get, post, patch, put , delete)',
                 'Is similar to a traditional Django View',
                 'Gives you the most control over you application logic',
                 'Is mapped manually URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        """ Create a Hello Message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST )
