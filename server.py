from flask import Flask, render_template
app = Flask(__name__)    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run')
def run():
    return render_template('index.html')

@app.route('/pet')
def pet():
    return render_template('index.html')

if __name__=="__main__":   
    app.run(debug=True)      



