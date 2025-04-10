from flask import Flask, render_template, request
import os
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form.get('name')
    app.logger.info(f"Received name: {name}")
    return render_template('result.html', name=name)

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    # debug_mode = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=True, host="0.0.0.0", port=5000)
