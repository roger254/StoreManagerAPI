from flask import Flask


def create_app():
    app = Flask(__name__)
    # app.config.from_object(config_filename)

    from app import api_blue
    app.register_blueprint(api_blue, url_prefix='/api/v1')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
