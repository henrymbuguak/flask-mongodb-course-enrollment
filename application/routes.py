from application import app
from flask import render_template, request, json, Response, redirect, flash, url_for
from application.models import Course, Enrollment, User
from application.forms import LoginForm, RegisterForm

courseData = [
    {
        "courseID": "1111",
        "title": "PHP 101",
        "description": "Intro to PHP",
        "credits": 3,
        "term": "Fall, Spring",
    },
    {
        "courseID": "2222",
        "title": "Java 1",
        "description": "Intro to Java Programming",
        "credits": 4,
        "term": "Spring",
    },
    {
        "courseID": "3333",
        "title": "Adv PHP 201",
        "description": "Advanced PHP Programming",
        "credits": 3,
        "term": "Fall",
    },
    {
        "courseID": "4444",
        "title": "Angular 1",
        "description": "Intro to Angular",
        "credits": 3,
        "term": "Fall, Spring",
    },
    {
        "courseID": "5555",
        "title": "Java 2",
        "description": "Advanced Java Programming",
        "credits": 4,
        "term": "Fall",
    },
]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", index=True)


@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term="Spring 2019"):
    return render_template(
        "courses.html", courseData=courseData, courses=True, term=term
    )


@app.route("/register")
def register():
    form = RegisterForm()
    return render_template("register.html", form=form, register=True)


@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.objects(email=email).first()
        if user and password == user.password:
            flash(f"{user.first_name}, you are successfully logged in!", "success")
            return redirect(url_for('index'))
        else:
            flash("Sorry, the email or password is wrong!.", "danger")
    return render_template("login.html", title="Login", form=form, login=True)


@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    id = request.form.get("courseID")
    title = request.form.get("title")
    term = request.form.get("term")

    data = {"id": id, "title": title, "term": term}

    return render_template("enrollment.html", course=data, enrollment=True)


@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if idx == None:
        jdata = courseData
    else:
        jdata = courseData[int(idx)]
    return Response(json.dumps(jdata), mimetype="application/json")





@app.route("/user")
def user():
    # User(
    #     user_id=1,
    #     first_name="Henry",
    #     last_name="Kiarie",
    #     email="kiarie@gmail.com",
    #     password="abd123",
    # ).save()
    # User(
    #     user_id=2,
    #     first_name="James",
    #     last_name="King",
    #     email="king@gmail.com",
    #     password="abd1235",
    # ).save()

    users = User.objects.all()
    return render_template("users.html", users=users)
