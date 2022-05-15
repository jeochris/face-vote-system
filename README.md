# face-vote-system

## Requirements
```
pip install django
```
1. Insert two Front facial images to compare in each folder: `static/front/comp{i}/`
2. Left and Right as well
3. Let appropriate number on `FRONT_IMG LEFT_IMG RIGHT_IMG` in `vote_app/views.py` (number of pairs to compare)

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
![image](https://user-images.githubusercontent.com/72757567/168465987-0efe1db8-2870-415d-a6a8-1673b01f23cd.png)
