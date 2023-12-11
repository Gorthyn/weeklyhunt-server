from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import Improvement

class ImprovementView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            improvement = Improvement.objects.get(pk=pk)
            serializer = ImprovementSerializer(improvement)
            return Response(serializer.data)
        except Improvement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        improvements = Improvement.objects.all()
        serializer = ImprovementSerializer(improvements, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ImprovementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        improvement = Improvement.objects.get(pk=pk)
        serializer = ImprovementSerializer(improvement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        improvement = Improvement.objects.get(pk=pk)
        improvement.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class ImprovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Improvement
        fields = ('id', 'playbook', 'improvement')