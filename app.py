from flask import Flask

app = Flask(__name__)


@app.route('/')
def mainpage():
    return("Hello")

if __name__ == "__main__": # only run this if the file is executed directly
    app.run(debug=True) #means it'll auto-reload when you save changes and show helpful error pages
