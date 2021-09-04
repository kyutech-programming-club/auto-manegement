from flask import Flask, render_template, request,Response, abort, redirect
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from collections import defaultdict

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = "secret"

class User(UserMixin):
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password

# ログイン用ユーザー作成
users = {
    1: User(1, "三木彪流", "mikitakeru"),
    2: User(2, "user2", "pass")
}

# ユーザーチェックに使用する辞書作成
nested_dict = lambda: defaultdict(nested_dict)
user_check = nested_dict()
for i in users.values():
    user_check[i.name]["password"] = i.password
    user_check[i.name]["id"] = i.id

@login_manager.user_loader
def load_user(user_id):
    return users.get(int(user_id))

#######################################################

@app.route('/', methods=["GET", "POST"])
def login():
    if(request.method == "POST"):
        # ユーザーチェック
        if(request.form["username"] in user_check and request.form["password"] == user_check[request.form["username"]]["password"]):
            # ユーザーが存在した場合はログイン
            login_user(users.get(user_check[request.form["username"]]["id"]))
            print(users.get(user_check[request.form["username"]]["id"]))
            return redirect("/home/")
        else:
            return abort(401)
    else:
        return render_template("index.html")

@app.route('/home/')
@login_required
def home():
    return render_template("main/dashbord.html")

@app.route('/subjects')
def buturi():
    return render_template('main/subjects/buturi.html')
@app.route('/subjects')
def denjiki():
    return render_template('main/subjects/denjiki.html')
@app.route('/subjects')
def denkikairo():
    return render_template('main/subjects/denkikairo.html')
@app.route('/subjects')
def densikairo():
    return render_template('main/subjects/densikairo.html')
@app.route('/subjects')
def muki():
    return render_template('main/subjects/muki.html')
@app.route('/subjects')
def yuuki():
    return render_template('main/subjects/yuuki.html')


# ログアウトパス
@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return Response('''
    logout success!<br />
    <a href="/">login</a>
    ''')


if __name__ == '__main__':
    app.run()