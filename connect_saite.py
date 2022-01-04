import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

def connection(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
    cookies = {

        '_ga': 'GA1.2.551334266.1617648921',
        '_gid': 'GA1.2.1253871043.1617648921',
        '_ym_d': '20',
        '_ym_isad': '2',
        '_ym_uid': '20357505',
        'KG_GUEST_ID': '22375451',
        'KG_SALE_UID': '182286207',
        'PHPSESSID': 'r8GVZWcidL6batopsVfKyOtdKc8REaGn'
    }

    res = requests.get(url, headers=headers, cookies=cookies)

    todos = res.text
    return todos


def connection_chrome(link):

    #chromedriver = 'C:\\Users\\Baron\\Dropbox\\msm\\chromedriver'
    chromedriver = 'C:\\Users\\Пользователь\\Dropbox\\msm\\chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # для открытия headless-браузера
    browser = webdriver.Chrome(options=options, executable_path=chromedriver)

    # Переход на страницу входа
    browser.get(link)
    requiredHtml = browser.page_source


    return requiredHtml


def connection_firefox(link):

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
    cookies = {

        '_ga': 'GA1.2.551334266.1617648921',
        '_gid': 'GA1.2.1253871043.1617648921',
        '_ym_d': '20',
        '_ym_isad': '2',
        '_ym_uid': '20357505',
        'KG_GUEST_ID': '22375451',
        'KG_SALE_UID': '182286207',
        'PHPSESSID': 'r8GVZWcidL6batopsVfKyOtdKc8REaGn'
    }


    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path=r'C:\Users\Пользователь\Dropbox\msm\chromedriver_win32\geckodriver.exe')
    driver.get(link)
    #time.sleep(5)
    #driver.set_timeout(5)
    requiredHtml = driver.page_source
    #print(requiredHtml)
    driver.quit()
    return requiredHtml
