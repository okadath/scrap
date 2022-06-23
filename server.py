from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   # return "a"
   # else:
   #    user = request.args.get('nm')
   #    return redirect(url_for('success',name = user))
   return render_template("login.html")

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')