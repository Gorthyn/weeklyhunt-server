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
    
    def create(self, request):
        serializer = MoveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        move = Move.objects.get(pk=pk)
        serializer = MoveSerializer(move, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        move = Move.objects.get(pk=pk)
        move.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = ('id', 'playbook', 'isRequired', 'name', 'description')