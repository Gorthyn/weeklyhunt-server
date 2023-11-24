from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import DarkSide

class DarkSideView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            dark_side = DarkSide.objects.get(pk=pk)
            serializer = DarkSideSerializer(dark_side)
            return Response(serializer.data)
        except DarkSide.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        dark_sides = DarkSide.objects.all()
        serializer = DarkSideSerializer(dark_sides, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = DarkSideSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        dark_side = DarkSide.objects.get(pk=pk)
        serializer = DarkSideSerializer(dark_side, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        dark_side = DarkSide.objects.get(pk=pk)
        dark_side.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class DarkSideSerializer(serializers.ModelSerializer):
    class Meta:
        model = DarkSide
        fields = ('id', 'description')