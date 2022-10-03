from flask import Flask, render_template  # , url_for, redirect, Blueprint
import sqlite3
con = sqlite3.connect("tutorial.db", check_same_thread=False)
cur = con.cursor()
# cur.execute("CREATE TABLE movie(title, year, score)")
# cur.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)
# con.commit()
app = Flask(__name__, template_folder='templates')

myAr = [3, 5, 7, 8]


@app.route('/')
def hello():
    res = cur.execute("SELECT * FROM movie")
    movies = res.fetchall()
    print(movies[0])
    context = {
        "name": "omri",
        "age": 10,
        "ar": myAr,
        "movies": movies
    }
    return render_template('hello.html', context=context)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
