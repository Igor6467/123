Для того чтобы запустить скрипт сначала установите зависимости

`pip install -r requirements.txt`

После, скомпилируйте скрипт в .ехе командой:

`pyinstaller --onefile tg_bot.py`
Сам .ехе файл будет лежать в папке `./dist`

Перед тем как запустить `.exe`, удостоверьтесь что рядом с ним лежит файл `config2.yaml`
В котором описаны настройки бота!
Пример конфига - файл `config1.yaml`