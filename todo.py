import os

import todoist
from flask import Flask

api = todoist.TodoistAPI(os.environ['TODOIST_KEY'])
api.sync()
app = Flask(__name__)


@app.route("/")
def hello():
    return ' - ' + '\n - '.join([i['content'] for i in api.items.all() if i['due_date_utc']])
