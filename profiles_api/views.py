from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list"""

        get_list = ["a", "b", "c", "d"]
        return Response({"message": "Hello!", "get_list": get_list})
