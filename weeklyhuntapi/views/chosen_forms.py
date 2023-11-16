from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import ChosenForm

class ChosenFormView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            chosen_form = ChosenForm.objects.get(pk=pk)
            serializer = ChosenFormSerializer(chosen_form)
            return Response(serializer.data)
        except ChosenForm.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        chosen_forms = ChosenForm.objects.all()
        serializer = ChosenFormSerializer(chosen_forms, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ChosenFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        form = ChosenForm.objects.get(pk=pk)
        serializer = ChosenFormSerializer(form, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        form = ChosenForm.objects.get(pk=pk)
        form.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class ChosenFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChosenForm
        fields = ('id', 'name', 'harm')
