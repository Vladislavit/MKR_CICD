def read_text_from_file(file_path: str) -> str:
    """
    Зчитує текст з файлу.

    :param file_path: Шлях до текстового файлу.
    :return: Зміст файлу у вигляді рядка.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text