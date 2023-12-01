from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import Heroic

class HeroicView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            heroic = Heroic.objects.get(pk=pk)
            serializer = HeroicSerializer(heroic)
            return Response(serializer.data)
        except Heroic.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        heroics = Heroic.objects.all()
        serializer = HeroicSerializer(heroics, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = HeroicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        heroic = Heroic.objects.get(pk=pk)
        serializer = HeroicSerializer(heroic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        heroic = Heroic.objects.get(pk=pk)
        heroic.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class HeroicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroic
        fields = ('id', 'description')