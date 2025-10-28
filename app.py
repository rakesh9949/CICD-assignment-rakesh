from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/api/message')
    def get_message():
        return {'message': 'Hello from Flask!'}

    return app


def main():
    app = create_app()
    app.run()


if __name__ == '__main__':
    main()
