import requests    # импорт библиотеки которая отправляет запрос и получает ответ
from bs4 import BeautifulSoup    # импорт библиотеки которая парсит html-код страницы


def get_html(url_plug):   # отправляет запрос и получает html-код страницы
    r = requests.get(url_plug)
    return r.text


def get_data(html):    # функция парсит html-код
    soup = BeautifulSoup(html, 'lxml')
    featured = soup.find_all('section')[1]    # секция featured идет 2й на странице плагинов
    return featured





def main():    # точка сборки
    url = 'https://wordpress.org/plugins/'
    print(get_data(get_html(url)))



if __name__ == '__main__':    # точка входа в скрипт
    main()

