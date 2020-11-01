from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.adminuser = get_user_model().objects.create_superuser(
            email="admin@pepo.com", password="password123"
        )
        self.client.force_login(self.adminuser)
        self.user = get_user_model().objects.create_user(
            email="regularuser@pepo.com",
            password="password123",
            name="Fulano Mengano Suprimo",
        )

    def test_users_listed(self) -> None:
        """Test that users are listed on user page"""
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_create_user_page(self):
        """Test that create user page works"""
        url = reverse("admin:core_user_add")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)