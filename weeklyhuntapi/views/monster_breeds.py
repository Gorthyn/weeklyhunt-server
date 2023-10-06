from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import MonsterBreeds

class MonsterBreedsView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            monster_breed = MonsterBreeds.objects.get(pk=pk)
            serializer = MonsterBreedsSerializer(monster_breed)
            return Response(serializer.data)
        except MonsterBreeds.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        monster_breeds = MonsterBreeds.objects.all()
        serializer = MonsterBreedsSerializer(monster_breeds, many=True)
        return Response(serializer.data)
    
class MonsterBreedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonsterBreeds
        fields = ('id', 'name', 'description')