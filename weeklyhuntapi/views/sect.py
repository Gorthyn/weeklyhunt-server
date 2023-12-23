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
        sects = Sect.objects.all()
        serializer = SectSerializer(sects, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = SectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        sect = Sect.objects.get(pk=pk)
        serializer = SectSerializer(sect, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        sect = Sect.objects.get(pk=pk)
        sect.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class SectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sect
        fields = '__all__'