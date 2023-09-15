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
        chosen_weapons = ChosenWeapon.objects.all()
        serializer = ChosenWeaponSerializer(chosen_weapons, many=True)
        return Response(serializer.data)
    
class ChosenWeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChosenWeapon
        fields = ('id', 'character', 'form', 'formHarm', 'material', 'businessEnd1', 'businessEndHarm1', 'businessEnd2', 'businessEndHarm2', 'businessEnd3', 'businessEndHarm3')