from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import Haven

class HavenView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            haven = Haven.objects.get(pk=pk)
            serializer = HavenSerializer(haven)
            return Response(serializer.data)
        except Haven.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        havens = Haven.objects.all()
        serializer = HavenSerializer(havens, many=True)
        return Response(serializer.data)

class HavenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Haven
        fields = ('id', 'name', 'description')