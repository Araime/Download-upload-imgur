# Download-upload-imgur

Консольное приложение для загрузки изображений с API веб-сервисов [Spacex](https://documenter.getpostman.com/view/2025350/RWaEzAiG#bc65ba60-decf-4289-bb04-4ca9df01b9c1) 
и [Hubble](http://hubblesite.org/api/documentation), их последующей обработки 
и загрузки на сервис [imgur](https://imgur.com/).

### Как установить?

#### Скачать

Python3 должен быть уже установлен. Скачать этот репозиторий себе на компьютер.

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html)
для изоляции проекта.

#### Быстрая настройка venv

Начниая с Python версии 3.3 виртуальное окружение идёт в комплекте в виде модуля
venv. Чтобы его установить и активировать нужно выполнить следующие действия в
командной строке:  

Указать скачанный репозиторий в качестве каталога.
```
cd C:\Users\ваш_пользователь\Downloads\папка_репозитория
```
Установить виртуальное окружение в выбраном каталоге.
```
Python -m venv env
```
В репозитории появится папка виртуального окружения env
<a href="https://imgbb.com/"><img src="https://i.ibb.co/Hn4C6PD/image.png" alt="image" border="0"></a>

Активировать виртуальное окружение.
```
env\scripts\activate
```
Если всё сделано правильно, вы увидите в командной строке (env) слева от пути 
каталога.
<a href="https://imgbb.com/"><img src="https://i.ibb.co/MZ72r22/2.png" alt="2" border="0"></a>

#### Установить зависимости

Используйте `pip` (или `pip3`, есть конфликт с Python2) для установки 
зависимостей:

```python
pip install -r requirements.txt
```

### Зарегистрироваться на imgur и создать приложение

#### Регистрация на Imgur

Если вы регистрируетесь на [imgur](https://imgur.com/) с домашнего компьютера, он
может не принять ваш номер телефона. В таком случае луше зарегистрироваться с
мобильного устройства, скачав приложение imgur.

#### Создание приложения

После регистрации необходимо пройти по [ссылке](https://api.imgur.com/oauth2/addclient) 
и создать приложение. В поле `Authorization callback URL` напишите `http://localhost`  
<a href="https://ibb.co/b6MbmrL"><img src="https://i.ibb.co/PrvDj54/image.png" alt="image" border="0"></a>

Вы получите client-id и client-secret.  
<a href="https://ibb.co/SxYVbwY"><img src="https://i.ibb.co/9vKy6HK/68747470733a2f2f64766d6e2e6f72672f66696c65722f63616e6f6e6963616c2f313537353239363331352f3433342f.jpg" alt="68747470733a2f2f64766d6e2e6f72672f66696c65722f63616e6f6e6963616c2f313537353239363331352f3433342f" border="0"></a>

Создайте в корне репозитория файл с именем .env и добавьте в него следующие строки:
```
CLIENT_ID=Ваш client-id
CLIENT_SECRET=Ваш client-secret
```

### Использование

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков 
[dvmn.org](https://dvmn.org).