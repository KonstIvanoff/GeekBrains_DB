-- Практическое задание по теме «Операторы, фильтрация, сортировка и ограничение»
-- 1.Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем.

-- vk.users definition

/*
CREATE TABLE `users` (
  `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT 'Идентификатор строки',
  `first_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT 'Имя пользователя',
  `last_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT 'Фамилия пользователя',
  `email` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT 'Почта',
  `phone` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT 'Телефон',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP COMMENT 'Время создания строки',
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Время обновления строки',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Пользователи';
*/

-- поскольку updated_at промечается текущей датой/временем по умолчанию, достаточно обновить поле created_at
update vk.users set created_at = now();
select * from vk.users limit 5;

/*
id	first_name	last_name	email						phone				created_at			updated_at
1	Beaulah		Schmitt		aullrich@example.org		250-625-7760x6968	2020-12-31 13:45:01	2020-12-31 13:45:01
2	Domingo		Kessler		o'keefe.reilly@example.org	07180345887			2020-12-31 13:45:01	2020-12-31 13:45:01
3	Elta		Aufderhar	einar.will@example.org		052-585-7493		2020-12-31 13:45:01	2020-12-31 13:45:01
4	Sebastian	Osinski		shany10@example.com			657.630.6935		2020-12-31 13:45:01	2020-12-31 13:45:01
5	Barton		Romaguera	geovanni.sauer@example.org	(412)764-2288x29829	2020-12-31 13:45:01	2020-12-31 13:45:01
*/

-- 2. Таблица users была неудачно спроектирована. Записи created_at и updated_at были заданы типом VARCHAR и в них долгое время помещались значения в формате 20.10.2017 8:10. 
-- Необходимо преобразовать поля к типу DATETIME, сохранив введённые ранее значения.

create temporary table users_1
(
  `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT 'Идентификатор строки',
  `first_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT 'Имя пользователя',
  `last_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT 'Фамилия пользователя',
  `email` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT 'Почта',
  `phone` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT 'Телефон',
  `created_at` varchar(50) not null, -- datetime DEFAULT CURRENT_TIMESTAMP COMMENT 'Время создания строки',
  `updated_at` varchar(50) not null, -- datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Время обновления строки',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`)
);

INSERT INTO vk.users_1 (first_name, last_name, email, phone, created_at, updated_at)
select first_name, last_name, email, phone, created_at, updated_at from users limit 10;

alter table users_1 modify created_at datetime;
alter table users_1 modify updated_at datetime;

desc users_1;

select created_at, updated_at from users_1;

/*
created_at 				updated_at
2020-12-31 13:45:01		2020-12-31 13:45:01
2020-12-31 13:45:01		2020-12-31 13:45:01
2020-12-31 13:45:01		2020-12-31 13:45:01
2020-12-31 13:45:01		2020-12-31 13:45:01
*/

/*
3.В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры: 0, если товар закончился и выше нуля, если на складе имеются запасы. 
Необходимо отсортировать записи таким образом, чтобы они выводились в порядке увеличения значения value. 
Однако нулевые запасы должны выводиться в конце, после всех 
*/

create temporary table storehouses_products (id serial, product varchar(50), value float);

select * from storehouses_products;

insert into storehouses_products(product,value) values ('ПИВО',0),('ВОДКА',2500),('ВИСКИ',0),('КОНЬЯК',30),('ТЕКИЛА',500),('РОМ',1);

select * from storehouses_products order by if(value=0,1000000000,value) asc;

/*
6	РОМ		1.0
4	КОНЬЯК	30.0
5	ТЕКИЛА	500.0
2	ВОДКА	2500.0
1	ПИВО	0.0
3	ВИСКИ	0.0
*/

-- 4.(по желанию) Из таблицы users необходимо извлечь пользователей, родившихся в августе и мае. 
-- Месяцы заданы в виде списка английских названий (may, august)

select user_id, birthday, monthname(birthday) as mnth from profiles where monthname(birthday) in ('may','august');

/*
user_id	birthday	mnth
14		1973-08-02	August
15		1991-05-02	May
19		2002-08-09	August
23		1996-08-02	August
...
*/

-- 5. (по желанию) Из таблицы catalogs извлекаются записи при помощи запроса. SELECT * FROM catalogs WHERE id IN (5, 1, 2); 
-- Отсортируйте записи в порядке, заданном в списке IN.

create temporary table catalogs (id serial, NAME varchar(100), amount float)

insert into catalogs(NAME, amount) values ('телевизоры',100),('чайники',500),('мясорубки',300),('холодильники',150),('компьютеры',75),('ноутбуки',180),('телефоны',220);

select * from catalogs WHERE id IN (5, 1, 2) order by (case id when 5 then 1 when 1 then 2 when 2 then 3 else 99 end);
/*
5	компьютеры	75.0
1	телевизоры	100.0
2	чайники		500.0
*/


-- Практическое задание теме «Агрегация данных»
-- 1.Подсчитайте средний возраст пользователей в таблице users.

select avg(timestampdiff(YEAR, birthday, now())) as avg_age from profiles;
--32.2800

-- 2.Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели.
-- Следует учесть, что необходимы дни недели текущего года, а не года рождения.

select  -- birthday, 
-- ( cast('2020-01-01' as date) + INTERVAL month(birthday)-1 MONTH + INTERVAL day(birthday)-1 DAY ) as birthday_this_year,
weekday(cast('2020-01-01' as date) + INTERVAL month(birthday)-1 MONTH + INTERVAL day(birthday)-1 DAY ) num,
dayname( cast('2020-01-01' as date) + INTERVAL month(birthday)-1 MONTH + INTERVAL day(birthday)-1 DAY ) wd, count(*) as cnt
from profiles
group by num, wd order by num

-- 3.(по желанию) Подсчитайте произведение чисел в столбце таблицы.
create temporary table num (num int);

insert into num values (1),(2),(3),(4),(5);

--  совершенно честно сгуглил решение, экспонента суммы логарифмов...
select round(exp(sum(log(num))),10) as res from num;
--120.0








