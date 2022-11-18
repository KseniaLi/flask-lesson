import sys

from flask import Flask, render_template, request, redirect, url_for

from model import db, db_init, Post
from config import SQLITE_DATABASE_NAME

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + SQLITE_DATABASE_NAME
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db.app = app
db.init_app(app)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html")


@app.route('/about.html')
def about():
    return render_template("about.html")


@app.route('/resume.html')
def resume():
    return render_template("resume.html")


@app.route('/contact.html', methods=['GET', 'POST'])
def message():
    posts = Post.query.order_by(Post.id.desc()).all()

    if request.method == "POST":
        name = request.form.get('name', type=str, default="")
        text = request.form.get('text', type=str, default="")
        print(name, text)
        p = Post(name=name, text=text)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('message'))

    return render_template("contact.html", posts=posts)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "init":
            with app.app_context():
                db_init()
                sys.exit(0)

    app.run(host='0.0.0.0', port=5000, debug=True)
