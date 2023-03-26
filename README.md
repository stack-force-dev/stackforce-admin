## :zap: Simple starter admin template powered by Django

### :dart: Working with: PostgreSQL
* For work with another database change `DATABASE_ENGINE` in `config/settings.py`
### :dart: Environment
    SECRET_KEY=<your secret key>
    DEBUG=<0 or 1>
    ALLOWED_HOSTS=<hosts via space>

    DATABASE_NAME=<your db name>
    DATABASE_USER=<your db user>
    DATABASE_PASS=<your db pass>
    DATABASE_HOST=<your db host>
    DATABASE_PORT=<your db port>
### :dart: Build
    docker build -t admin:latest .
### :dart: Run
    docker run -d -p 8000:8000 --name admin --volume .:/app --env-file .env admin:latest 
### :dart: Migrate
    docker exec -it admin python manage.py migrate
### :dart: Create superuser
    docker exec -it admin python manage.py createsuperuser
### :dart: Let's go!
    http://localhost:8000/admin/
