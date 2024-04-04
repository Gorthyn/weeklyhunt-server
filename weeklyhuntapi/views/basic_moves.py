from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import BasicMove

class BasicMoveView(ViewSet):
    """Weekly Hunt basic moves view"""

    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        """Handle GET requests for single move"""
        try:
            move = BasicMove.objects.get(pk=pk)
            serializer = BasicMoveSerializer(move)
            return Response(serializer.data)
        except BasicMove.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        moves = BasicMove.objects.select_related('playbook').all()
        serializer = BasicMoveSerializer(moves, many=True)
        return Response(serializer.data)

class BasicMoveSerializer(serializers.ModelSerializer):
    """JSON serializer for basic moves"""
    class Meta:
        model = BasicMove
        fields = ('id', 'name')
