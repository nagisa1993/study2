from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<guest>')
def index(guest):
	return render_template('index.html', name = guest)

@app.route('/<int:score>')
def showscore(score):
	return render_template('index2.html', marks = score)

@app.route('/examresult')
def showtable():
	dict = {'phy':50,'che':60,'maths':70}
	return render_template('bootstraptable.html', result = dict)

if __name__ == '__main__':
	app.run()