"""6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. """


def int_func(word):
    """
    Возвращает слово с прописной первой буквой

    :param word: слов
    :return: слово с прописной первой буквой, если слово состоит из маленьких латинский букв None в противном случае
    """

    if all([96 < ord(char) < 123 for char in word]):
        return chr(ord(word[0]) - 32) + word[1:]


while True:
    user_input = input("Введите слово из маленьких латинских букв: ")

    mod_word = int_func(user_input)
    if mod_word is not None:
        print(f"Новое слово: {mod_word}")
