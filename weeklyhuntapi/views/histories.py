from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import History

class HistoryView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            history = History.objects.get(pk=pk)
            serializer = HistorySerializer(history)
            return Response(serializer.data)
        except History.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        histories = History.objects.all()
        serializer = HistorySerializer(histories, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = HistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        history = History.objects.get(pk=pk)
        serializer = HistorySerializer(history, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        history = History.objects.get(pk=pk)
        history.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('id', 'playbook', 'description')