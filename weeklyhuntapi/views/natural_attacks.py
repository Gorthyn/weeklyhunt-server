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

    def create(self, request):
        serializer = NaturalAttacksSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        natural_attack = NaturalAttacks.objects.get(pk=pk)
        serializer = NaturalAttacksSerializer(natural_attack, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        natural_attack = NaturalAttacks.objects.get(pk=pk)
        natural_attack.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class NaturalAttacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaturalAttacks
        fields = ('id', 'name', 'harm', 'range', 'type')