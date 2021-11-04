# BackEndTest
This is a Django-Celery-Redis-Dockerized project, which will fetch update PostgresSQL DB hourly with BTC USD exchange rates. An API end point is provided with GET and POST methods.
GET method will return the current BTC USD exchange rate.
POST method will return the current Ask & Bid price of BTC/USD.

# Dockerfile
Configured to copy code, install the python packages required for the project.

# docker-compose.yml
Celery, Postgresql, Redis, Django app are configured and containerized.

# API Endpoints
To generate Token
http://hostname:8000/v1/quotes


For getting the BTC/USD exchange details
http://hostname:8000/v1/quotes

The APIs are secured using Token Authentication, to access the API's, user has to generate Token.
**STEPS TO GENERATE TOKEN:**
1. Using httpie package: http POST http://127.0.0.1:8000/get_token/ username="suser" password="suser"
2. Once the token is generated use the same to access the API's.
3. Sample response: {"token": "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"}

**Note: Postman also can be used for the same.**


# Running the Project
1. Copy the project or GIT clone.
2. Change directory to Project and run "sudo docker-compose build" command.
3. Once the build is successful, run "sudo docker-compose up" command.
4. Please check if all the services are up: app, celery, db, redis
    Docker Compose Up logs:
      celery_1  |                 
      celery_1  | 
      celery_1  | [tasks]
      celery_1  |   . write_btc_usd_quote
      celery_1  | 
      celery_1  | [2021-11-04 07:44:20,339: INFO/MainProcess] Connected to redis://redis:6379//
      celery_1  | [2021-11-04 07:44:20,468: INFO/MainProcess] mingle: searching for neighbors
      app_1     | Operations to perform:
      app_1     |   Apply all migrations: admin, auth, authtoken, contenttypes, quotesapp, sessions
      app_1     | Running migrations:
      app_1     |   No migrations to apply.
      app_1     | >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>:  app
      celery_1  | [2021-11-04 07:44:21,766: INFO/MainProcess] mingle: all alone
      celery_1  | [2021-11-04 07:44:21,842: WARNING/MainProcess] /usr/local/lib/python3.8/site-packages/celery/fixups/django.py:202: UserWarning: Using settings.DEBUG leads to a memory
      celery_1  |             leak, never use this setting in production environments!
      celery_1  |   warnings.warn('''Using settings.DEBUG leads to a memory
      celery_1  | [2021-11-04 07:44:21,844: INFO/MainProcess] celery@716fc707dd1e ready.
      app_1     | >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>:  app
      app_1     | Watching for file changes with StatReloader
      app_1     | Performing system checks...
      app_1     | 
      app_1     | System check identified no issues (0 silenced).
      app_1     | November 04, 2021 - 07:44:23
      app_1     | Django version 3.2.9, using settings 'core.settings'
      app_1     | Starting development server at http://0.0.0.0:8000/
      app_1     | Quit the server with CONTROL-C.
5. Celery is configured to write the exchage rate data to DB every hour.
6. DB data sample data:
      1 "62424.86000000"	"2021-11-04 06:21:02"
      2	"62443.02000000"	"2021-11-04 06:22:00"
      3	"62469.17000000"	"2021-11-04 06:23:00"
      4	"62486.34000000"	"2021-11-04 06:24:01"
      5	"62494.05000000"	"2021-11-04 06:25:00"
      6	"62525.75000000"	"2021-11-04 06:26:01"


# Using the API's
1. GET method
    Request: http GET http://127.0.0.1:8000/v1/quotes "Authorization: Token <generated token>"
    Response: {"btcusd_exchange_rate": "61976.26000000"}

2. POST method
    Request: http POST http://127.0.0.1:8000/v1/quotes "Authorization: Token <generated token>"
    Response: {"btcusd_ask_price": "61814.01000000", "btcusd_bid_price": "61814.00000000"}

    
  
  
  
  
  
