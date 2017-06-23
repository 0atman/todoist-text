import os

import todoist
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello(key):
    api = todoist.TodoistAPI(key)
    api.sync()
    return ' - ' + '\n - '.join([i['content'] for i in api.items.all() if i['due_date_utc']])
