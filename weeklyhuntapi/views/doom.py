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

class DoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doom
        fields = ('id', 'description')