from flask import Flask
app = application = Flask(__name__)

@app.route("/hi")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    print "Minial app for Poc Booting"
    app.run()