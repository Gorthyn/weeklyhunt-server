from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import Gear

class GearView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            gear = Gear.objects.get(pk=pk)
            serializer = GearSerializer(gear)
            return Response(serializer.data)
        except Gear.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        gears = Gear.objects.select_related('playbook').all()
        serializer = GearSerializer(gears, many=True)
        return Response(serializer.data)

class GearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gear
        fields = ('id', 'name', 'harm', 'playbook')