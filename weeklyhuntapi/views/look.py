from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import Look

class LookView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            look = Look.objects.get(pk=pk)
            serializer = LookSerializer(look)
            return Response(serializer.data)
        except Look.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        looks = Look.objects.select_related('playbook').all()
        serializer = LookSerializer(looks, many=True)
        return Response(serializer.data)

class LookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Look
        fields = ('id', 'playbook', 'category', 'description')