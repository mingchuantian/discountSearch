from app import app
from flask import render_template
from app.forms import BrandSubmitForm


@app.route('/', methods = ['GET', 'POST'])
def index():
    form = BrandSubmitForm()
    return render_template('index.html', form=form)

@app.route('/submitted/<brand>')
def submitted(brand):
    with open("websites.txt", 'w') as websites:
        websites.write("https://www.davidjones.com/brand/" + brand)
    crawler = Sites()
    crawler.run_crawler()
    return "Your submission successed."