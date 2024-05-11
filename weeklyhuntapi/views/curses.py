from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import Curse

class CurseView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            curse = Curse.objects.get(pk=pk)
            serializer = CurseSerializer(curse)
            return Response(serializer.data)
        except Curse.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        curses = Curse.objects.all()
        serializer = CurseSerializer(curses, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CurseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        curse = Curse.objects.get(pk=pk)
        serializer = CurseSerializer(curse, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        curse = Curse.objects.get(pk=pk)
        curse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curse
        fields = ('id', 'name', 'description')