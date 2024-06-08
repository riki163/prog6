**Лабораторная работа 9 **
Реализовать локальное развертывание проекта на FastAPI и продемонстрировать это развертывание. 

**Шаги реализации:
  1. Создание файла "main.py" со следующим содержимым:**
      from fastapi import FastAPI
    
      app = FastAPI()
    
      @app.get("/")
      def read_root():
        return {"Hello": "World"}
**2. Создание Dockerfile**
  1. Создайть файл Dockerfile со следующим содержимым:
      FROM python:3.9

      WORKDIR /app
      
      COPY requirements.txt .
      RUN pip install --no-cache-dir -r requirements.txt
      
      COPY . .
      
      CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
**3. Создайте файл requirements.txt со следующим содержимым:**
     fastapi
     uvicorn

**4. Сборка Docker-образа**
      docker build -t fastapi-project .
      <img width="567" alt="image" src="https://github.com/riki163/prog6/assets/99810152/96c30f96-5a93-4806-b35e-d10850bb0d75">

**5. Запуск Docker-контейнера**

       docker run -d --name fastapi-container -p 8000:8000 fastapi-project
        ![image](https://github.com/riki163/prog6/assets/99810152/bc235902-44db-4045-b5e7-238368646b73)

