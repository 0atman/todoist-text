import todoist
from flask import Flask

app = Flask(__name__)


@app.route("/<key>")
def hello(key):
    api = todoist.TodoistAPI(key)
    api.sync()
    return '' + '\n'.join([i['content'] for i in api.items.all() if (i['due_date_utc'] and not i['checked']) or 1279019 in i['labels']])
