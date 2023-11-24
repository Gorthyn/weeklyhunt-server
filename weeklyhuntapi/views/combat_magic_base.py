from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import CombatMagicBase

class CombatMagicBaseView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            combat_magic_base = CombatMagicBase.objects.get(pk=pk)
            serializer = CombatMagicBaseSerializer(combat_magic_base)
            return Response(serializer.data)
        except CombatMagicBase.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        combat_magic_bases = CombatMagicBase.objects.all()
        serializer = CombatMagicBaseSerializer(combat_magic_bases, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CombatMagicBaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        magic_base = CombatMagicBase.objects.get(pk=pk)
        serializer = CombatMagicBaseSerializer(magic_base, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        magic_base = CombatMagicBase.objects.get(pk=pk)
        magic_base.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
class CombatMagicBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CombatMagicBase
        fields = ('id', 'name', 'harm', 'type', 'range', 'attributes')
