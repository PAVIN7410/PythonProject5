from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Chrome()

def search_wikipedia(query):
    browser.get("https://ru.wikipedia.org/wiki/" + query)

def list_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)

def list_links():
    links = browser.find_elements(By.TAG_NAME, "a")
    for link in links:
        print(link.get_attribute("href"))

def main():
    query = input("Введите запрос: ")
    search_wikipedia(query)

    while True:
        action = input("Выберите действие: 1 - листать параграфы, 2 - перейти на одну из связанных страниц, 3 - выйти из программы: ")
        if action == "1":
            list_paragraphs()
        elif action == "2":
            list_links()
            link = input("Введите ссылку: ")
            search_wikipedia(link)
        elif action == "3":
            break

if __name__ == "__main__":
    main()

