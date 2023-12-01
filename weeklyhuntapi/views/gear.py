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
        gears = Gear.objects.all()
        serializer = GearSerializer(gears, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = GearSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        gear = Gear.objects.get(pk=pk)
        serializer = GearSerializer(gear, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        gear = Gear.objects.get(pk=pk)
        gear.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class GearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gear
        fields = ('id', 'name', 'harm', 'playbook')