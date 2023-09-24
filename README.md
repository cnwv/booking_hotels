
[![pytest](https://img.shields.io/badge/pytest-passed-brightgreen?logo=pytest)](https://docs.pytest.org/en/7.4.x/)
[![celery](https://img.shields.io/badge/5.3.1-Celery-blue?logo=celery)](https://docs.celeryq.dev/en/stable/index.html)
[![fastapi](https://img.shields.io/badge/0.100.0-fastapi-blue?logo=fastapi)](https://fastapi.tiangolo.com/)
[![postgres](https://img.shields.io/badge/16_alpine-PostgreSQL-blue?logo=postgresql)](https://www.postgresql.org/docs/current/index.html)
[![celery](https://img.shields.io/badge/1.2.0-Flower-blue)](https://flower.readthedocs.io/en/latest/)
[![redis](https://img.shields.io/badge/7-Redis-blue?logo=redis)](https://redis.io/)
[![grafana](https://img.shields.io/badge/1.11.2-Alembic-blue)](https://alembic.sqlalchemy.org/en/latest/)
[![grafana](https://img.shields.io/badge/2.1.1-Pydantic-blue?logo=pydantic)](https://docs.pydantic.dev/latest/)
[![grafana](https://img.shields.io/badge/1.31.0-Sentry-blue?logo=sentry)](https://sentry.io/)
[![grafana](https://img.shields.io/badge/21.2.0-Gunicorn-blue?logo=gunicorn)](https://gunicorn.org/)
[![grafana](https://img.shields.io/badge/2.0.19-SQLAlchemy-blue?logo=SQLAlchemy)](https://www.sqlalchemy.org/)
[![grafana](https://img.shields.io/badge/0.17.1-prometheus-blue?logo=prometheus)](https://prometheus.io/)
[![grafana](https://img.shields.io/badge/9.4.7-Grafana-blue?logo=grafana)](https://grafana.com/)

# Booking app
This is a backend service for hotel booking based on Fastapi like booking.com
The application implements full interaction with the following entities:
- Hotels
- Rooms
- Reservations
- Users


## How to use it

1. Copy repo on local machine
```git clone https://github.com/cnwv/booking_hotels```
2. Create .env-prod file
3. Run
```docker-compose up -d```




### Celery & Flower
The following command is used to start Celery
```
celery --app=app.tasks.celery:celery worker -l INFO -P solo
```
Note that `-P solo` is only used on Windows, as Celery has problems running on Windows.  
The command used to start Flower is
```
celery --app=app.tasks.celery:celery flower
``` 

They are already included in the docker container startup settings

### Dockerfile
If you changed something inside the Dockerfile
Run the command ```docker build .```

### Sentry
To configure logging, register on [sentry](sentry.io). Select the framework of your project and copy the sentry_dns you are prompted for and enter it in the .env-non-dev file.

### Grafana / Prometheus
[Setup guide](https://grafana.com//tutorials/grafana-fundamentals/)

1. To enter the cabinet you need to specify ```username: admin, password: admin```
2. Then override the password
3. To get the charts working you must in grafana-dashboard specify your uid in the following piece of code:
```"datasource":{"type": "prometheus","uid": "Your UID"} ```
4. It can be taken from the json schema of the preset dashboards
(in settings add data source -> prometheus -> "choose name"). Then in Dashboards -> import -> Paste the contents of grafana-dashboard.json and choose some random uuid(and name for the dashboard)
5. If you are not interested in metrics / logging you can disable it by commenting out the sentry and instumentator lines in the app/main.py file and docker-compose

### Documentation

- [x] Swagger UI <localhost:8000/docs>
- [x] ReDoc <localhost:8000/redoc>


