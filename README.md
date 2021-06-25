### requirments

1. flask
```sh
pip install Flask
```
2. flask_sqlalchemy
```sh
pip install Flask-SQLAlchemy
```
3. lxml
```sh
pip install lxml
```

### Start project
1. Clone the repo
```sh
git clone https://github.com/LorenzoCA1/Coding-Challenge.git
```

2. database(for fresh database (OPTIONAL))
```sh
Python
>>>From app import db 
>>>db.create_all()
>>exit()
```

2. database check(for fresh database (OPTIONAL))
```sh
sqlite3 data.db
>>>.table   (check if cases is a table)
>>>.exit
```

### Usage
You must go to project repo in command line and run:
```sh
flask run
```
Enter link in browser:
```sh
http://127.0.0.1:5000/
```
Upload XML file:
```sh
http://127.0.0.1:5000/
```
Check data:
```sh
http://127.0.0.1:5000/data
```
