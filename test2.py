from bs4 import BeautifulSoup
from connect_saite import connection_chrome
from len_dict import main_len_dict

def get_total_pages(html):# Получить кол-во страниц

    spisok = dict()

    soup = BeautifulSoup(html, 'lxml')

    if soup.body:
        dl = soup.find_all('dl', {'class': 'cat-article-params'})

    for teg in dl:
        teg_1 = teg.find_all('dt')
        teg_2 = teg.find_all('dd')
        for teg1, teg2 in zip(teg_1, teg_2):
            seq = teg1.text.lower()
            value = teg2.text
            spisok[seq] = value
    spisok_end = main_len_dict(spisok)



def main():

    get_total_pages(connection_chrome('https://www.keramogranit.ru/catalog-products/keramicheskaya-plitka/'))

if __name__ =='__main__':
    main()
