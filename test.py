from bs4 import BeautifulSoup, Comment
from connect_saite import *


def get(html):# Получить кол-во страниц
    # Коллекция: - Collection
    # Стиль: - Style
    # Тип поверхности: - Surface_type
    # Вариативность цвета: - color_variability
    # Кол-во в упаковке, шт: - Qty_in_a_package
    # Размер, см: - Size_cm
    # Количество кв.м в упаковке: - amount_km_m_in_a_package
    # Тип товара: - Item_type
    # особенности: - peculiarities
    # Цвет: - color
    # Вид изделия: - Product_type
    # Применение: - application
    # Износостойкость: - Wear_resistance
    # Особенности производства: - Features_of_production
    # Ректификация: - Rectification
    # Фактура: - Texture
    # Артикул: - vendor_code
    # Цвет массы: - Mass_color

    application = []

    soup = BeautifulSoup(html, 'html.parser')
    teg = soup.find('div', {'class': 'product__desc-dls'}).children

    for t in teg:

        dt = t.find('dt')
        dd = t.find('dd')
        if dt != -1:
            if dt.text == 'Коллекция:':
                teg7 = dd.text
                print(teg7)
            if dt.text == 'Стиль:':
                teg8 = dd.text
                print(teg8)
            if dt.text == 'Тип поверхности:':
                teg9 = dd.text
                print(teg9)
            if dt.text == 'Вариативность цвета:':
                teg10 = dd.text
                print(teg10)
            if dt.text == 'Кол-во в упаковке, шт:':
                teg11 = dd.text
                print(teg11)
            if dt.text == 'Размер, см:':
                teg12 = dd.text
                print(teg12)
            if dt.text == 'Количество кв.м в упаковке:':
                teg13 = dd.text
                print(teg13)
            if dt.text == 'Тип товара:':
                teg14 = dd.text
                print(teg14)
            if dt.text == 'Особенности:':
                teg15 = dd.text
                print(teg15)
            if dt.text == 'Цвет:':
                teg16 = dd.text
                print(teg16)
            if dt.text == 'Вид изделия:':
                teg17 = dd.text
                print(teg17)
            if dt.text == 'Применение:':
                teg18 = dd.text
                print(teg18)
            if dt.text == 'Износостойкость:':
                teg19 = dd.text
                print(teg19)
            if dt.text == 'Особенности производства:':
                teg20 = dd.text
                print(teg20)
            if dt.text == 'Ректификация:':
                teg21 = dd.text
                print(teg21)
            if dt.text == 'Фактура:':
                teg22 = dd.text
                print(teg22)
            if dt.text == 'Артикул:':
                teg23 = dd.text
                print(teg23)
            if dt.text == 'Цвет массы:':
                teg24 = dd.text
                print(teg24)

def main():

    get(connection_chrome('https://msk.estima.ru/catalog/alba/alba-ab-01-30x60x10-nepolirovannyy/'))


if __name__ =='__main__':
    main()