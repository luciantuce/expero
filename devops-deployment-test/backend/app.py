import datetime
import os
import time

from flask import Flask, jsonify
import psycopg2


app = Flask(__name__)

app.config.update(
    NAME=os.getenv('NAME'),
    VERSION=os.getenv('VERSION'),
    DBCONNETIONSTRING=os.getenv('DBCONNETIONSTRING'),
)


def add_audit(route):
    conn = cursor = None
    try:
        conn = psycopg2.connect(app.config['DBCONNETIONSTRING'])
        conn.autocommit = True

        cursor = conn.cursor()

        cursor.execute('''
CREATE TABLE IF NOT EXISTS audit (
    audit_id serial primary key,
    app_name text NOT NULL,
    route text NOT NULL,
    date_added timestamp NOT NULL
);
        ''')

        cursor.execute('''
INSERT INTO audit (app_name, route, date_added) VALUES (%s, %s, %s);
        ''', (
            app.config['NAME'],
            route,
            datetime.datetime.fromtimestamp(time.time()),
        ))

    except:
        raise
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


@app.route('/')
def hello():
    add_audit('/')
    return 'Hello Backend!'


@app.route('/version')
def version():
    add_audit('/version')
    return jsonify({
        'name': app.config['NAME'],
        'version': app.config['VERSION'],
    })
