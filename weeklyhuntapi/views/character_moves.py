from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import CharacterMove

class CharacterMoveView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            character_move = CharacterMove.objects.get(pk=pk)
            serializer = CharacterMoveSerializer(character_move)
            return Response(serializer.data)
        except CharacterMove.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        character_moves = CharacterMove.objects.select_related('character', 'move').all()
        serializer = CharacterMoveSerializer(character_moves, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations for character move"""
        serializer = CharacterMoveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """Handle PUT requests for character move"""
        character_move = CharacterMove.objects.get(pk=pk)
        serializer = CharacterMoveSerializer(character_move, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk=None):
        """Handle DELETE requests for character move"""
        try:
            character_move = CharacterMove.objects.get(pk=pk)
            character_move.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except CharacterMove.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

class CharacterMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterMove
        fields = ('id', 'move', 'character')