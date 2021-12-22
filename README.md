# FastAPI

```
$ cd project
$ python3.9 -m venv env
$ source env/bin/activate

(env)$ pip install fastapi==0.65.3
(env)$ pip install uvicorn==0.14.0

(env)$ uvicorn app.main:app --reload


(env)$ export ENVIRONMENT=prod
(env)$ export TESTING=1
```

- [Resource PING](http://127.0.0.1:8000/ping)
- [Docs](http://localhost:8000/docs)
- [OpenAPI](http://localhost:8000/openapi.json)

