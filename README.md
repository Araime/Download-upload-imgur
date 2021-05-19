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
и создать приложение. В поле `Authorization callback URL` напишите `http://localhost`.  

<a href="https://ibb.co/b6MbmrL"><img src="https://i.ibb.co/PrvDj54/image.png" alt="image" border="0"></a>

Вы получите client-id и client-secret.  

<a href="https://ibb.co/SxYVbwY"><img src="https://i.ibb.co/9vKy6HK/68747470733a2f2f64766d6e2e6f72672f66696c65722f63616e6f6e6963616c2f313537353239363331352f3433342f.jpg" alt="68747470733a2f2f64766d6e2e6f72672f66696c65722f63616e6f6e6963616c2f313537353239363331352f3433342f" border="0"></a>

Создайте в корне репозитория файл с именем .env и добавьте в него следующие строки:
```
CLIENT_ID=Ваш client-id
CLIENT_SECRET=Ваш client-secret
```

### Использование

#### Spacex API

Чтобы скачать фотографии с запуска Spacex, необходимо запустить скрипт 
fetch_spacex.py и в качестве аргумента передать ссылку на запуск. Скрипт 
fetch_spacex.py проверяет, есть ли в репозитории папка images, если такой 
папки нет, создаёт её. Все фотографии сохраняются в папку images.  
Не у всех запусков есть фотографии, по этому нужно будет попробовать несколько
запросов.  
Пример с фотографиями:

```
python fetch_spacex.py https://api.spacexdata.com/v3/launches/13
```

Подробнее об [Spacex API](https://documenter.getpostman.com/view/2025350/RWaEzAiG#bc65ba60-decf-4289-bb04-4ca9df01b9c1).

#### Hubble API

Скрипт fetch_hubble.py настроен на скачивание коллекций изображений. Красивые 
изображения Hubble хранятся в коллекциях. Вот некоторые из них: “holiday_cards”, 
“wallpaper”, “spacecraft”, “news”, “printshop”, “stsci_gallery”. При запуске 
скрипта необходимо передать ссылку коллекцию в качестве аргумента. Скрипт 
fetch_hubble.py проверяет, есть ли в репозитории папка images, если такой 
папки нет, создаёт её. Все изображения сохраняются в папку images.  
Пример скачивания коллекции:

```
python fetch_hubble.py https://hubblesite.org/api/v3/images/stsci_gallery
```

Подробнее об [Hubble API](http://hubblesite.org/api/documentation).

#### Обработка (по желанию)

С помощью скрипта image_processing.py можно все скачанные изображения в формате
.jpg и .png, в папке images пересохранить в формате JPEG и сжать, сохраняя 
пропорции. После сжатия самая большая сторона изображения не будет превышать 
размер 1080 пикселей, а все оставшиеся файлы .png будут удалены.  
Пример использования:

```
python image_processing.py
```

#### Загрузка на Imgur

Для загрузки всех изображений в папке images, необходимо запустить скрипт
upload.py. После запуска программа запросит пин-код и даст ссылку для его
получения. Пройдите по ней и скопируйте пин-код.  

<a href="https://imgbb.com/"><img src="https://i.ibb.co/kQN5R5p/2.png" alt="2" border="0"></a>

Вставьте полученый пин-код.  

<a href="https://ibb.co/4FPt0xv"><img src="https://i.ibb.co/grz9cCq/image.png" alt="image" border="0"></a>

Скрипт начнёт загрузку всех изображений в папке images.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков 
[dvmn.org](https://dvmn.org).