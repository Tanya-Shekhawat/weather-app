from flask import Flask , render_template , request
import requests 

app = Flask(__name__) 

@app.route("/")
def home() :
    return render_template("index.html")

@app.route("/weatherapp")
def getWeather() :
    url = "https://api.openweathermap.org/data/2.5/weather" 
    param = {
    "city" : request.form.get("city") , 
    "units" : request.form.get("units"), 
    "appid" : request.form.get("appid") 
    }
    response = requests.get(url, params = param)
    data = response.json()

if __name__ == "__main__" :
    app.run(host="0.0.0.0", port = 5002) 