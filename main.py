from flask import Flask
from lib.response import returnResponse
import sqlite3
import random
import json


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
  db = sqlite3.connect('database.db')
  cursor = db.cursor()

  for _ in range(1, 10):
      username = f"user{random.randint(1000000, 9999999)}"
      password = 'testpword'

      cursor.execute(
          "INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
      print(f"Adding {username} to insert statement.")

  print(f"Committing users to database.")

  db.commit()

  return '<h1>Added users to database</h1>'

@app.route('/responsetesting')
def responseTesting():
  data = {
      'message': 'Hello, people!',
      'status': 'success'
  }
  json_data = json.dumps(data)  # Convert the data to JSON string

  return returnResponse("OK", data=json_data)




if __name__ == '__main__':
    app.run()
