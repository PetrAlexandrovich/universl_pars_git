from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from len_dict import *

def insert_book(dic):

    # columns = dic.keys()
    # haracters = [dic[column] for column in columns]
    # haracters = main_len_dict(dic)
    # print(haracters)
    haracters = dic

    insert = "INSERT INTO estima(material_type, link_to_product_card, " \
                "sale, name, links_to_Photos, package_m2," \
                "collection, style, surface_type, color_variability, qty_in_a_package," \
                "size_cm, amount_kv_m_in_a_package, item_type, peculiarities, color," \
                "product_type, application, wear_resistance, features_of_production, " \
                "rectification, texture, vendor_code, mass_color, date, time) " \
                "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(insert, haracters)

        print(cursor)
        conn.commit()

    except Error as e:
        print('Error:', e)
        pass

    finally:
        cursor.close()
        conn.close()


def main():
    #'mterial_type': 'Цифровой керамогранит',
    dic = {'link_to_product_card': 'https://msk.estima.ru/catalog/alba/alba-ab-01-30x60x10-nepolirovannyy/',
           'sale': "'Новинка '",
           'name': 'Керамическая плитка Alba AB 01 30x60x10 Неполированный',
           'links_to_Photos': "'https://msk.estima.ru//upload/iblock/2f0/AB_01-30x60-22_1.jpg'",
           'package_m2': '1.080',
           'collection': 'Alba',
           'style': 'Мрамор',
           'surface_type': 'Неполированный',
           'color_variability': 'Средняя',
           'qty_in_a_package': '6',
           'size_cm': '30x60',
           'amount_kv_m_in_a_package': '1,08',
           'item_type': 'Керамическая плитка',
           'peculiarities': 'Морозостойкий',
           'color': 'Белый, Светлый',
           'product_type': 'Плитка',
           'application': 'Для бассейна',
           'wear_resistance': 'PEI III',
           'features_of_production': 'Глазурованный керамогранит',
           'rectification': 'Да',
           'texture': 'мрамор',
           'vendor_code': 'AB01/NS_NC/30x60x10R/GW',
           'mass_color': 'белая',
           'date': '2021-10-20',
           'time': '16:12:17'
          }
    dic1 = {'material_type': 'Цифровой керамогранит',
            'link_to_product_card': 'https://msk.estima.ru/catalog/keramogranit/seriy/ar-01-40-5x40-5kh8-nepolirovannyy/',
            'sale': "'Новинка '",
            'name': 'Керамическая плитка AR 01 40,5x40,5х8 Неполированный',
            'links_to_Photos': "'https://msk.estima.ru/upload/resize_cache/iblock/8e3/1920_1080_1/AR01_1.jpg', 'https://msk.estima.ru/upload/resize_cache/iblock/5a0/1920_1080_1/AR01_2.jpg', 'https://msk.estima.ru/upload/resize_cache/iblock/0ec/1920_1080_1/AR01_3.jpg', 'https://msk.estima.ru/upload/resize_cache/iblock/2ae/1920_1080_1/AR01_4.jpg', 'https://msk.estima.ru/upload/resize_cache/iblock/cc1/1920_1080_1/AR01_5.jpg', 'https://msk.estima.ru/upload/resize_cache/iblock/d08/1920_1080_1/AR01_6.jpg', 'https://msk.estima.ru/upload/resize_cache/iblock/471/1920_1080_1/AR01_7.jpg', 'https://msk.estima.ru/upload/resize_cache/iblock/5d2/1920_1080_1/AR01_8.jpg', 'https://msk.estima.ru/upload/resize_cache/iblock/391/1920_1080_1/AR01_9.jpg'",
            'package_m2': '1.804',
            'collection': 'Art',
            'style': 'Дизайн',
            'surface_type': 'Неполированный',
            'color_variability': 'Существенная',
            'qty_in_a_package': '11',
            'size_cm': '40.5x40.5',
            'amount_kv_m_in_a_package': '1,804',
            'item_type': 'Керамическая плитка',
            'peculiarities': 'Морозостойкий',
            'color': 'Бежевый, Светлый, Серый, Темный',
            'product_type': 'Плитка',
            'application': 'Для бассейна, Для ванной, Для гостиной, Для коридора, Для кухни, Для пола, Для стен, Для улицы, Для фасада, для внутренней отделки, для гаража, для дачи, для дома, для дорожек, для камина, для квартиры, для комнаты, для крыльца, для лестницы, для наружных работ, для печи, для ступеней, для туалета, для фартука',
            'wear_resistance': 'PEI IV',
            'features_of_production': 'Глазурованный керамогранит',
            'rectification': 'Да',
            'vendor_code': 'AR01/NS_R9/40,5x40,5x8N/GW',
            'mass_color': 'белая',
            'date': '2021-10-20',
            'time': '18:27:38'}


    insert_book(dic)

if __name__ == '__main__':
    main()