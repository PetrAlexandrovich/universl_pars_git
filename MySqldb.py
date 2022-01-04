from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import MySQLdb


def dic2sql(dic, sql):
    sf = ''

    for key in dic:
        tup = (key, dic[key])
        sf += (str(tup) + ',')

    sf = sf.rstrip(',')



    sql2 = sf
    print(type(sql2))
    return sql2


if __name__ == '__main__':
    # {'apple': 216, 'jar': 138}

    dic = {'material_type': 'Цифровой керамогранит',
           'link_to_product_card': 'https://msk.estima.ru/catalog/alba/alba-ab-01-30x60x10-nepolirovannyy/',
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

    insert = "INSERT INTO ' + estima_test +'(material_type, link_to_product_card, " \
                "sale, name, links_to_Photos, package_m2," \
                "collection, style, surface_type, color_variability, qty_in_a_package," \
                "size_cm, amount_kv_m_in_a_package, item_type, peculiarities, color," \
                "product_type, application, wear_resistance, features_of_production, " \
                "rectification, texture, vendor_code, mass_color, date, time) " \
                "values %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"
    # dic = {'apple': 216, 'jar': 138}
    # sql = "insert into users (login,userid) VALUES %s;"
    haracters = dic2sql(dic, insert)
    print(haracters)

    # Подключитесь к MySQL и отправьте данные
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(haracters)

        print(cursor)
        conn.commit()

    except Error as e:
        print('Error:', e)
        pass

    finally:
        cursor.close()
        conn.close()