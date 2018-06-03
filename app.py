from flask import Flask

app = Flask(__name__)

@app.route('/info')
def get_info():
    return 'Stub for linking to sheets API'


if __name__ == '__main__':
    app.run()
