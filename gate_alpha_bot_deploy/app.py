from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Gate Alpha Bot!"

if __name__ == "__main__":
    app.run()