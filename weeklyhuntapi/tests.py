from django.test import TestCase
from .models import Character, Playbook
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APITestCase
from weeklyhuntapi.models import NaturalAttacks, Playbook, Rating
from django.contrib.auth.models import User

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

class CharacterDetailViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.playbook = Playbook.objects.create(name="The Divine", description="Description of The Divine.")
        self.character = Character.objects.create(name="John Doe", playbook=self.playbook, charm=2, cool=1, sharp=1, tough=-1, weird=2)
        self.detail_url = reverse('character-detail', kwargs={'pk': self.character.pk})

    def test_get_character_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'John Doe')

    def test_update_character(self):
        response = self.client.patch(self.detail_url, {'name': 'Jane Doe'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.character.refresh_from_db()
        self.assertEqual(self.character.name, 'Jane Doe')

    def test_delete_character(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Character.objects.count(), 0)

class CharacterInvalidDataTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.character_url = reverse('character-list')

    def test_create_character_with_invalid_data(self):
        response = self.client.post(self.character_url, {'name': '', 'playbook_id': 999, 'charm': 'invalid'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class NaturalAttacksTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.natural_attack = NaturalAttacks.objects.create(name="Claw", harm=2, range="Short", type="Slashing")

    def test_get_natural_attacks(self):
        url = reverse('naturalattacks-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_natural_attack(self):
        url = reverse('naturalattacks-list')
        data = {"name": "Bite", "harm": 3, "range": "Melee", "type": "Piercing"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(NaturalAttacks.objects.count(), 2)

    def test_delete_natural_attack(self):
        url = reverse('naturalattacks-detail', args=[self.natural_attack.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(NaturalAttacks.objects.count(), 0)

class PlaybookTests(APITestCase):
    def setUp(self):
        self.playbook = Playbook.objects.create(name="Hunter", description="Tracks supernatural creatures.")

