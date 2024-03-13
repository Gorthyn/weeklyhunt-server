from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import NaturalAttacks

class NaturalAttacksView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            natural_attack = NaturalAttacks.objects.get(pk=pk)
            serializer = NaturalAttacksSerializer(natural_attack)
            return Response(serializer.data)
        except NaturalAttacks.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        natural_attacks = NaturalAttacks.objects.all()
        serializer = NaturalAttacksSerializer(natural_attacks, many=True)
        return Response(serializer.data)

class NaturalAttacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaturalAttacks
        fields = ('id', 'name', 'harm', 'range', 'type')