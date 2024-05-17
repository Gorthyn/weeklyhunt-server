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

    def create(self, request):
        serializer = GearSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        gear = Gear.objects.get(pk=pk)
        serializer = GearSerializer(gear, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        gear = Gear.objects.get(pk=pk)
        gear.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gear
        fields = ('id', 'name', 'harm', 'playbook')