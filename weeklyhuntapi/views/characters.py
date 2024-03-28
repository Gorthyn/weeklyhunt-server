from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import Character

class CharacterView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            character = Character.objects.select_related('playbook').prefetch_related('gear').get(pk=pk)
            serializer = CharacterSerializer(character)
            return Response(serializer.data)
        except Character.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        characters = Character.objects.select_related('playbook').prefetch_related('gear').all()
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations for character"""
        serializer = CharacterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """Handle PUT requests for character"""
        character = Character.objects.get(pk=pk)
        serializer = CharacterSerializer(character, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for character"""
        try:
            character = Character.objects.get(pk=pk)
            character.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Character.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'user', 'name', 'playbook', 'rating', 'harm_slots', 'luck_slots', 'experience_slots', 'description', 'imageURL')
