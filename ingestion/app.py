from flask import Flask
from burn_analyzer import process_online_data
import json

app = Flask(__name__)


@app.route('/')
def get_info():
    return json.dumps(process_online_data.processOnlineData())


if __name__ == '__main__':
    app.run()
