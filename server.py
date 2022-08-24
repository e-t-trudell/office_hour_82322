from flask import Flask, render_template
app = Flask(__name__)    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run')
def run():
    return render_template('run.html')

@app.route('/pet')
def pet():
    return render_template('pet.html')

@app.route('/bite')
def bite():
    return render_template('bite.html')

@app.route('/climb')
def climb():
    return render_template('climb.html')

@app.route('/cower')
def cower():
    return render_template('cower.html')

@app.route('/friend')
def friend():
    return render_template('friend.html')

@app.route('/losthand')
def losthand():
    return render_template('losthand.html')



if __name__=="__main__":   
    app.run(debug=True)      



