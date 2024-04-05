from file_reading.file_reading import read_text_from_file


def count_words(text: str) -> int:
    """
    Підраховує кількість слів у тексті.

    :param text: Вхідний текст.
    :return: Кількість слів у тексті.
    """
    words = text.split()
    return len(words)


def count_sentences(text: str) -> int:
    """
    Підраховує кількість речень у тексті.

    :param text: Вхідний текст.
    :return: Кількість речень у тексті.
    """
    sentence_endings = [".", "!", "?", "..."]
    num_sentences = 0
    for ending in sentence_endings:
        num_sentences += text.count(ending)
    return num_sentences


def count_words_and_sentences(file_path: str) -> tuple[int, int]:
    """
    Підраховує кількість слів та речень у текстовому файлі.

    :param file_path: Шлях до текстового файлу.
    :return: Кортеж, що містить кількість слів та речень.
    """
    text = read_text_from_file(file_path)
    num_of_words = count_words(text)
    num_of_sentences = count_sentences(text)
    return num_of_words, num_of_sentences