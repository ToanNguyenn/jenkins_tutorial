from flask import Flask
import time
app = Flask(__name__)
@app.route('/')

def hello_world():
    return f"Hello Jenkins at {time.time()}"

if __name__ == '__main__':
    print("App run!!")
    app.run(debug=True)
