[![Build Status](https://travis-ci.com/litdarya/LMS.svg?token=JtpoL6qhaq8diBuzrTpZ&branch=master)](https://travis-ci.com/litdarya/LMS)

# LMS

## Первый запуск

Сначала запускаем докер
```(bash)
# docker-compose up
```

Когда Docker запущен, можно заполнить создать и заполнить таблицы коммандами:
```(bash)
virtualenv venv
source venv/bin/activate
pip install -r lms/infra/db/manage_tables/requirements.txt
python lms/infra/db/manage_tables/execute_script.py --script lms/infra/db/manage_tables/sql_scripts/create_tables.sql
python lms/infra/db/manage_tables/execute_script.py --script lms/infra/db/manage_tables/sql_scripts/fill_tables.sql

```
Проверить таблицы можно через psql:
Из контейнера:
```(bash)
sudo docker exec -it lms_postgres_1 bash
psql -U admin -d lms_db
```
Локальный:
```(bash)
psql -U admin -d lms_db -h localhost
```
Проверка:
```(postgresql)
select * from users;
```
Должна получиться непустая таблица


## DEV
> #### hint
> Для быстроты разработки, секцию web в docker-compose следует закомментить, 
> далее собираем в venv:
>
> `python3 setup.py install`
>
> Теперь можно запускать так:
> 
> `python3 lms/client.py `
>
> Или использовать Pycharm для запуска

Собираем докер образы:

```(bash)
docker-compose up
```

Чтобы создать/заполнить базы, используем `lms/infra/db/*.sql`

Готово
