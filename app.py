from flask import Flask
app = application = Flask(__name__)

@app.route("/hi")
def hello():
    return "Hello World V2!"

if __name__ == "__main__":
    print "Minial app V2 for Poc Booting"
    app.run()