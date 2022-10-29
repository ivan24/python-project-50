import pytest
from gendiff.file_diff import generate_diff


@pytest.fixture
def path_file1():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def path_file2():
    return 'tests/fixtures/file2.json'


def test_file_difference():
    with open('tests/fixtures/etalon.txt', 'r') as file:
        expected_file = file.read()
    result_file = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert result_file == str(expected_file)


