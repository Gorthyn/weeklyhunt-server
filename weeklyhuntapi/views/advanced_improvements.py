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
        improvements = AdvancedImprovements.objects.select_related('playbook').all()
        serializer = AdvancedImprovementsSerializer(improvements, many=True)
        return Response(serializer.data)


class AdvancedImprovementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvancedImprovements
        fields = ('id', 'playbook', 'description')