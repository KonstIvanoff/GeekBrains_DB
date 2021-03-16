import json
from pymongo import MongoClient

mongourl = '127.0.0.1:27017'
mongodb = 'Recruitment'

def cont_vacancies():

    # допустим, имеем файл с новыми вакансиями (или результат парсинга), нужно актуализировать базу
    with open('hhcc.json','r') as st:
        vac_list = json.load(st)

    with MongoClient(mongourl) as client:
        db = client[mongodb]
        coll = db.myvacancies

    # проверяем наличие вакансий в баз (по ссылке)
    i = 0
    newvacs = []
    for vac in vac_list:
        vac_lnk = vac['link']
        # print(vac_lnk)
        qr = coll.find_one({'link':vac_lnk})
        # если ссылка не нашлась - загружаем вакансию в БД (используем уже имеющуюся процедуру)
        if qr == None:
            newvacs.append(vac)
            i += 1

    if i > 0:
        save_to_mongo(newvacs)
    print(f'Добавлено {i} вакансий.')

# сохранение данных в БД Mongo
def save_to_mongo(v_data):

    # очистка данных
    # удаляем "пустые" вакансии - только одна запись в словаре (их много в данных Superjob)
    i = 0
    while i < len(v_data):
        j = v_data[i]
        if len(j) == 1:
            del v_data[i]
        i += 1

    # ищем и удаляем пустые пары в словаре вакансии (если не указана зарплата)
    fordel = []
    i = 0
    while i < len(v_data):
        j = v_data[i]
        for k, w in j.items():
            if w == None or w == '':
                fordel.append([i, k])
        i += 1
    # удаление по собранным данным (номер вакансии, ключ пары)
    for i in fordel:
        n = i[0]
        k = i[1]
        del v_data[n][k]

    mongourl = '127.0.0.1:27017'
    mongodb = 'Recruitment'

    # запись в базу
    with MongoClient(mongourl) as cli:
        db = cli[mongodb]
        mycollection = db.myvacancies

        mycollection.insert_many(v_data)

cont_vacancies()