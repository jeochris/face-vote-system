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
1. Migrate and run server
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
2. Go to `127.0.0.1:8000/`
3. Starting from front, start voting each pair (1~5) : higher score if you think similar
4. Vote result saved in db.sqlite3.vote_app_personalanswer
5. Convert it to csv file if needed

## Caution
1. Please vote with order front -> left -> right
2. Once voting started, I recommend to not stop voting
3. If you want to restart voting anyway, turn off server and delete files/folders below
```
vote_app/migrations/__pycache__
vote_app/migrations/0001_initial.py
db.sqlite3
```

## Demo
<img src = "https://user-images.githubusercontent.com/72757567/168466699-001f3554-c9a8-4fdd-a1dc-5f1829cfa095.png" width="70%" height="70%">

![KakaoTalk_20220515_174452909](https://user-images.githubusercontent.com/72757567/168467318-344826ba-183a-4c11-8c94-e54499cfa731.png)

