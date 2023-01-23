# Mail with Celery

## Run 

At first run Redis (for example on Docker)
```shell
docker run -d -p 6379:6379 redis
```

Set Environment Variables from env.bat
```shell
call env.bat 
echo %VAR_NAME% (check)
```

Start app
```shell
python manage.py runserver
```

Start worker
```shell
celery -A send_email worker -l info -P gevent (for Windows)
```

Start beat
```shell
celery -A send_email beat -l info
```

Start Flower
```shell
celery -A send_email flower  --address=localhost --port=5555
```
