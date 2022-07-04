from flask import Flask

app = Flask(__name__)

@app.route("/") #slash is empty route which returns main page.
def hello_world():
  return "Hello, World!"

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)