from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import Fate

class FateView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            fate = Fate.objects.get(pk=pk)
            serializer = FateSerializer(fate)
            return Response(serializer.data)
        except Fate.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        fates = Fate.objects.all()
        serializer = FateSerializer(fates, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = FateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        fate = Fate.objects.get(pk=pk)
        serializer = FateSerializer(fate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        fate = Fate.objects.get(pk=pk)
        fate.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class FateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fate
        fields = ('id', 'description')