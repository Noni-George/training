import os
from flask import Flask, render_template
from google.cloud import datastore

app = Flask(__name__)

ds_client = datastore.Client()
KEY_TYPE = 'Task'

def query():
    return ds_client.query(kind=KEY_TYPE).fetch()

@app.route('/')
def hello():
    l = list(query())
    if not l:
        print("No result is returned")
        created= "Wait a minute"
        description = "So what is this ?"
        done = "I thought whe had to implement a data base search box"
    else:  
        d = dict(l[0])
        created=d['created']
        description = d['description']
        done = d['done']

    return render_template('index.html',
        created=created,
        description=description,
        done=done
        )

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
