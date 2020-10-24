import requests    # импорт библиотеки которая отправляет запрос и получает ответ
from bs4 import BeautifulSoup    # импорт библиотеки которая парсит html-код страницы
import csv    # импорт библиотеки для работы с csv файлами



def get_html(url_plug):   # отправляет запрос и получает html-код страницы
    r = requests.get(url_plug)
    return r.text


def refined_data(s):    # функция делит список по преболам и в 0-м элементе удаляет запятую
    # 1,554 total ratings
    rate = s.split(' ')[0]
    return rate.replace(',', '') 


def write_csv(d):    # функция записывает данные в csv-file
    with open('plugins.csv', 'a') as f:    # 'a' - append
        writer = csv.writer(f)

        writer.writerow((d['name'],
                         d['url'],
                         d['views'])) 


def get_data(html):    # функция парсит html-код
    soup = BeautifulSoup(html, 'lxml')
    featured = soup.find_all('section')[1]    # секция featured идет 2й на странице плагинов
    plugines = featured.find_all('article')    # вытягивание инфы о каждом блоке в выбр.разделе 
    
    for plugin in plugines:    # цикл перебирает теги и забирает нужные данные в них
        name_plugin = plugin.find('h3').text
        link_plugin = plugin.find('h3').find('a').get('href') 
        
        rate_plugin = plugin.find('span', class_='rating-count').find('a').text
        rate = refined_data(rate_plugin)    # для очистки данных, передали строку в функцию по очистке данных

        data = {'name': name_plugin,
                'url': link_plugin,
                'views': rate   
               }

        # print(data)
        write_csv(data)



def main():    # точка сборки
    url = 'https://wordpress.org/plugins/'
    print(get_data(get_html(url)))



if __name__ == '__main__':    # точка входа в скрипт
    main()
