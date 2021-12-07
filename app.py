from flask import *
import weatherapp

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def main():
    temp = ""
    if request.method == "POST":
        cityname = request.form.get("city")
        print(str(cityname))
        temp = weatherapp.getweather(cityname)
        print(temp)
    return render_template("index.html", temp=temp)


if __name__ == '__main__':
    app.run(threaded=True,port=5000)