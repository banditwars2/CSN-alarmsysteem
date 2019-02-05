from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/alarmstatus', methods=["GET", "POST"])
def test():
    if request.method == 'POST':
        status = request.args['status']
        with open('alarm.txt', 'w') as file:
            file.write(status)
        return status
    else:
        with open('alarm.txt', 'r') as file:
            content = file.read()
            return content


@app.route('/alarmaan', methods=["POST"])
def alarm_on():
    if request.method == 'POST':
        status = request.args['status']
        with open('alarm.txt', 'w') as file:
            file.write(status)
        return render_template('index.html')


@app.route('/alarmoff', methods=["POST"])
def alarm_off():
    if request.method == 'POST':
        status = request.args['status']
        with open('alarm.txt', 'w') as file:
            file.write(status)
        return render_template('index.html')


@app.route('/isalive', methods=["GET"])
def check_is_alive():
    if request.method == 'GET':
        return "alive"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
