import pandas as pd

def read_from_console():
    """
    Зчитує текст, введений користувачем з консолі.
    :return: Введений рядок.
    """
    return input("Введіть текст: ")

def read_from_file_builtin(filepath):
    """
    Зчитує вміст текстового файлу за допомогою вбудованих засобів Python.
    :param filepath: Шлях до файлу.
    :return: Вміст файлу у вигляді рядка.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def read_from_file_pandas(filepath):
    """
    Зчитує CSV-файл за допомогою бібліотеки pandas.
    :param filepath: Шлях до CSV-файлу.
    :return: DataFrame з вмістом файлу.
    """
    return pd.read_csv(filepath)