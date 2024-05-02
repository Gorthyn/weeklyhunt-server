from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import ChosenWeapon

class ChosenWeaponView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            chosen_weapon = ChosenWeapon.objects.get(pk=pk)
            serializer = ChosenWeaponSerializer(chosen_weapon)
            return Response(serializer.data)
        except ChosenWeapon.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        chosen_weapons = ChosenWeapon.objects.prefetch_related('character', 'form', 'material', 'businessEnd1', 'businessEnd2', 'businessEnd3').all()
        serializer = ChosenWeaponSerializer(chosen_weapons, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ChosenWeaponSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        chosen_weapon = ChosenWeapon.objects.get(pk=pk)
        serializer = ChosenWeaponSerializer(chosen_weapon, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        chosen_weapon = ChosenWeapon.objects.get(pk=pk)
        chosen_weapon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ChosenWeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChosenWeapon
        fields = ('id', 'character', 'form', 'formHarm', 'material', 'businessEnd1', 'businessEndHarm1', 'businessEnd2', 'businessEndHarm2', 'businessEnd3', 'businessEndHarm3')