from rest_framework import serializers


class HelloSerializers(serializers.Serializer):
    """Serializes a name field for testing api view post (serialize is basically a a form where u define the input fields)"""

    name = serializers.CharField(max_length=50)
