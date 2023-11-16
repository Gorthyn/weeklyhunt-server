from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import CombatEffect

class CombatEffectView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            combat_effect = CombatEffect.objects.get(pk=pk)
            serializer = CombatEffectSerializer(combat_effect)
            return Response(serializer.data)
        except CombatEffect.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        combat_effects = CombatEffect.objects.all()
        serializer = CombatEffectSerializer(combat_effects, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CombatEffectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        effect = CombatEffect.objects.get(pk=pk)
        serializer = CombatEffectSerializer(effect, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        effect = CombatEffect.objects.get(pk=pk)
        effect.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
class CombatEffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CombatEffect
        fields = ('id', 'name', 'harm_bonus', 'type_bonus', 'attributes', 'special')