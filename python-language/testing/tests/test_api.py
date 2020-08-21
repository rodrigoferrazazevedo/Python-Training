# tests/test_api.py
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

    @pytest.mark.parametrize('age', range(18))
    def test_invalid_age_too_young(self, age, min_user):
        min_user['age'] = age
        assert not is_valid(min_user)

    @pytest.mark.parametrize('age', range(66, 100))
    def test_invalid_age_too_old(self, age, min_user):
        min_user['age'] = age
        assert not is_valid(min_user)

    @pytest.mark.parametrize('age', ['NaN', 3.1415, None])
    def test_invalid_age_wrong_type(self, age, min_user):
        min_user['age'] = age
        assert not is_valid(min_user)

    @pytest.mark.parametrize('age', range(18, 66))
    def test_valid_age(self, age, min_user):
        min_user['age'] = age
        assert is_valid(min_user)

    @pytest.mark.parametrize('field', ['email', 'name', 'age'])
    def test_mandatory_fields(self, field, min_user):
        min_user.pop(field)
        assert not is_valid(min_user)

    @pytest.mark.parametrize('field', ['email', 'name', 'age'])
    def test_mandatory_fields_empty(self, field, min_user):
        min_user[field] = ''
        assert not is_valid(min_user)

    def test_name_whitespace_only(self, min_user):
        min_user['name'] = '\n\t'
        assert not is_valid(min_user)

    @pytest.mark.parametrize(
        'field, value',
        [
            ('email', None),
            ('email', 3.1415),
            ('email', {}),

            ('name', None),
            ('name', 3.1415),
            ('name', {}),

            ('role', None),
            ('role', 3.1415),
            ('role', {}),
        ]
    )
    def test_invalid_types(self, field, value, min_user):
        min_user[field] = value
        assert not is_valid(min_user)

class TestExport:

    @pytest.fixture
    def csv_file(self, tmpdir):
        yield tmpdir.join("out.csv")

    @pytest.fixture
    def existing_file(self, tmpdir):
        existing = tmpdir.join('existing.csv')
        existing.write('Please leave me alone...')
        yield existing

    def test_export(self, users, csv_file):
        export(csv_file, users)

        lines = csv_file.readlines()

        assert [
            'email, name, age, role\n',
            'minimal@example.com, Primus Minimus, 18,\n',
            'full@example.com, Maximus Plenus, 65, emperor\n'
        ] == lines

    def test_export_quoting(self, min_user, csv_file):
        min_user['name'] = 'A name, with a comma'

        export(csv_file, [min_user])

        lines = csv_file.readlines()
        assert [
            'email, name, age, role\n',
            'minimal@example.com, "A name, with a comma", 18,\n',
        ] == lines

    def test_does_not_overwrite(self, users, existing_file):
        with pytest.raises(IOError) as err:
            export(existing_file, users, overwrite=False)

        assert err.match(
            r"'{}' already exists\.".format(existing_file)
        )

        assert existing_file.read() == 'Please leave me alone...'