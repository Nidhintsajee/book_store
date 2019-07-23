from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.static_folder = 'templates'
mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    userDetails=[]
    userBook=[]
    userCustomer=[]
    userReservation=[]
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM author")
    if resultValue > 0:
        userDetails = cur.fetchall()

    resultValueB = cur.execute("SELECT * FROM books")
    if resultValueB > 0:
        userBook = cur.fetchall() 
    resultValueC = cur.execute("SELECT * FROM customers")
    if resultValueC > 0:
        userCustomer = cur.fetchall()

    resultValueR = cur.execute("SELECT * FROM reservation")
    if resultValueR > 0:
        userReservation = cur.fetchall()        
    return render_template('index.html', userDetails=userDetails, userBook=userBook,userCustomer=userCustomer,userReservation=userReservation)

@app.route('/authors')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM author")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('authors.html',userDetails=userDetails)


# add_authors

@app.route('/add_authors')
def add_authors():
    userDetails = []
    return render_template('add_authors.html',userDetails=userDetails)
    

@app.route('/author_delete/<int:aid>', methods=['GET'])
def author_delete(aid):
    cur = mysql.connection.cursor()
    resultValue1 = cur.execute("DELETE FROM books where B_A_ID="+ str(aid))

    resultValue = cur.execute("DELETE FROM author where A_ID="+ str(aid))
    mysql.connection.commit()
    return redirect('/')

@app.route('/author_edit/<int:aid>', methods=['GET'])
def author_edit(aid):
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM author where A_ID="+ str(aid))
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('add_authors.html',userDetails=userDetails)
    else:
        return redirect('/')

@app.route('/insert_update_author/', defaults={'aid': None}, methods=['GET','POST'])
@app.route('/insert_update_author/<int:aid>', methods=['GET','POST'])
def insert_update_author(aid = ''):
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        A_FNAME = userDetails['A_FNAME']
        A_LNAME = userDetails['A_LNAME']
        if aid:
            cur = mysql.connection.cursor()
            cur.execute("UPDATE author set A_FNAME=(%s), A_LNAME=(%s) where A_ID=(%s)",(A_FNAME, A_LNAME, aid))
            mysql.connection.commit()
            cur.close()
            return redirect('/')
        else:    
            
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO author(A_FNAME, A_LNAME) VALUES(%s, %s)",(A_FNAME, A_LNAME))
            mysql.connection.commit()
            cur.close()
            return redirect('/')
    else:
        return redirect('/')


# book_edit  

@app.route('/add_book')
def add_book():
    userDetails = []
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM author")
    if resultValue > 0:
        authorList = cur.fetchall()
    return render_template('add_book.html',userDetails=userDetails, authorList=authorList)
    

@app.route('/book_delete/<int:bid>', methods=['GET'])
def book_delete(bid):
    cur = mysql.connection.cursor()
    resultValue1 = cur.execute("DELETE FROM books where B_ID="+ str(bid))

    mysql.connection.commit()
    return redirect('/')

@app.route('/book_edit/<int:bid>', methods=['GET'])
def book_edit(bid):
    cur = mysql.connection.cursor()
    authorListe = cur.execute("SELECT * FROM author")
    if authorListe > 0:
        authorList = cur.fetchall()
    resultValue = cur.execute("SELECT * FROM books where B_ID="+ str(bid))
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('add_book.html',userDetails=userDetails, authorList=authorList)
    else:
        return redirect('/')          

@app.route('/insert_update_book/', defaults={'bid': None}, methods=['GET','POST'])
@app.route('/insert_update_book/<int:bid>', methods=['GET','POST'])
def insert_update_book(bid = ''):
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        B_TITLE = userDetails['B_TITLE']
        B_A_ID = userDetails['B_A_ID']
        B_PUBLISHER = userDetails['B_PUBLISHER']
        B_PUB_DATE = userDetails['B_PUB_DATE']
        B_SUBJECT = userDetails['B_SUBJECT']
        B_UNIT_PRICE = userDetails['B_UNIT_PRICE']
        B_STOCK = userDetails['B_STOCK']
        if bid:
            cur = mysql.connection.cursor()
            cur.execute("UPDATE books set B_TITLE=(%s), B_A_ID=(%s),B_PUBLISHER=(%s), B_PUB_DATE=(%s),B_SUBJECT=(%s), B_UNIT_PRICE=(%s), B_STOCK=(%s) where B_ID=(%s)",(B_TITLE, B_A_ID,B_PUBLISHER, B_PUB_DATE,B_SUBJECT, B_UNIT_PRICE, B_STOCK, bid))
            mysql.connection.commit()
            cur.close()
            return redirect('/')
        else:    
            
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO books(B_TITLE, B_A_ID,B_PUBLISHER, B_PUB_DATE,B_SUBJECT, B_UNIT_PRICE, B_STOCK) VALUES(%s, %s,%s, %s,%s, %s,%s)",(B_TITLE, B_A_ID,B_PUBLISHER, B_PUB_DATE,B_SUBJECT, B_UNIT_PRICE, B_STOCK))
            mysql.connection.commit()
            cur.close()
            return redirect('/')
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
