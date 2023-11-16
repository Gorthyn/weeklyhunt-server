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
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        material = ChosenMaterial.objects.get(pk=pk)
        serializer = ChosenMaterialSerializer(material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        material = ChosenMaterial.objects.get(pk=pk)
        material.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class ChosenMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChosenMaterial
        fields = ('id', 'name')