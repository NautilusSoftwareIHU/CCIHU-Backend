from django.test import TestCase
from .models import IHUUser
from .serializers import UserSerializer

class UserSerializerTest(TestCase):
    def setUp(self):
        # Δημιουργία test χρήστη
        self.user = IHUUser.objects.create(
            username="testuser", email="test@example.com", password="securepassword"
        )

    def test_serialization(self):
        serializer = UserSerializer(self.user)
        self.assertEqual(serializer.data['username'], "testuser")

    def test_deserialization(self):
        data = {"username": "newuser", "email": "new@example.com", "password": "newpassword"}
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        new_user = serializer.save()
        self.assertEqual(new_user.username, "newuser")

    def test_update(self):
        data = {"email": "updated@example.com"}
        serializer = UserSerializer(self.user, data=data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_user = serializer.save()
        self.assertEqual(updated_user.email, "updated@example.com")