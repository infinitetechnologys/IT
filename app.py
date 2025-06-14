from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/services')
def services():
    return render_template('services.html')   

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html') 

@app.route('/contact')
def contact():
    return render_template('contact.html') 
@app.route('/sitemap.xml')
def sitemap():
    return render_template('sitemap.xml') 
    
@app.route('/robots.txt')
def robots():
    return render_template('robots.txt') 
if __name__ == '__main__':
    app.run(debug=True)
