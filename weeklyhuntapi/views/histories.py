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
        histories = History.objects.select_related('playbook').all()
        serializer = HistorySerializer(histories, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = HistorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        history = History.objects.get(pk=pk)
        serializer = HistorySerializer(history, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        history = History.objects.get(pk=pk)
        history.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('id', 'playbook', 'description')