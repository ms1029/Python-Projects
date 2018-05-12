from flask import Flask, flash, render_template, redirect, request
from bson.objectid import ObjectId
from datetime import datetime
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client.todo

@app.route('/note', methods=['GET'])
def get_notes():
  notes = []
  for note in db.notes.find():
    notes.append(note)
  return render_template('notes.html', notes=notes)

@app.route('/note/new', methods=['GET'])
@app.route('/note/edit/<string:note_id>', methods=['GET'])
def edit_note(note_id=None):
  note = {
    'title': '',
    'text': ''
  }
  if note_id:
    note = db.notes.find_one({'_id': ObjectId(note_id)})
  return render_template('operations.html', note=note)

@app.route('/note/save/', methods=['POST'])
@app.route('/note/save/<string:note_id>', methods=['POST'])
def save_note(note_id=None):
  if note_id:
    note = db.notes.find_one({'_id': ObjectId(note_id)})
    note['title'] = request.form['title']
    note['text'] = request.form['text']
    db.notes.update_one({'_id': ObjectId(note_id)}, {'$set': note})
  else:
    note = {
      'title': request.form['title'],
      'text': request.form['text'],
      'createdDate': datetime.now()
    }
    db.notes.insert_one(note)
  return redirect('/note')


@app.route('/note/delete/<string:note_id>', methods=['POST'])
def delete_note(note_id):
  db.notes.delete_one({'_id': ObjectId(note_id)})
  return redirect('/note')

if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0')
