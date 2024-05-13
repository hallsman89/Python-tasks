from config import DB_NAME, DB_PASS, DB_USER, DB_HOST, DB_PORT

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT, connection, cursor


conn: connection = psycopg2.connect(
    dbname="postgres", user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT
)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
curs: cursor = conn.cursor()
curs.execute(f"CREATE DATABASE {DB_NAME}")
curs.close()
conn.close()
