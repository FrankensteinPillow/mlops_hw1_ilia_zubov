# Домашнее задание № 1

## Установка

### UV
Решение использует современный пакетный менеджер python `uv`. Для дальнейшей работы необходима установка только этой системной зависимости. Для его установки необходимо выполнить следующие команды:
* Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
* Linux / MacOS: `curl -LsSf https://astral.sh/uv/install.sh | sh`

## Запуск пайплайна
Перед началом работы с пайплайном необходимо склонировать репозиторий:
```
git clone git@github.com:FrankensteinPillow/mlops_hw1_ilia_zubov.git
```
Перейдём в директорию с решением:
```
cd mlops_hw1_ilia_zubov
```
Далее установим необходимые зависимости (список зависимостей указан в файле `pyproject.toml`):
```
uv sync
```
Загрузим данные, необходимые для обучения модели:
```
dvc pull
```
Запустим пайплайн обучения:
```
dvc repro
```
Проверим получившиеся метрики:
```
dvc metrics show
```
