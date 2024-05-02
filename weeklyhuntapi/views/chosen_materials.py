from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import ChosenMaterial

class ChosenMaterialView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            chosen_material = ChosenMaterial.objects.get(pk=pk)
            serializer = ChosenMaterialSerializer(chosen_material)
            return Response(serializer.data)
        except ChosenMaterial.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        chosen_materials = ChosenMaterial.objects.all()
        serializer = ChosenMaterialSerializer(chosen_materials, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ChosenMaterialSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        chosen_material = ChosenMaterial.objects.get(pk=pk)
        serializer = ChosenMaterialSerializer(chosen_material, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        chosen_material = ChosenMaterial.objects.get(pk=pk)
        chosen_material.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ChosenMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChosenMaterial
        fields = ('id', 'name')