# Challenge

* Create Docker containers for **frontend** and **backend** applications (details below).
* Deploy this container cluster to AWS.
    * Bring up two **frontend** behind a load balancer.
    * Bring up two **backend** behind a load balancer.
    * **Backend** is only accessible by **frontend** and not by the public internet.
    * All services are configured with and respond with a unique _NAME_.
* Deploy a PostgreSQL instance.
    * DB instance is shared by all **backend**.
    * DB instance is only accessible by **backend** and not by the public internet.
* Deliverables
    * Deployment templates/scripts as text files that can be checked into a version control system.
    * Reviewers should be able to duplicate your setup in a different AWS environment using supplied deployment files.

**_Note:_** Specific AWS components and deployment technologies are left up to you.

# Applications

## frontend

Python3 Flask app to serve UI and handle browser requests from the user.

Configuration is done via environment variables:

* _NAME_ - Name of the app (example: `frontend-1`)
* _VERSION_ - Version of the app (example: `0.0.1`)
* _API_ - URL to **backend** (example: `http://localhost:5001`)

Endpoints:

* `/` - Hello world!
* `/version` - configured _NAME_ and _VERSION_ in JSON
* `/passthrough` - fetch **backend** `/version`

Sample dev environment run command:

```
$ cd frontend
$ source venv/bin/activate
$ FLASK_APP=app.py FLASK_DEBUG=1 VERSION=0.0.1 NAME=frontend API=http://localhost:5001 flask run
```

## backend

Python3 Flask app to handle requests from **frontend** and execute business logic. Requires a PostgreSQL database.

Configuration is done via environment variables:

* _NAME_ - Name of the app (example: `backend-1`)
* _VERSION_ - Version of the app (example `0.0.1`)
* _DBCONNECTIONSTRING_ - PostgreSQL connection string for `psycopg2`
    * Example connection strings:
    * https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
    * https://wiki.postgresql.org/wiki/Using_psycopg2_with_PostgreSQL

Endpoints:

* `/` - Hello world!
* `/version` - configured _NAME_ and _VERSION_ in JSON

Sample dev environment run command:

```
$ cd backend
$ source venv/bin/activate
$ FLASK_APP=app.py FLASK_DEBUG=1 VERSION=0.0.1 NAME=backend DBCONNETIONSTRING='dbname=backend user=sammy password=sammypw host=localhost port=5432' flask run --port=5001
```

