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
        character_moves = CharacterMove.objects.all()
        serializer = CharacterMoveSerializer(character_moves, many=True)
        return Response(serializer.data)

class CharacterMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterMove
        fields = ('id', 'move', 'character')