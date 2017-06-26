import arrow
import todoist
from flask import Flask

app = Flask(__name__)


@app.route("/<key>")
def hello(key):
    api = todoist.TodoistAPI(key)
    api.sync()
    items = []

    for i in api.items.all():
        if 1279019 in i['labels']:
            items.append(i['content'])
            pass
        if i['due_date_utc']:
            if arrow.get(i['due_date_utc'], "DD MMM YYYY") < arrow.utcnow():
                items.append(i['content'])

    return '' + '\n'.join(items)
