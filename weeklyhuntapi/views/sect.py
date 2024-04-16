from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import Sect

class SectView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            sect = Sect.objects.get(pk=pk)
            serializer = SectSerializer(sect)
            return Response(serializer.data)
        except Sect.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        sects = Sect.objects.all()  # Add prefetch_related if there are related models.
        serializer = SectSerializer(sects, many=True)
        return Response(serializer.data)

class SectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sect
        fields = '__all__'