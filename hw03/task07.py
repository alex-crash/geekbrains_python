"""7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово
состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
заглавной буквы. Необходимо использовать написанную ранее функцию int_func(). """


def int_func(word):
    """
    Возвращает слово с прописной первой буквой

    :param word: слов
    :return: слово с прописной первой буквой, если слово состоит из маленьких латинский букв None в противном случае
    """

    if all([96 < ord(char) < 123 for char in word]):
        return chr(ord(word[0]) - 32) + word[1:]


while True:
    user_input = input("Введите слова из латинских букв в нижнем регистре, разделенные пробелами: ").split()

    new_list = list(map(int_func, user_input))
    if all([word is not None for word in new_list]):
        print(f"Новое предложение: {' '.join(new_list)}")