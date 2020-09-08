from django.urls import reverse


def test_profile_page_no_logged_user(client, user):
    resp = client.get(reverse("accounts:profile", args=[1]))
    assert resp.status_code == 302  # redirect


def test_profile_page_logged_user(user, logged_user_client):
    resp = logged_user_client.get(reverse("accounts:profile", args=[user.id]))
    assert resp.status_code == 200


def test_change_user_data(user, logged_user_client):
    resp = logged_user_client.get(reverse("accounts:profile", args=[user.id]))
    assert resp.status_code == 200
