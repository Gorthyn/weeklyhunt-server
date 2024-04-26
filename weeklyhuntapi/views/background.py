from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import Background

class BackgroundView(ViewSet):
    """Background View"""

    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            background = Background.objects.get(pk=pk)
            serializer = BackgroundSerializer(background)
            return Response(serializer.data)
        except Background.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        backgrounds = Background.objects.all()
        serializer = BackgroundSerializer(backgrounds, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BackgroundSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        background = Background.objects.get(pk=pk)
        serializer = BackgroundSerializer(background, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        background = Background.objects.get(pk=pk)
        background.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BackgroundSerializer(serializers.ModelSerializer):
    """JSON serializer for background"""
    class Meta:
        model = Background
        fields = ('id', 'name', 'description')