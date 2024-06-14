from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from weeklyhuntapi.models import Playbook

class PlaybookView(ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        try:
            playbook = Playbook.objects.get(pk=pk)
            serializer = PlaybookSerializer(playbook)
            return Response(serializer.data)
        except Playbook.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        playbooks = Playbook.objects.prefetch_related('advanced_improvements', 'basic_moves', 'histories', 'improvements', 'look', 'moves', 'ratings', 'gear', 'dice_roller').all()
        serializer = PlaybookSerializer(playbooks, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PlaybookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        playbook = Playbook.objects.get(pk=pk)
        serializer = PlaybookSerializer(playbook, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        playbook = Playbook.objects.get(pk=pk)
        playbook.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlaybookSerializer(serializers.ModelSerializer):
    advanced_improvements = serializers.StringRelatedField(many=True)
    basic_moves = serializers.StringRelatedField(many=True)
    histories = serializers.StringRelatedField(many=True)
    improvements = serializers.StringRelatedField(many=True)
    look = serializers.StringRelatedField(many=True)
    moves = serializers.StringRelatedField(many=True)
    ratings = serializers.StringRelatedField(many=True)
    gear = serializers.StringRelatedField(many=True)
    dice_roller = serializers.StringRelatedField(many=True)

    class Meta:
        model = Playbook
        fields = '__all__'  # Using __all__ to cover all the fields in the model