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
        moves = Move.objects.select_related('playbook').all()
        serializer = MoveSerializer(moves, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MoveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        move = Move.objects.get(pk=pk)
        serializer = MoveSerializer(move, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        move = Move.objects.get(pk=pk)
        move.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = ('id', 'playbook', 'isRequired', 'name', 'description')