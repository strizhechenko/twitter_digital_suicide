# Что это

Скрипт для удаления вообще всех твитов из вашего аккаунта.

# Как установить

	git clone git@github.com:strizhechenko/twitter_digital_suicide.git
	cd twitter_digital_suicide
	virtualenv env
	. env/bin/activate
	pip install -r requirements.txt

# Где взять архив твитов и куда положить

Заходите в настройки учётной записи твиттера и где-то там запрашиваете архив твитов. Кладёте в twitter.zip прямо в папке проекта.

# Как запустить

## Нужен APP в твиторе

Зарегать апп в твиторе и авторизоваться в нём по [доке](https://github.com/strizhechenko/twitterbot_example#%D0%90%D0%B2%D1%82%D0%BE%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B5%D0%B9)

## Удаляйте уже мои твиты

	. env/bin/activate
	python deleter_archive.py

# Что ещё тут есть интересного?

deleter.py - скрипт удаляет всё кроме последних 100 твитов. Можно положить в крон.

# Полезности

Ещё есть скрипт env.sh для того чтобы запускать кодяку несколько раз.
