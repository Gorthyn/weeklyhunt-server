from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import Reason

class ReasonView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            reason = Reason.objects.get(pk=pk)
            serializer = ReasonSerializer(reason)
            return Response(serializer.data)
        except Reason.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        reasons = Reason.objects.all()
        serializer = ReasonSerializer(reasons, many=True)
        return Response(serializer.data)
    
class ReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reason
        fields = '__all__'