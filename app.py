from flask import Flask, render_template,request,jsonify
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
info= []
@app.route("/login", methods=['GET','POST'])
def login():
    msg=""
    if request.method == 'POST':
        with open('data.json', 'r') as json_file:
            info= json.load(json_file)
        username = request.form['username']
        password = request.form['password']
        print(f'recived username: {username}, password:{password}')
        for i in info:
         if username == i['username'] and password== i['password']:
            return render_template("sucsses.html")
        else: 
            msg="not regesterd or incorrect info,please try again"
    
    return render_template("login.html",msg=msg)
@app.route("/singup", methods=['GET','POST'])
def singup():
    notice="you have successfully singed up" 
    if request.method == 'POST':
            username1 = request.form['username']
            password1 = request.form['password']
            print(f'recived username: {username1}, password:{password1}')
            info.append({'username':username1,'password':password1})
            json_data = jsonify(info)
    # Save the JSON data to a file
            with open('data.json', 'w') as json_file:
                json_file.write(json_data.get_data(as_text=True))
            return f"<p>{notice}</p>"
              
    return render_template("singup.html",notice=notice)       
if __name__ == '__main__':
    app.run(debug=True)
