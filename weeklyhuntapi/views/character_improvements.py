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

class CharacterImprovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterImprovement
        fields = ('id', 'character', 'improvement', 'isChecked')