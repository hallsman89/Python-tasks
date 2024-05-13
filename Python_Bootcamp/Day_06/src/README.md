## Create and activate virtual enviroment
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m pip install --editable ./
```
## Generate files from proto file
```
cd proto
python -m grpc_tools.protoc --proto_path=. ./galaxy.proto --python_out=. --grpc_python_out=. --pyi_out=.
```
## Run EX00
```
python reporting_server.py
```
`!!!Don't stop the server till the completion of the last EX!!!`.
In case of the mistake like "No module named 'galaxy_pb2'"
Use the following command:
```
export PYTHONPATH=/full/path/to/Python_Bootcamp.Day_06-1/src/proto
```

In new terminal
```
python3 reporting_client.py 1111.1 2222.2 -3333 4444
```
## Run EX01

Run script several times
```
python3 reporting_client_v2.py 1111.1 2222.2 -3333 4444
```
## Run EX02

Create `.env` file with the following content for connect to Postgresql:
```
DB_USER=your_user_name
DB_PASS=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=database_name
```
Create database use script, but before start postgresSQL
```
sudo service postgresql start
python3 create_db.py
```
Use migration for create tables
```
alembic upgrade fec5f6ca3ad1
```
To enter the interactive command line of PostgreSQL and to see all existing tables
```
psql -U username -d database_name
\dt
```

Run script several times
```
python3 reporting_client_v3.py scan 1111.1 2222.2 -3333 4444
python3 reporting_client_v3.py list_traitors
```
