from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializers


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
