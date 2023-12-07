from flask import Flask
from flask_cors import CORS
from controllers import Controller


app = Flask(__name__)
CORS(app)


@app.route("/api/twit", methods=['POST'])
def twit():
    controller = Controller()
    return controller.get_nitter()



if __name__ == "__main__":
    app.run()