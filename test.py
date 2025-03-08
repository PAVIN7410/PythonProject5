import requests
import pprint

img = "https://fs-thb01.getcourse.ru/fileservice/file/thumbnail/h/b4f55662ac97e7dff335e875fa0166c7.png/s/s1200x/a/256825/sc/214"

#2. Прописываем запрос:

response = requests.get(img)
with open("test.jpg", "wb") as file:
    file.write(response.content)
