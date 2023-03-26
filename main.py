# -*- coding: utf-8 -*-
import time


def text_to_codes(text, abc):
    """
    Преобразование текста в числовые коды

    :param text: исходный текст
    :param abc: алфавит
    :return: порядковый номер буквы сходного текста из алфавита
    """
    return [abc.index(c) for c in text]


def codes_to_text(codes, abc):
    """
    Преобразование числовых кодов в текст
    порядковый номер буквы из алфавита abc

    :param codes: массив чисел, который представляет собой порядковый номер буквы из алфавита
    :param abc: алфавит которым преобразовывали буквы в числа
    :return: текст который который был зашифрован
    """
    return "".join([abc[c] for c in codes])


def cesar(codes, rot=13):
    """
    Сдвигаем шифром цезаря закодированный текст

    :param codes: коды букв
    :param rot: сдвиг
    :return: коды букв после сдвига
    """
    text3 = []
    for symbol in codes:
        text3.append((symbol + rot) % 32)
    return text3


def analis_text(text, abc1, abc2, abc3):
    """
    :param abc1: полный алфавит
    :param abc2: алфавит для замены ё на е
    :param abc3: редуцированный алфавит
    :return: словарь, сколько раз встречается каждая буква
    """

    # преобразование алфавитов (удаление лишних символов и замена ё на е)
    clear_text = ""
    for ch in text:
        if ch in abc1:
            clear_text += abc2[abc1.index(ch)]

    # числовое кодирование
    letter_encoded = text_to_codes(clear_text, abc3)

    # Подсчёт количества каждого символа с выводом на экран.
    # Создается словарь: {буква из алфавита : сколько раз встречается в тексте}
    letter_count = {letter: code for letter, code in zip(abc3, letter_encoded)}

    letter_decoded = codes_to_text(letter_encoded, abc3)

    return letter_count, letter_decoded, letter_encoded


def main():
    abc1 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"  # полный алфавит
    abc2 = "абвгдеежзийклмнопрстуфхцчшщъыьэюя"  # алфавит для замены ё на е
    abc3 = "абвгдежзийклмнопрстуфхцчшщъыьэюя"  # редуцированный алфавит

    # чтение текстового файла (с преобразованием в нижний регистр)
    with open("texts/big_text.txt", "r", encoding="utf-8") as f:
        big_text = f.read().lower()

    letter_count, letter_decoded, letter_encoded = analis_text(big_text, abc1, abc2, abc3)

    # запись результата
    with open("texts/big_text_clear.txt", "w", encoding="utf-8") as f:
        f.write(letter_decoded)

    # зашифровываем текст Цезарем и записываем в файл
    caesar_cipher_codes = cesar(letter_encoded)
    with open("texts/ceaser_ciper_text.txt", "w", encoding="utf-8") as f:
        f.write(codes_to_text(caesar_cipher_codes, abc3))

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    duration_in_seconds = end_time - start_time
    minutes, seconds = divmod(duration_in_seconds, 60)
    print(f"Программа выполнялась за: {int(minutes)} мин. {int(seconds)} сек.")
