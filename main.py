from connect_saite import connection_chrome
from get_haracers import *
from db_mysql_read import insert_book
from write_read_page import *
from len_dict import *


# 1. Выяснить кол-во страниц
# 2. Сформировать список урлов на страницы выдачи
# 3. собрать данные


def myfunc(num_page, url):
    tru = 0
    k = 0
    paste_book = []
    page_part = '?PAGEN_2='

    #print(url)
    for i in url:
        #print(i)
        k += 1
        total_pages = get_total_pages(connection_chrome(i))
        link = i
        del_url(i)
        for i in range(num_page, total_pages + 1):
            #print(i)
            url_list=[]
            dct = []
            url_gen = link + page_part + str(i)  # Формируем ссылку
            #print(url_gen)
            html = connection_chrome(url_gen)
            #print(html)
            url_list.extend(get_page_data(html, dct))
            url_l = url_list[0]
            list_dct = url_list[1]
            print(' ------- ')
            print('Страница:', i, 'из', total_pages, ',', 'Раздел: ', link + page_part + str(num_page))
            write_to_a_file_number(i)  # записать в файл текущий номер страници
            j = 0
            for list1 in url_l:
                j += 1
                pr = get_haracter(list1, list_dct[j])  # Передать список с сылками и словарь со стилями.
                haracter = main_len_dict(pr)
                print(haracter)
                insert_book(haracter)
        overwrite_a_file_url()
        write_to_a_file_number(1)
        num_page = 1  # Сбросить счетчик

def main():

    myfunc(int(num_page()), url_page())
    # try:
    #     logging.basicConfig(
    #         level=logging.DEBUG,
    #         filename="mylog.log",
    #         format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    #         datefmt='%H:%M:%S',
    #     )
    #     myfunc(int(num_page()), url_page())
    #
    # except:  # or catch one specific error with 'except AttributeError:'
    #
    #
    #     print('Нет подключения')
    #     time.sleep(300)
    #     main()


if __name__ =='__main__':
    main()