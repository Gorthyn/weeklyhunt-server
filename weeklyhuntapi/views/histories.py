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
    
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('id', 'playbook', 'description')