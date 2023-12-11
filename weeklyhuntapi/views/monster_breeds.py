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
    
    def create(self, request):
        serializer = MonsterBreedsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        monster_breed = MonsterBreeds.objects.get(pk=pk)
        serializer = MonsterBreedsSerializer(monster_breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        monster_breed = MonsterBreeds.objects.get(pk=pk)
        monster_breed.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class MonsterBreedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonsterBreeds
        fields = ('id', 'name', 'description')