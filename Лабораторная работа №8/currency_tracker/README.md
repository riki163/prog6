# Установка Poetry
```
curl -sSL https://install.python-poetry.org | python3 -
```

# Установка зависимостей:
```
poetry install
```

# Добавление Sphinx для документации:
```
poetry add -D sphinx
```

# Создание виртуального окружения 
```
python -m venv .venv
source .venv/bin/activate
```

# Инициализация документации с помощью Sphinx:
```
poetry run sphinx-quickstart docs
```

# Сборка документации:
```
poetry run sphinx-build -b html docs docs/_build
```

