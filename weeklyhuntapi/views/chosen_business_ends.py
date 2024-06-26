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
    
    def create(self, request):
        serializer = ChosenBusinessEndSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        chosen_business_end = ChosenBusinessEnd.objects.get(pk=pk)
        serializer = ChosenBusinessEndSerializer(chosen_business_end, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        chosen_business_end = ChosenBusinessEnd.objects.get(pk=pk)
        chosen_business_end.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ChosenBusinessEndSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChosenBusinessEnd
        fields = ('id', 'name', 'harm')
