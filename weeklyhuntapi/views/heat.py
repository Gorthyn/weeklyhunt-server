from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import Heat

class HeatView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            heat = Heat.objects.get(pk=pk)
            serializer = HeatSerializer(heat)
            return Response(serializer.data)
        except Heat.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        heats = Heat.objects.all()
        serializer = HeatSerializer(heats, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = HeatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        heat = Heat.objects.get(pk=pk)
        serializer = HeatSerializer(heat, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        heat = Heat.objects.get(pk=pk)
        heat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heat
        fields = ('id', 'description')