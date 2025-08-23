from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import HelloSerializers, UserProfileSerializer
from .models import UserProfile
from rest_framework.authentication import TokenAuthentication
from .permissions import UpdateOwnProfile


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = HelloSerializers

    def get(self, request, format=None):
        """Return a list"""

        get_list = ["a", "b", "c", "d"]
        return Response({"message": "Hello!", "get_list": get_list})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")  # type: ignore
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """Handle partial update of an Object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """Test Api ViewSet"""

    serializer_class = HelloSerializers

    def list(self, request):
        """Return a list of objects"""

        get_list = [1, 2, 3, 4]
        return Response({"message": "Hello", "list": get_list})

    def create(self, request):
        """Create a new hello message"""

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")  # type: ignore
            message = f"Hello {name}!"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ "get a specific object by id"""

        return Response({"method": "GET"})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({"method": "PUT"})

    def partial_update(self, request, pk=None):
        """Handle partial update of an Object"""
        return Response({"method": "PATCH"})

    def destroy(self, request, pk=None):
        """Delete an object"""
        return Response({"method": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
