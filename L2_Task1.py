import requests, json, time, pickle, re
from bs4 import BeautifulSoup as bsp
from pprint import pprint
from pymongo import MongoClient

# парсинг строки зарплат
def parse_salary(self, sal):
        c1 = None
        c2 = None
        val = ['']

        if sal == '':
                return c1, c2, val[0]

        mystr = sal.replace(' ', '').replace(chr(160), '')
        res = re.findall(r'\d+', mystr)
        # print(sal, mystr, res)
        if len(res) == 2:
                c1, c2 = res[0], res[1]
        elif len(res) == 1:
                try:
                        i = mystr.index('от')
                        c1, c2 = res[0], None
                except ValueError:
                        c1, c2 = res[0], res[0]

        if len(res) > 0:
                val = re.findall(r'\D{3}', mystr)

        return [c1, c2, val[0]]

class hh_parsing():
        def __init__(self, whatfind, filepth):
            self.whatfind = whatfind
            self.filepth = filepth

        # разбор вакансий
        def parse_vac(self, vacs):
                res = []
                for i in vacs:
                        currentvac = {}
                        vacinfo = i.findChild(attrs={'class': 'vacancy-serp-item__info'}).find('a')
                        currentvac['source'] = 'hh.ru'
                        currentvac['name'] = vacinfo.text
                        currentvac['link'] = vacinfo['href']
                        mysal = i.findChild(attrs={'class': 'vacancy-serp-item__sidebar'}).text
                        currentvac['salary'] = mysal
                        mysalparsed = parse_salary(mysal)
                        currentvac['salary_min'], currentvac['salary_max'], currentvac['salary_currency'] = map(
                                lambda x: x, mysalparsed)
                        currentvac['company'] = i.findChild('div', attrs={
                                'class': 'vacancy-serp-item__meta-info-company'}).text
                        currentvac['address'] = i.findChild('span', attrs={
                                'data-qa': 'vacancy-serp__vacancy-address'}).text
                        res.append(currentvac)
                return res


        def parse(self):
                base_url = 'https://hh.ru/search/vacancy'
                myparams = {'clusters':'true', 'enable_snippets':'true', 'salary':'', 'st':'searchVacancy', 'text':self.whatfind, 'from':'suggest_post'}
                myheaders = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5'}
                myproxy = {'https': 'https://51.158.107.202:9999'}

                myvacancies = []
                mypage = 0

                while True:
                        qr = requests.get(base_url, headers=myheaders, params=myparams, proxies=myproxy)

                        if not qr.status_code == 200:
                                print('Запрос страницы отработал некорректно!')
                                mypage += 1
                                myparams = {'L_is_autosearch': 'false', 'clusters': 'true', 'enable_snippets': 'true', 'text': 'PLSQL',
                                            'page': str(mypage)}
                                time.sleep(2)
                                continue
                        mydoc = qr.text
                        mysoup = bsp(mydoc,'html.parser')

                        # тег, содержащий вакансии
                        root = mysoup.find(attrs={'class':'vacancy-serp'})
                        # выбираем вакансии
                        # премиальные вакансии
                        vacs = root.findChildren('div', attrs={'data-qa': 'vacancy-serp__vacancy vacancy-serp__vacancy_premium', 'class': ['vacancy-serp-item', 'vacancy-serp-item_premium']}, recursive=False)
                        myvacancies += self.parse_vac(vacs)
                        # обычные вакансии
                        vacs = root.findChildren('div', attrs={'data-qa': 'vacancy-serp__vacancy'},recursive=False)
                        myvacancies += self.parse_vac(vacs)

                        # ищем кнопку "Дальше"
                        buttons = mysoup.find('div', attrs={'data-qa': 'pager-block'})
                        buttonnext = buttons.findChild('a', text='дальше')
                        print(f'Обработано страниц {str(mypage + 1)}')
                        # break
                        if buttonnext == None:
                                break
                        else:
                                mypage += 1
                                myparams = {'L_is_autosearch':'false', 'clusters':'true', 'enable_snippets':'true', 'text':self.whatfind, 'page':str(mypage)}
                                time.sleep(2)

                with open (self.filepth,'w') as f:
                        json.dump(myvacancies, f, indent=2, ensure_ascii=False)


class superjob_parsing():
        def __init__(self, whatfind, filepth):
            self.whatfind = whatfind
            self.filepth = filepth

       def parse(self):
                base_url = 'https://www.superjob.ru/vacancy/search'
                myparams = {'keywords': self.whatfind, 'noGeo':'1'}
                myheaders = {
                        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5'}
                myproxy = {'https': 'https://51.158.107.202:9999'}

                myvacancies = []
                mypage = 1

                while True:
                        qr = requests.get(base_url, headers=myheaders, params=myparams, proxies=myproxy)

                        if qr.status_code == 200:
                                mysoup = bsp(qr.text, 'html.parser')

                                root = mysoup.findChild('div', attrs={'class': '_1ID8B'})
                                vacs = root.findChildren('div', attrs={'class': 'f-test-search-result-item'})
                                for i in vacs:
                                        currentvac = {}
                                        currentvac['source'] = 'www.superjob.ru'
                                        try:
                                                titl = i.findChild('div', attrs={'class': 'jNMYr GPKTZ _1tH7S'})
                                                currentvac['name'] = titl.findChild('a').text
                                                currentvac['link'] = 'www.superjob.ru' + titl.findChild('a')['href']
                                                currentvac['salary'] = i.findChild('span', attrs={
                                                        'class': '_3mfro _2Wp8I PlM3e _2JVkc _2VHxz'}).text
                                                mysalparsed = parse_salary(currentvac['salary'])
                                                currentvac['salary_min'], currentvac['salary_max'], currentvac[
                                                        'salary_currency'] = map(lambda x: x, mysalparsed)
                                                currentvac['company'] = i.findChild('span', attrs={
                                                        'class': '_3mfro _3Fsn4 f-test-text-vacancy-item-company-name _9fXTd _2JVkc _2VHxz _15msI'}).text
                                                currentvac['address'] = i.findChild('span', attrs={
                                                        'class': '_3mfro f-test-text-company-item-location _9fXTd _2JVkc _2VHxz'}).text
                                        except:
                                                # pprint(i)
                                                continue
                                        myvacancies.append(currentvac)
                                print(f'Обработано страниц {str(mypage)}')

                                mypage += 1
                                nextbutton = mysoup.findChild('a', text='Дальше')
                                if nextbutton == None:
                                        break
                                else:
                                        myparams['page'] = str(mypage)
                                        time.sleep(2)

                with open(self.filepth, 'w') as f:
                        json.dump(myvacancies, f, indent=2, ensure_ascii=False)

hh = hh_parsing('C++','hhcc.json')
hh.parse()

sj = superjob_parsing('SQL Server','sjcc.json')
sj.parse()







