from ihuauth.models import UserProfile
from django.test import TestCase


class UserProfileTest(TestCase):
    def test_create_user_profile(self):
        """Test ότι το instance δημιουργείται σωστά."""
        user = UserProfile.objects.create(username="john_doe", email="john@example.com")
        self.assertEqual(user.username, "john_doe")
        self.assertEqual(user.email, "john@example.com")
        self.assertIsNotNone(user.created_at)
