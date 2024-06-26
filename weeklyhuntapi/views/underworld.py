from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import Underworld

class UnderworldView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            underworld = Underworld.objects.get(pk=pk)
            serializer = UnderworldSerializer(underworld)
            return Response(serializer.data)
        except Underworld.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        underworlds = Underworld.objects.all()
        serializer = UnderworldSerializer(underworlds, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UnderworldSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        underworld = Underworld.objects.get(pk=pk)
        serializer = UnderworldSerializer(underworld, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        underworld = Underworld.objects.get(pk=pk)
        underworld.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UnderworldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Underworld
        fields = '__all__'