from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import Doom

class DoomView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            doom = Doom.objects.get(pk=pk)
            serializer = DoomSerializer(doom)
            return Response(serializer.data)
        except Doom.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        dooms = Doom.objects.all()
        serializer = DoomSerializer(dooms, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = DoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        doom = Doom.objects.get(pk=pk)
        serializer = DoomSerializer(doom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        doom = Doom.objects.get(pk=pk)
        doom.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class DoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doom
        fields = ('id', 'description')