# Healthshare

## Run in Flask

Requirements: Python 3.X, pip (flask, mysql-connector, flask_cors, requests)
```
python app.py
``` 
Open localhost:5000

## Run in Docker (under development)

```
docker build -t healthshare:latest .
```
```
docker run -p 5000:5000 healthshare
```
Open localhost:5000