from flask import Flask,jsonify,render_template
from flask_cors import CORS
import sqlite3
con = sqlite3.connect("titanic.sqlite")
cur = con.cursor()
application = Flask(__name__)

CORS(application)
@application.route("/")
def index():
    return render_template("index.html")

@application.route("/hello")
def hello():
    return "Hello World!"
@application.route("/api/v1.0/names")
def names():
    # Create our session (link) from Python to the DB
    # session = Session(engine)
    all=[]
    con = sqlite3.connect("titanic.sqlite")
    cur = con.cursor()

    """Return a list of all passenger names"""
    # Query all passengers
    results = cur.execute("SELECT name FROM passenger").fetchall()
    
    for i in results:
            names = {}
            print(i[0])
            names["name"] = i[0]
            all.append(names)

    # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))
    con.close()
    return jsonify(all)
@application.route("/api/v1.0/passengers")
def passengers():
    # Create our session (link) from Python to the DB
    # session = Session(engine)
    all=[]
    con = sqlite3.connect("titanic.sqlite")
    cur = con.cursor()
    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results = cur.execute("SELECT name,age,sex FROM passenger").fetchall()
    # results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

    # session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_passengers = []
    for name, age, sex in results:
        passenger_dict = {}
        passenger_dict["name"] = name
        passenger_dict["age"] = age
        passenger_dict["sex"] = sex
        all_passengers.append(passenger_dict)

    return jsonify(all_passengers)
if __name__ == "__main__":
    application.run(port=5000, debug=True)