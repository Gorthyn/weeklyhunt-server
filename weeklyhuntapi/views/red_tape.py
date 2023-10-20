from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import RedTape

class RedTapeView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            red_tape = RedTape.objects.get(pk=pk)
            serializer = RedTapeSerializer(red_tape)
            return Response(serializer.data)
        except RedTape.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        red_tapes = RedTape.objects.all()
        serializer = RedTapeSerializer(red_tapes, many=True)
        return Response(serializer.data)
    
class RedTapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedTape
        fields = '__all__'