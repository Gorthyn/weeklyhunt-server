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
        who_you_losts = WhoYouLost.objects.all()
        serializer = WhoYouLostSerializer(who_you_losts, many=True)
        return Response(serializer.data)

class WhoYouLostSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhoYouLost
        fields = '__all__'