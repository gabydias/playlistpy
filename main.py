from flask import Flask, jsonify, request
from db import get_songs

app = Flask(__name__)

@app.route('/')
def songs():

    return get_songs()    

if __name__ == '__main__':
    app.run()
