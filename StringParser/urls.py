from StringParser import app
from flask import render_template
from StringParser.forms import StringParseForm 

@app.route("/",methods=["GET","POST"])
def index():
  Greeting= "Hi If you are seeing this page. Congrats!! App is working fine"
  return render_template('StringParser/index.html', greeting=Greeting)

@app.route("/parse", methods = ["GET","POST"])
def parse(request):
  form = StringParseForm()
  if form.validate_on_submit():
    form = StringParseForm(request.POST)
    return redirect(url_for(''))
  return render_template('StringParser/parse.html',form=form )
