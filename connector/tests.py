import pytest
from string import hexdigits
from random import choices

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import RegisteredBot


@pytest.mark.django_db
def test_user_creation():
    new_user = User.objects.create_user(
        username='sample user',
        email='user@sample.com',
        password='sample password'
    )
    
    sample_user = User.objects.get(username='sample user')
    
    assert new_user == sample_user


@pytest.mark.django_db
def test_getting_non_existing_user():
    with pytest.raises(User.DoesNotExist):
        non_existing_user = User.objects.get(username='this user not exists')


bot_model_test_params = [
    (''.join(choices(hexdigits.lower(), k=64)), True),
    (''.join(choices(hexdigits.lower(), k=65)), False)
]


@pytest.mark.django_db
@pytest.mark.parametrize('token_hash,is_valid', bot_model_test_params)
def test_registered_bot_model(token_hash, is_valid):
    registered_bot = RegisteredBot(
        name='test_bot', API_token='sample', secret_token_hash=token_hash
    )
    try:
        registered_bot.full_clean()
        bot_valid = True
    except ValidationError:
        bot_valid = False
    assert bot_valid == is_valid

