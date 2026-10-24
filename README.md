# To-Do List Service

## Описание
Сервис управления списком задач на FastAPI. Помогает создавать задачи, просматривать их и отмечать выполенными.

## Установка и запуск
1. Создать окружение: `python3 -m venv .venv` 
2. Активировать: `source .venv/bin/activate`
3. Установить зависимости: `pip install -r requirements-dev.text`
4. Создать файл `.env` на основе `env.example`
5. Запустить: `uvicorn app_final:app --reload`
6. Документация: `http://127.0.0.1:8000/docs`

## Тесты
Запуск: `python -m pytest -v`

## Переменные окружения
- `APP_NAME` - название приложения.
- `APP_AUTHOR` - автор.
- `MAX_TASKS` - лимит задач.

## Диагностика
- `/health` - проверка статуса.
- `/version` - версия.
- Логи выводятся в консоль.

## Запуск без режима разработки
`uvicorn app_final:app --host 0.0.0.0 --port 8000`

