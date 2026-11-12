from flask import Flask

app = Flask(__name__) 
#creates flask applciation; idk what flask is 

def add(a, b):
    return a + b


@app.route("/") 
#this routes the url to our home function 
def home():
    return f"App is running! 3+2 = {add(3, 2)}"
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    #so when calling the fucntion in main were runnning the app on port 50000