# Описание проекта:
### Проект представляет собой простое приложение для управления задачами (To-Do List), реализованное на FastAPI. Приложение позволяет создавать, обновлять, получать и удалять задачи.

# Создайте Docker образ и запустите контейнер:

\\\ 
docker-compose up --build
\\\ 

# Структура проекта:
main.py - маршруты и логика API.
Dockerfile - Docker образ.
docker-compose.yml - управления сервисами Docker.

# Примеры запросов:
### Создание задачи:
```
curl -X POST "http://localhost:8000/todos/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"id\":1,\"title\":\"First Task\",\"description\":\"This is the first task\",\"completed\":false}"
```
### Получение списка задач:
```
curl -X GET "http://localhost:8000/todos/" -H "accept: application/json"
``` 
### Обновление задачи:
```
curl -X PUT "http://localhost:8000/todos/1" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"id\":1,\"title\":\"Updated Task\",\"description\":\"This is the updated task\",\"completed\":true}"
```
### Удаление задачи:
```
curl -X DELETE "http://localhost:8000/todos/1" -H "accept: application/json"
```
