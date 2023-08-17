#this line imports fumctionality
from flask import Flask, render_template, request, redirect
import sqlite3

#initializing 
app = Flask(__name__) #we will always use this function for Flask

"""
decorators add aditional features to our functions 
"""
items = []

@app.route('/')
def checklist():
              return render_template('checklist.html', items=items)



@app.route('/add', methods=['POST']) #if the user is at the add screen
def add():
              item = request.form['item']
              add_item(item)
              return redirect('/')

def add_item(): #the view function
              item = request.form['item'] # store it 'item'
              item.append(item) #Append the new item to the list
              #(not stored in a database)
              return redirect('/')
              
#now, we're creating the Update functionality/endpoint
@app.route('/edit/<int:item_id>', methods=['GET', 'POST']) #This is the READ part of CRUD (speccifically the GET method)
def edit_item(item_id):
              item = items[item_id-1] #Retrieve the item based on its index
              #just getting info
              
              if request.method == 'POST': #IF WE DO SEND INFORMATION
                            new_item = request.form['item'] #we will have a new_item that we get from the request.form['items']
                            items[item_id - 1] = new_item #adding new_item to our items list
                            return redirect('/')
              return render_template('edit.html',item=item, item_id=item_id) #this is the UPDATE part of our CRUD framework


#Delete (C.R.U.D)

@app.route('/delete/<int:item_id>')
def delete_item(item_id): #define the deleted item
              del items[item_id - 1]
              return redirect('/') #send the user back to the home page



"""
if __name__ == '__main__':
              app.run(debug=True, port=8000)
"""



              
"""
below is an example of a simple route function

@app.route('/')
def hello_world():
              return 'Hello Tutorialspoint' # this is what will be printed on the webpage when the code is run

if __name__ == '__main__':
              app.run() #this function runs the route
"""