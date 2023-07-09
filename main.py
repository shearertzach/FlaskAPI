from flask import Flask
import sqlite3
import random


app = Flask(__name__)


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




if __name__ == '__main__':
    app.run()
