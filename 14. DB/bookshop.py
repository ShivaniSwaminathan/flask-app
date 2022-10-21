from flask import *  
import random
import sqlite3  
  
app = Flask(__name__)  
 
@app.route("/")  
def index():  
    return render_template("index.html");  
 
@app.route("/sellersign")  
def add():  
    return render_template("ssignup.html")  
 
@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            passw = request.form["pas"]  
            ids=random.randint(1,1000)
            with sqlite3.connect("Sellers.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Sellers (sid,Sname,Password) values (?,?,?)",(ids,name,passw))  
                con.commit()  
                msg = "SignedUp Successfully!"  
        except:  
            con.rollback()  
            msg = "We can not add the Seller to the list"  
        finally:  
            return render_template("success.html",msg = msg)  
            con.close()  
@app.route("/slogin")
def slogin():
        return render_template("slogin.html")  
@app.route("/validatedetails",methods = ["POST","GET"])
def validate():
    msg = "msg"  
    if request.method == "POST":    
            ids=request.form['ids']
            passw = request.form["pas"] 
            with sqlite3.connect("Sellers.db") as con:  
                cur = con.cursor() 
                statement = f"SELECT Sname from Sellers WHERE Sid='{ids}' AND Password = '{passw}'"
                cur.execute(statement)  
                if  not cur.fetchone():  
                    msg = "LogIn Failed!"  
                else:
                    return  render_template("Selleruporshow.html",msg = msg)

@app.route("/upload",methods = ["POST","GET"])
def upload():
        return render_template("upload.html")
@app.route("/savebookdetails",methods = ["POST","GET"])  
def bookdetails():
    if request.method == "POST":  
        try:  
            bname = request.form["name"]  
            price = request.form["price"] 
            aname = request.form["author"] 
            lang = request.form["lang"] 
            cat = request.form["cate"] 
            with sqlite3.connect("Comics.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Comics (bname,price,authorname,language,category) values (?,?,?,?,?)",(bname,price,aname,lang,cat))  
                con.commit()  
                msg = "Book Added Successfully!"  
        except:  
            con.rollback()  
            msg = "We can not add the Book to the list"  
        finally:  
            return render_template("upsuccess.html",msg = msg)  
            con.close()  

@app.route("/view")  
def view():  
    con = sqlite3.connect("Comics.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Comics")  
    rows = cur.fetchall()  
    return render_template("view.html",rows = rows)  
 
 

  
if __name__ == "__main__":  
    app.run(debug = True,port=3000)  