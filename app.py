from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_time', methods=['POST'])
def fetch_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_time

# @app.route('/upload_image', methods=['POST'])
# def upload_image():
#     if 'file' not in request.files:
#         return 'No file part'
#     file = request.files['file']
#     if file.filename == '':
#         return 'No selected file'
#     if file:
#         file.save(f"static/{file.filename}")
#         return f"Image uploaded: <img src='/static/{file.filename}' alt='Uploaded Image'>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)