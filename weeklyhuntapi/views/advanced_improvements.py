from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import AdvancedImprovements

class AdvancedImprovementsView(ViewSet):
    """Weekly Hunt Advanced Improvements view"""

    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        """Handle GET requests for single improvement"""
        try:
            improvement = AdvancedImprovements.objects.get(pk=pk)
            serializer = AdvancedImprovementsSerializer(improvement)
            return Response(serializer.data)
        except AdvancedImprovements.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all improvements"""
        improvements = AdvancedImprovements.objects.all()
        serializer = AdvancedImprovementsSerializer(improvements, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AdvancedImprovementsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        improvement = AdvancedImprovements.objects.get(pk=pk)
        serializer = AdvancedImprovementsSerializer(improvement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        improvement = AdvancedImprovements.objects.get(pk=pk)
        improvement.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class AdvancedImprovementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvancedImprovements
        fields = ('id', 'playbook', 'description')