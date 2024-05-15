from flask import Flask
import requests
import random

app = Flask(__name__)

# handle requests
@app.route('/', methods=['GET'])
def generateData():
    # Generate a random number
    data = random.randint(1, 1000)
    return str(data)

# Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5601)