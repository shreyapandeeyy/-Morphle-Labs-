from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Shreya Rajesh Pandey"
    username = os.getlogin()
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode()
    return f"Name - {full_name}<br>Username - {username}<br>Server Time in IST - {server_time}<br><pre>{top_output}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
