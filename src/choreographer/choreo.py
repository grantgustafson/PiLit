from flask import Flask
from index import index
from track_data import track_service
app = Flask(__name__)
app.register_blueprint(index)
app.register_blueprint(track_service)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
