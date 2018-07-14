import os
import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Returns JSON formatted date for AJAX-y goodness
@app.route('/date')
def current_date():
	return "{ date:\""+ datetime.datetime.now().strftime("%Y%m%d") +"\"}"
	
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)