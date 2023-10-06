from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import Move

class MoveView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            move = Move.objects.get(pk=pk)
            serializer = MoveSerializer(move)
            return Response(serializer.data)
        except Move.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        moves = Move.objects.all()
        serializer = MoveSerializer(moves, many=True)
        return Response(serializer.data)
    
class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = ('id', 'playbook', 'isRequired', 'name', 'description')