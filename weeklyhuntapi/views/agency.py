from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import Agency

class AgencyView(ViewSet):
    """Agency View"""

    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            agency = Agency.objects.get(pk=pk)
            serializer = AgencySerializer(agency)
            return Response(serializer.data)
        except Agency.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        agencies = Agency.objects.all()
        serializer = AgencySerializer(agencies, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AgencySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        agency = Agency.objects.get(pk=pk)
        serializer = AgencySerializer(agency, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        agency = Agency.objects.get(pk=pk)
        agency.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AgencySerializer(serializers.ModelSerializer):
    """JSON serializer for agency"""
    class Meta:
        model = Agency
        fields = ('id', 'type')