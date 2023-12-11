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
        looks = Look.objects.all()
        serializer = LookSerializer(looks, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = LookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        look = Look.objects.get(pk=pk)
        serializer = LookSerializer(look, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        look = Look.objects.get(pk=pk)
        look.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class LookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Look
        fields = ('id', 'playbook', 'category', 'description')