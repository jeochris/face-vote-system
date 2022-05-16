# face-vote-system

## Requirements
```
pip install django
```
1. Insert two Front facial images to compare in each folder: `static/front/comp{i}/`
2. Left and Right as well
3. Let appropriate number on `FRONT_IMG LEFT_IMG RIGHT_IMG` in `vote_app/views.py` (number of pairs to compare)
4. Use your own `secrets.json` (secret key)

## How to run
1. Migrate only when you first start this program
```
python manage.py makemigrations
python manage.py migrate
```
2. Run server
```
python manage.py runserver
```
3. Go to `127.0.0.1:8000/`
4. Start voting each pair (1~5) : higher score if you think similar
5. You can continue voting where you stopped even if you reopened the server, but please go to `127.0.0.1:8000/` when you continue
6. Vote result saved in db.sqlite3.vote_app_personalanswer
7. Convert it to csv file if needed

## Caution
1. You cannot modify your voting score after you vote
2. If you want to delete all your voting score, turn off server and delete files/folders below
```
vote_app/migrations/__pycache__
vote_app/migrations/0001_initial.py
db.sqlite3
```

## Demo
<img src = "https://user-images.githubusercontent.com/72757567/168466699-001f3554-c9a8-4fdd-a1dc-5f1829cfa095.png" width="70%" height="70%">

![KakaoTalk_20220515_174452909](https://user-images.githubusercontent.com/72757567/168467318-344826ba-183a-4c11-8c94-e54499cfa731.png)

