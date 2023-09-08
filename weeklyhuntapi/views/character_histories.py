from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import CharacterHistory

class CharacterHistoryView(ViewSet):
    """CharacterHistory View"""

    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            char_history = CharacterHistory.objects.get(pk=pk)
            serializer = CharacterHistorySerializer(char_history)
            return Response(serializer.data)
        except CharacterHistory.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        char_histories = CharacterHistory.objects.all()
        serializer = CharacterHistorySerializer(char_histories, many=True)
        return Response(serializer.data)

class CharacterHistorySerializer(serializers.ModelSerializer):
    """JSON serializer for character histories"""
    class Meta:
        model = CharacterHistory
        fields = ('id', 'character', 'history', 'characterName')