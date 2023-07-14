from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from weeklyhuntapi.models import CharacterGear

class CharacterGearView(ViewSet):
    """Weekly Hunt character gear view"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single gear"""
        try:
            character_gear = CharacterGear.objects.get(pk=pk)
            serializer = CharacterGearSerializer(character_gear)
            return Response(serializer.data)
        except CharacterGear.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all character gears"""
        character_gears = CharacterGear.objects.all()
        serializer = CharacterGearSerializer(character_gears, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations for character gear

        Returns:
            Response -- JSON serialized character gear instance
        """
        new_character_gear = CharacterGear()
        new_character_gear.character_id = request.data["character"]
        new_character_gear.gear_id = request.data["gear"]
        new_character_gear.save()

        serializer = CharacterGearSerializer(new_character_gear)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """Handle PUT requests for character gear

        Returns:
            Response -- Empty body with 204 status code
        """
        character_gear = CharacterGear.objects.get(pk=pk)
        character_gear.character_id = request.data["character"]
        character_gear.gear_id = request.data["gear"]
        character_gear.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single gear"""
        try:
            character_gear = CharacterGear.objects.get(pk=pk)
            character_gear.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except CharacterGear.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

class CharacterGearSerializer(serializers.ModelSerializer):
    """JSON serializer for character gears"""
    class Meta:
        model = CharacterGear
        fields = ('id', 'character', 'gear')
