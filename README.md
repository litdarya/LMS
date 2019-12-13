# LMS

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
