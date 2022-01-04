import os
def overwrite_a_file_url():
    # прочитаем файл построчно
    with open('url.txt', 'r') as f:
        lines = f.readlines()

    # запишем файл построчно пропустив первую строку
    with open('url.txt', 'w') as f:
        f.writelines(lines[1:])


def write_to_a_file_number(i):
    fail = open('page_number.txt', 'w')
    fail.write(str(i))
    fail.close()


def num_page():
    f = open('page_number.txt')
    num_page = f.read()
    #print(num_page)
    return num_page


def url_page():
    with open('url.txt') as f:
        url = f.readlines()

    url = [x.strip() for x in url]
    return url


def del_url(i):
    tru = None
    if os.path.getsize('del_url.txt') > 0:

        with open('del_url.txt') as file:  # Проверяет входит ли ссылка в файл
            print(file)
            for line in file:
                if i in line:
                    tru = 1

        if tru != 1:
            print('не входит')
            fail = open('del_url.txt', 'a')  # Добавить url в файл del_url если ссылка не входит
            n = str([i])
            fail.write(n.replace('[', '').replace(']', '').replace('\'', '') + '\n')
            fail.close()
    else:
        print('добавил в пустой файл')
        fail = open('del_url.txt', 'a')  # Добавить url в файл del_url если файл пустой
        n = str([i])
        fail.write(n.replace('[', '').replace(']', '').replace('\'', '') + '\n')
        fail.close()