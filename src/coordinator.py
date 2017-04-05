from flask import Flask
from console import console_service
from module_service import modules
app = Flask(__name__)
app.register_blueprint(console_service)
app.register_blueprint(modules)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
