import requests
from bs4 import BeautifulSoup
from googletrans import Translator

translator = Translator()  # Инициализируем Translator здесь, чтобы использовать его глобально
# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Переводим слово и определение на русский
        translated_word = translator.translate(english_words, dest="ru").text
        translated_definition = translator.translate(word_definition, dest="ru").text

        # Чтобы программа возвращала словарь
        return {
            "english_words": english_words,
            "word_definition": translated_definition, # Возвращаем переведённое определение
            "translated_word": translated_word # Возвращаем переведённое слово

        }


    # Функция, которая сообщит об ошибке, но не остановит программу
    except Exception as e:
        print(f"Произошла ошибка: {e}")  # Выводим сообщение об ошибке
        return None


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()

        if word_dict is None:  # Проверяем, что словарь не None
            print("Не удалось получить информацию о слове. Попробуйте еще раз.")
            continue

        word = word_dict.get("english_words")  # Берем оригинальное английское слово для проверки ответа пользователя
        translated_word = word_dict.get("translated_word")  # Берем переведённое слово для вывода
        word_definition = word_dict.get("word_definition")  # Берем переведённое определение для вывода

        # Начинаем игру
        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ")

        if user.lower() == translated_word.lower(): # Сравниваем ввод пользователя с переведённым словом

            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {translated_word} ({word})")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? да/нет")
        if play_again != "да":
            print("Спасибо за игру!")
            break


word_game()
