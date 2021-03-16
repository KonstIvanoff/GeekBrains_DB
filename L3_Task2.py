from pymongo import MongoClient

mongourl = '127.0.0.1:27017'
mongodb = 'Recruitment'

def find_vacancies(salary_min, salary_max):

    with MongoClient(mongourl) as cli:
        db = cli[mongodb]
        mycollection = db.myvacancies

        if not salary_min == None and not salary_max ==None:
            res = mycollection.find({'$and':[{'salary_min':{'$gte':salary_min}},{'salary_max':{'$lte':salary_max}}]}
                                    ,{'_id': 0, 'name': 1, 'company': 1, 'salary': 1, 'salary_min': 1, 'salary_max': 1, 'link':1})
        elif salary_min == None and not salary_max == None:
            res = mycollection.find({'salary_max': {'$lte': salary_max}},
                                    {'_id': 0, 'name': 1, 'company': 1, 'salary': 1, 'salary_min': 1, 'salary_max': 1, 'link': 1})
        elif not salary_min == None and salary_max == None:
            res = mycollection.find({'salary_max': {'$gte': salary_min}},
                                    {'_id': 0, 'name': 1, 'company': 1, 'salary': 1, 'salary_min': 1, 'salary_max': 1, 'link': 1})
        elif salary_min == None and salary_max == None:
            # res = mycollection.find({'$and':[ {'salary_max': {'$exists':'false'}},{'salary_min': {'$exists':'false'}} ]},
            #                         {'_id': 0, 'name': 1, 'company': 1, 'salary': 1, 'salary_min': 1, 'salary_max': 1, 'link': 1})
            res = mycollection.find({'$and':[{'salary_min':{'$exists':0}},{'salary_max':{'$exists':0}}]}, {'_id': 0, 'name': 1, 'company': 1, 'salary': 1, 'salary_min': 1, 'salary_max': 1, 'link': 1})

        return res

# ЗП в заданных границах
# for vac in find_vacancies(50000, 100000):
#     print(vac)

# ЗП с заданным минимумом
# for vac in find_vacancies(50000, None):
#     print(vac)

# ЗП с заданным максимумом
# for vac in find_vacancies(None, 150000):
#     print(vac)

# ЗП не указана
for vac in find_vacancies(None, None):
    print(vac)
