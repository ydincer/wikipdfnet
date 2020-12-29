from flask import Flask,render_template,request,send_file,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,validators,Label
import os
import pdfkit
import random


def wiki(url,filename):
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_url(url,filename, configuration=config)
    


app = Flask(__name__)

app.config['SECRET_KEY'] = 'wikipdf.net'

class UrlForm(FlaskForm):
    style={"class":"form-control","aria-describedby":"inputGroup-sizing-lg",
    "placeholder":"Wikipedia URL address"}
    url = StringField("",
    [validators.Length(min=4, max=25,message="Please url address enter")],render_kw=style)

@app.route('/')
def index():
    form = UrlForm(request.form)
    return render_template('index.html',form = form)


@app.route('/download',methods=['POST'])
def download():
    url = request.form['url']
    path ='pdf-'+str(random.randint(1000,9999))+'.pdf'
    wiki(url,path)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)