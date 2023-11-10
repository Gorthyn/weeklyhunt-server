from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import AgencyGoals

class AgencyGoalsView(ViewSet):
    """Weekly Hunt Agency Goals view"""

    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single goal"""
        try:
            goal = AgencyGoals.objects.get(pk=pk)
            serializer = AgencyGoalsSerializer(goal)
            return Response(serializer.data)
        except AgencyGoals.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all goals"""
        goals = AgencyGoals.objects.all()
        serializer = AgencyGoalsSerializer(goals, many=True)
        return Response(serializer.data)
    
    
    def create(self, request):
        serializer = AgencyGoalsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        goal = AgencyGoals.objects.get(pk=pk)
        serializer = AgencyGoalsSerializer(goal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        goal = AgencyGoals.objects.get(pk=pk)
        goal.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class AgencyGoalsSerializer(serializers.ModelSerializer):
    """JSON serializer for agency goals"""
    class Meta:
        model = AgencyGoals
        fields = ('id', 'description')