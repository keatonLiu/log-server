from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/log')
def show_log():
    return render_template('log.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
