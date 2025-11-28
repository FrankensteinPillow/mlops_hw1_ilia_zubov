# Домашнее задание № 1

## Установка

### UV
Решение использует современный пакетный менеджер python `uv`. Для дальнейшей работы необходима установка только этой системной зависимости. Для его установки необходимо выполнить следующие команды:
* Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
* Linux / MacOS: `curl -LsSf https://astral.sh/uv/install.sh | sh`

### MLFlow
При исполнении пайплайна происходил логирование обучаемой модели в MLFlow. Для локального запуска необходимо выполнить команду:
```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db
```
UI сервера MLFlow будет доступен по адресу `127.0.0.1:5000`

## Запуск пайплайна
Перед началом работы с пайплайном необходимо склонировать репозиторий:
```bash
git clone git@github.com:FrankensteinPillow/mlops_hw1_ilia_zubov.git
```
Перейдём в директорию с решением:
```bash
cd mlops_hw1_ilia_zubov
```
Далее установим необходимые зависимости (список зависимостей указан в файле `pyproject.toml`):
```bash
uv sync
```
Загрузим данные, необходимые для обучения модели:
```bash
dvc pull
```
Запустим пайплайн обучения:
```bash
dvc repro
```
Проверим получившиеся метрики:
```bash
dvc metrics show
```
