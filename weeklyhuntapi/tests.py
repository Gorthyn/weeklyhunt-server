from django.test import TestCase
from .models import Character, Playbook
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient

# Create your tests here. Will need to create tests to validate pull requests for future use in moving to the front end.
class CharacterModelTest(TestCase):
    def test_character_creation(self):
        playbook = Playbook.objects.create(name="The Divine", description="Description of The Divine.")
        character = Character.objects.create(name="John Doe", playbook=playbook, charm=2, cool=1, sharp=1, tough=-1, weird=2)
        self.assertEqual(character.name, "John Doe")
        self.assertEqual(character.playbook.name, "The Divine")
        self.assertEqual(character.charm, 2)
        self.assertEqual(character.cool, 1)
        self.assertEqual(character.sharp, 0)
        self.assertEqual(character.tough, 2)
        self.assertEqual(character.weird, -1)