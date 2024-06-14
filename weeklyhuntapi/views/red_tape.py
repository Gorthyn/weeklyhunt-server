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

    def create(self, request):
        serializer = RedTapeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        red_tape = RedTape.objects.get(pk=pk)
        serializer = RedTapeSerializer(red_tape, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        red_tape = RedTape.objects.get(pk=pk)
        red_tape.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RedTapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedTape
        fields = '__all__'