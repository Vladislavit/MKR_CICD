import os

import pytest

from text_processing.text_processing import (
    count_sentences,
    count_words,
    count_words_and_sentences,
)


@pytest.fixture
def sample_text():
    return "Тестове речення номер один. Тестове речення номер два."


@pytest.fixture
def sample_file(sample_text):
    file_path = "temp_test_file.txt"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(sample_text)

    # я викорисав yield, щоб забезпечити видалення файлу після виконання тесту
    yield file_path

    # видалення того файлу
    os.unlink(file_path)


@pytest.mark.parametrize(
    "text, expected_words",
    [
        ("Це; тестовий текст, який має: кілька слів.", 7),
        ("Це тестове... речення?", 3),
        ("", 0),
    ],
)
def test_count_words(text, expected_words):
    num_of_words = count_words(text)
    assert num_of_words == expected_words


@pytest.mark.parametrize(
    "text, expected_sentences",
    [("Перше речення. Друге речення! Третє речення?", 3), ("", 0)],
)
def test_count_sentences(text, expected_sentences):
    num_sentences = count_sentences(text)
    assert num_sentences == expected_sentences


def test_count_words_and_sentences(sample_file):
    num_words, num_sentences = count_words_and_sentences(sample_file)
    assert num_words == 8
    assert num_sentences == 2