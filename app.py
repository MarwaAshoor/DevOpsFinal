from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Route to display the form and calculate age
@app.route('/', methods=['GET', 'POST'])
def home():
    age = None
    if request.method == 'POST':
        birth_year = request.form['birth_year']
        try:
            birth_year = int(birth_year)
            current_year = datetime.now().year
            age = current_year - birth_year
        except ValueError:
            age = "Invalid year, please enter a valid number."
    
    return render_template('index.html', age=age)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)