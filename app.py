from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Route to display the form and calculate age
@app.route('/', methods=['GET', 'POST'])
def home():
    age = None
    if request.method == 'POST':
        birthday_str = request.form['birthday']
        birthday = datetime.strptime(birthday_str, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    
    return render_template('index.html', age=age)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)
