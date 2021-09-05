from flask import Flask, render_template, request,Response, abort, redirect
import mysql.connector


dns = {
    'user': 'root',
    'host': 'localhost', # 各自設定
    'password': 'hibiki2029', # 各自設定
    'database': 'userdata' # 各自設定
}
#db = MySQL(**dns)
db = mysql.connector.connect(**dns)

# 接続できているか確認
if db.is_connected():
    print("データベースへの接続が成功しました。")
else:
    print("データベースへの接続が失敗しました。")
    exit(1)
#######

app = Flask(__name__)

Name = ""

@app.route('/', methods=["GET", "POST"])
def login():
    if(request.method == "POST"):
        cur = db.cursor(buffered=True)
        cur.execute("SELECT userName, PassWord FROM users")
        for (name, pwd) in cur:
            print(name, pwd)
            if (request.form["username"] == name and request.form["password"] == pwd):
                global Name
                Name = request.form["username"]
                cur.close()
                return redirect("/home/")
    else:
        return render_template("index.html")

@app.route('/home/')
def home():
    return render_template("main/dashbord.html", name=Name)

@app.route('/subjects/butsuri')
def butsuri():
    return render_template('main/subjects/butsuri.html')

@app.route('/subjects/denjiki')
def denjiki():
    return render_template('main/subjects/denjiki.html')

@app.route('/subjects/denkikairo')
def denkikairo():
    return render_template('main/subjects/denkikairo.html')

@app.route('/subjects/densikairo')
def densikairo():
    return render_template('main/subjects/densikairo.html')

@app.route('/subjects/muki')
def muki():
    return render_template('main/subjects/muki.html')

@app.route('/subjects/yuuki')
def yuuki():
    return render_template('main/subjects/yuuki.html')

if __name__ == '__main__':
    app.run()
