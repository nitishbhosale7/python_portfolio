from os import name
from flask import Flask ,render_template , request ,redirect
from flask.wrappers import Request
import csv

app = Flask(__name__)
print(__name__)


# @app.route('/works.html')
# def new():
#     return render_template('works.html')


@app.route('/')
def home():
    return render_template('index.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# @app.route('/about.html')
# def about():
#     return render_template('about.html')


# @app.route('/components.html')
# def components():
#     return render_template('components.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_data(data):
    with open('database.txt',mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n emai; = {email} , subject =  {subject} , message = {message}')



def write_to_csv(data):
    with open('databases.csv',mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer=csv.writer(database2, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form',methods=['GET' , 'POST'])
def submit_form():  
    if request.method == 'POST' :
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thank_you.html')

    else:
        return 'Something went wrong' 