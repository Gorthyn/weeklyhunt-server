from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import CharacterImprovement

class CharacterImprovementView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            character_improvement = CharacterImprovement.objects.get(pk=pk)
            serializer = CharacterImprovementSerializer(character_improvement)
            return Response(serializer.data)
        except CharacterImprovement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        character_improvements = CharacterImprovement.objects.all()
        serializer = CharacterImprovementSerializer(character_improvements, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations for character improvement"""
        serializer = CharacterImprovementSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """Handle PUT requests for character improvement"""
        character_improvement = CharacterImprovement.objects.get(pk=pk)
        serializer = CharacterImprovementSerializer(character_improvement, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk=None):
        """Handle DELETE requests for character improvement"""
        try:
            character_improvement = CharacterImprovement.objects.get(pk=pk)
            character_improvement.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except CharacterImprovement.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

class CharacterImprovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterImprovement
        fields = ('id', 'character', 'improvement', 'isChecked')