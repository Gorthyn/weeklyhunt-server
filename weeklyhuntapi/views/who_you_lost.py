from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import WhoYouLost

class WhoYouLostView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            who_you_lost = WhoYouLost.objects.get(pk=pk)
            serializer = WhoYouLostSerializer(who_you_lost)
            return Response(serializer.data)
        except WhoYouLost.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        who_you_losts = WhoYouLost.objects.all()  # Add prefetch_related if there are frequent accesses to related data.
        serializer = WhoYouLostSerializer(who_you_losts, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = WhoYouLostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        who_you_lost = WhoYouLost.objects.get(pk=pk)
        serializer = WhoYouLostSerializer(who_you_lost, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        who_you_lost = WhoYouLost.objects.get(pk=pk)
        who_you_lost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WhoYouLostSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhoYouLost
        fields = '__all__'