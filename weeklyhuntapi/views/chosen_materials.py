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
    
class ChosenMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChosenMaterial
        fields = ('id', 'name')