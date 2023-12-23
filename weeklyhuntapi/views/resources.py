from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import Resources

class ResourcesView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            resource = Resources.objects.get(pk=pk)
            serializer = ResourcesSerializer(resource)
            return Response(serializer.data)
        except Resources.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        resources = Resources.objects.all()
        serializer = ResourcesSerializer(resources, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ResourcesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        resource = Resources.objects.get(pk=pk)
        serializer = ResourcesSerializer(resource, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        resource = Resources.objects.get(pk=pk)
        resource.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = '__all__'