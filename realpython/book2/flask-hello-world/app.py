# ---- Flask Hello World ---- #

# import the Flask from the flask package
from flask import Flask

# create the application object
app = Flask(__name__)

# use the decorator pattern to link the view function to a url
@app.route('/')
@app.route('/hello')

# defin the view using a function, which returns a string
def hello_world():
    return 'Hello, World!'

# start the developement server using the run() method
if __name__ == '__main__':
    app.run()