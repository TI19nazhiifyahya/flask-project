from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
    grade_dict = {'phy':50,'che':70, 'maths':60}
    return render_template('results.html', result = grade_dict)