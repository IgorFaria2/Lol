from flask import Flask
from blueprints.main import main_blueprints

app = Flask(__name__)
app.config['DEBUG'] = True

app.register_blueprint(main_blueprints)

if __name__ == "__main__":
    app.run()