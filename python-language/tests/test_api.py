import os
from unittest.mock import patch, mock_open, call
import pytest
from ..api import is_valid, export, write_csv

@pytest.fixture
def min_user():
    #valid user minimal data
    return {
        'email': 'minimal@example.com',
        'name': 'Primus Minimus',
        'age': 18,
    }

@pytest.fixture
def full_user():
    #valid user full data
    return {
        'email': 'full@example.com',
        'name': 'Maximus Plenus',
        'age': 65,
        'role': 'emperor',
    }

@pytest.fixture
def users(min_user, full_user):
    bad_user = {
        'email': 'invalid@example.com',
        'name': 'Horribilis',
    }
    #2 valid users and 1 invalid user
    return [min_user, bad_user, full_user]

class TestIsValid:
    #if user is valid or not
    def test_minimal(self, min_user):
        assert is_valid(min_user)

    def test_full(self, full_user):
        assert is_valid(full_user)