## Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
cd src
pip install -r requirements.txt
```
## Run EX00
```bash
python fight.py
```

## Run EX01
```bash
python server.py
```
In new terminal
```bash
source venv/bin/activate
python crawl.py post http://example.com
python crawl.py get <returned id>
```
`crawl.py` with *post* return json with field **id**

`crawl.py` with *get* and **id** return task

Or in browser: open `localhost:8888/docs`

## Run EX02
First off all, run redis and then start server
```bash
redis-server --daemonize yes
python server_cached.py 30
```
`server_cached.py` gets argument *time* it's a time that the cache will be stored

In new terminal
```bash
source venv/bin/activate
python crawl.py post http://example.com
python crawl.py get <returned id>
```
Or in browser: open `localhost:8888/docs`
