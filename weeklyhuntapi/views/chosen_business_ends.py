from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import ChosenBusinessEnd

class ChosenBusinessEndView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            chosen_business_end = ChosenBusinessEnd.objects.get(pk=pk)
            serializer = ChosenBusinessEndSerializer(chosen_business_end)
            return Response(serializer.data)
        except ChosenBusinessEnd.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        chosen_business_ends = ChosenBusinessEnd.objects.all()
        serializer = ChosenBusinessEndSerializer(chosen_business_ends, many=True)
        return Response(serializer.data)

class ChosenBusinessEndSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChosenBusinessEnd
        fields = ('id', 'name', 'harm')
