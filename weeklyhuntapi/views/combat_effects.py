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
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        combat_effect = CombatEffect.objects.get(pk=pk)
        serializer = CombatEffectSerializer(combat_effect, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        combat_effect = CombatEffect.objects.get(pk=pk)
        combat_effect.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CombatEffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CombatEffect
        fields = ('id', 'name', 'harm_bonus', 'type_bonus', 'attributes', 'special')