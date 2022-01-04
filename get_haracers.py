# -*- coding: utf8 -*-
from bs4 import BeautifulSoup
from connect_saite import connection
from len_dict import main_len_dict
from datetime import date, datetime
#  Получить данные с карточки товара site Estima

def get_haracter(link, dct):
    list_end = {}
    list_url_foto = []
    list_sale = []
    html = connection(link)

                                    # preview
    '----------------------------------------------------------------------------'
    # Тип материала - Material_type

    try:
        type_material = dct.pop('тип материала:')  # Если есть "тип материала", то передать в переменную и удалить из словоря dct.
        teg1 = str(type_material)
        list_end['material_type'] = teg1
    except:
        list_end['material_type'] = 'none'

    '----------------------------------------------------------------------------'
    # Ссылка на карточку товара - Link_to_product_card
    teg2 = link
    list_end['link_to_product_card'] = teg2
    print(teg2)
    '----------------------------------------------------------------------------'
    # Акция, скидки, хит продаж и т.д - sale
    for tp in dct.values():
        list_sale.append(tp)
    ls = str(list_sale)
    teg3 = ls.translate(str.maketrans('', '', '[]'))
    list_end['sale'] = teg3
    if list_end == '':
        list_end['sale'] = 'none'

    '----------------------------------------------------------------------------'
                                   # Card Product
    '----------------------------------------------------------------------------'
    # Наименование товара - name
    soup = BeautifulSoup(html, 'lxml')
    soup_teg1 = soup
    teg4 = soup_teg1.find('div', {'class': 'content-block'}).find('h1').text
    list_end['name'] = teg4
    '----------------------------------------------------------------------------'
    # Ссылки на фотограии - Links_to_Photos
    soup_link_foto = soup
    try:
        link_f = soup_link_foto.find('div', {'class': 'product-block__top'})\
            .find('div', {'class': 'pictures'})\
            .find('div', {'class': 'sync-slider'})\
            .find('div', {'class': 'main-slide'})\
            .find('div', {'class': 'sync1 owl-carousel gallery-popup'})\
            .findAll('div', {'class': 'item'})

        link_foto = BeautifulSoup(str(link_f), 'html.parser')

        for link in link_foto.findAll('a'):
            list_url_foto.append('https://msk.estima.ru' + link.get('href'))
        luf = str(list_url_foto)
        teg5 = luf.translate(str.maketrans('', '', '[]'))
        list_end['links_to_Photos'] = teg5

    except:
        list_end['links_to_Photos'] = 'none'


    '----------------------------------------------------------------------------'
    # Цена за кв М2 - Price_m2
    # price_kv_m = BeautifulSoup(html, 'html.parser')
    # price = price_kv_m.find('div', {'class': 'pbb__top'})\
    # .find('div', {'class': 'prices'})\
    # .find('span', {'class': 'price'}).text
    # if price:
    #     teg6 = price
    #
    # else:
    #
    '----------------------------------------------------------------------------'
    # В 1 упаковке кв м2 - Package_m2

    try:
        upak_kv_m = BeautifulSoup(html, 'html.parser')
        sku = upak_kv_m.find('div', {'class': 'pbb__top'}).find('input', {'name': 'sqm_amount'}).get('value')
        if sku:
            teg7 = sku
        else:
            teg7 = 'None'
        list_end['package_m2'] = teg7

    except:

        list_end['package_m2'] = 'none'

    '-----------------------------------------------------------------------------'
    # Коллекция: - Collection
    # Стиль: - Style
    # Тип поверхности: - Surface_type
    # Вариативность цвета: - color_variability
    # Кол-во в упаковке, шт: - Qty_in_a_package
    # Размер, см: - Size_cm
    # Количество кв.м в упаковке: - amount_kv_m_in_a_package
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
    try:
        soup = BeautifulSoup(html, 'html.parser')
        teg = soup.find('div', {'class': 'product__desc-dls'}).children

        for t in teg:
            dt = t.find('dt')
            dd = t.find('dd')
            if dt != -1:
                if dt.text == 'Коллекция:':
                    teg8 = dd.text
                    list_end['collection'] = teg8
                if dt.text == 'Стиль:':
                    teg9 = dd.text
                    list_end['style'] = teg9
                if dt.text == 'Тип поверхности:':
                    teg10 = dd.text
                    list_end['surface_type'] = teg10
                if dt.text == 'Вариативность цвета:':
                    teg11 = dd.text
                    list_end['color_variability'] = teg11
                if dt.text == 'Кол-во в упаковке, шт:':
                    teg12 = dd.text
                    list_end['qty_in_a_package'] = teg12
                if dt.text == 'Размер, см:':
                    teg13 = dd.text
                    list_end['size_cm'] = teg13
                if dt.text == 'Количество кв.м в упаковке:':
                    teg14 = dd.text
                    list_end['amount_kv_m_in_a_package'] = teg14
                if dt.text == 'Тип товара:':
                    teg15 = dd.text
                    list_end['item_type'] = teg15
                if dt.text == 'Особенности:':
                    teg16 = dd.text
                    list_end['peculiarities'] = teg16
                if dt.text == 'Цвет:':
                    teg17 = dd.text
                    list_end['color'] = teg17
                if dt.text == 'Вид изделия:':
                    teg18 = dd.text
                    list_end['product_type'] = teg18
                if dt.text == 'Применение:':
                    teg19 = dd.text
                    list_end['application'] = teg19
                if dt.text == 'Износостойкость:':
                    teg20 = dd.text
                    list_end['wear_resistance'] = teg20
                if dt.text == 'Особенности производства:':
                    teg21 = dd.text
                    list_end['features_of_production'] = teg21
                if dt.text == 'Ректификация:':
                    teg22 = dd.text
                    list_end['rectification'] = teg22
                if dt.text == 'Фактура:':
                    teg23 = dd.text
                    list_end['texture'] = teg23
                if dt.text == 'Артикул:':
                    teg24 = dd.text
                    list_end['vendor_code'] = teg24
                if dt.text == 'Цвет массы:':
                    teg25 = dd.text
                    list_end['mass_color'] = teg25
    except:
        pass
    '-----------------------------------------------------------------------------'
    # date
    # time
    teg26 = str(date.today())
    list_end['date'] = teg26
    time = datetime.now().time()
    teg27 = str(str(time.hour) + ':' + str(time.minute) + ':' + str(time.second))
    list_end['time'] = teg27
    '-----------------------------------------------------------------------------'

    return list_end




def get_total_pages(html):# Получить кол-во страниц
    soup = BeautifulSoup(html, 'lxml')

    if soup.find('div', class_='bx-pagination-container row'):
        conteter = soup.find('div', class_='bx-pagination-container row')
        #print(conteter)
        pages =conteter.find_all('a')[-2]
        total_pages = pages.find('span').string
        return int(total_pages)
    else:
        return 1



def get_page_data(html, dct):   # Получить все ссылки на страницы с характеристиками и словарь со стилями
    url_list = []
    dct = {}
    i = 0

    soup = BeautifulSoup(html, 'lxml')
    a = soup.find_all('div', class_='catalog-list aaa-category')  # Получить весь блок в превью
    a = str(a)
    a_soup = BeautifulSoup(a, 'lxml')
    link_a = a_soup.find_all('div', class_='catalog-list__item-back')


    for link in link_a:

        i += 1
        ssulka = 'https://msk.estima.ru' + link.a.get('href')  # Взять ссылку
        #print(ssulka)
        url_list.append(ssulka)
        st = get_type_material(link)
        dct[i] = st  # Получить стили и добавить в словарь
    #dct1.append(dct)
    return url_list, dct

def get_type_material(html):

    dct = {}

    if html.find('div', {'class': 'catalog-list__item-desc'}):
        dl = html.find('div', {'class': 'catalog-list__item-desc'})
        dt = dl.find_all('dt')
        dd = dl.find_all('dd')

        dt_text = [elem.string.lower() for elem in dt]
        dd_text = [elem.string for elem in dd]

        i = 0
        for text in dt_text:
            if text == 'тип материала:':
                dct[text] = dd_text[i]
            i += 1

    try:
        if html.find('span', {'class': 'ico-new'}):
            new_product = html.find('span', {'class': 'ico-new'}).string # Взять с превью текст - Новинка
            dct['new'] = new_product
    except:
        pass

    try:
        if html.find('span', {'class': 'ico-discount'}):
                discont = html.find('span', {'class': 'ico-discount'}).string
                dct['discont'] = discont
    except:
        pass

    try:
        if html.find('span', {'class': 'ico-bestprice'}):
            best_pice = html.find('span', {'class': 'ico-bestprice'}).string
            dct['sale'] = best_pice
    except:
        pass

    try:
        if html.find('span', {'class': 'ico-hit'}):
            bestseller = html.find('span', {'class': 'ico-hit'}).string
            dct['bestseller'] = bestseller
    except:
        pass

    try:
        if html.find('span', {'class': 'ico-promo'}):
            stock = html.find('span', {'class': 'ico-promo'}).string
            dct['stock'] = stock
    except:
        pass



    return dct




