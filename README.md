# api для социальной сети
API соцсети, позволяющий добавлять записи, комментировать, подписываться на пользователей.
### Технологии:
Python, Django, DRF, JWT
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:CrockoMan/api_foryatubehelp.git
```

```
cd api_foryatubehelp
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
Работа с постами:<br />
<http://127.0.0.1:8000/api/v1/posts/><br />
```
GET Получить список публикаций.
Response:
{
  "count": 123,
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2023-10-08T13:50:35.424Z",
      "image": "string",
      "group": 0
    }
  ]
}
При указании limit и offset выдача будет с  пагинацией, при наличии достаточного количества записей для пагинации
Response:
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2023-10-08T13:50:35.424Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
```
POST: Добавить публикацию
{
  "text": "string",
  "image": "string",
  "group": 0
}
Response:
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2023-10-08T13:52:53.162Z",
  "image": "string",
  "group": 0
}
```
<http://127.0.0.1:8000/api/v1/posts/{id}/> - Работа с постом {id}<br />
```
http://127.0.0.1:8000/api/v1/posts/{id}/
GET
Response:
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2023-10-08T13:54:21.976Z",
  "image": "string",
  "group": 0
}
```
```
PUT PATCH
{
  "text": "string",
  "image": "string",
  "group": 0
}
Response:
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2023-10-08T13:54:21.979Z",
  "image": "string",
  "group": 0
}
```
```
DELETE
No response body
```
Работа с комментариями осуществляется по id поста, к которому опубликован/публикуется комментарий, например:<br />
<http://127.0.0.1:8000/api/v1/posts/{id}/comments/> - работа с комментариями 
поста id<br />
```
GET
Response:
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2023-10-08T14:01:43.545Z",
    "post": 0
  }
]
```
```
POST
{
  "text": "string"
}
Response:
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2023-10-08T14:02:11.024Z",
  "post": 0
}
```
<http://127.0.0.1:8000/api/v1/posts/{id}/comments/{id}> - При указании id 
поста и id комментария, возможна работа с комментарием<br />
```
GET
Response:
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2023-10-08T14:04:24.189Z",
  "post": 0
}
```
```
PUT
{
  "text": "string"
}
Response:
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2023-10-08T14:04:45.939Z",
  "post": 0
}
```
```
DELETE
No response body
```
Работа с группами:<br />
<http://127.0.0.1:8000/api/v1/groups/><br />
```
GET Получить список групп.
Response:
[
  {
    "id": 0,
    "title": "string",
    "slug": "ciYncA_9Go1aRPdDJpHtss2cZafcNoPO3k_8YUXSNUmoWkRvqw",
    "description": "string"
  }
]
```
<http://127.0.0.1:8000/api/v1/groups/{id}/><br />
```
GET Получить группу.
Response:
{
  "id": 0,
  "title": "string",
  "slug": "ktSquiMZl2Cu4PxgxWqEoocBkysxQrofmZgDGUk4-0NNFUmWqE",
  "description": "string"
}
```
Работа с подписками:<br />
<http://127.0.0.1:8000/api/v1/follow/><br />
```
GET Получить список подписок.
Response:
[
  {
    "user": "string",
    "following": "string"
  }
]
```
```
POST Подписаться
{
  "following": "string"
}
Response:
{
  "user": "string",
  "following": "string"
}
```
Автор: [К.Гурашкин](<https://github.com/CrockoMan>)
