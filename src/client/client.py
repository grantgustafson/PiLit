from flask import Flask
from status_service import status_service
app = Flask(__name__)
app.register_blueprint(status_service)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8123)
