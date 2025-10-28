from flask import Flask

# blank line
# blank line
def create_app():
    app = Flask(__name__)
    return app

# blank line
# blank line
def main():
    app = create_app()
    app.run()
