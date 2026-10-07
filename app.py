from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

mongo_uri = os.getenv("Mongo_DB")
client = MongoClient(mongo_uri)

db = client.test
collection = db["Flask & MongoDB"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        from_data = dict(request.form)
        collection.insert_one(from_data)
        return "Form submitted successfully!"
    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)
