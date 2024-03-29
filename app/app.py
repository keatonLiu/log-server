import requests
from flask import Flask, request, Response

app = Flask(__name__, template_folder='templates')


@app.route('/log')
def show_log():
    fileuri = request.args.get('fileuri')
    if not fileuri:
        return 'fileuri is required', 400
    try:
        res = requests.get(fileuri)
    except requests.exceptions.RequestException as e:
        return str(e), 500
    return Response(res.content.decode('utf-8'), mimetype='text/plain', content_type='text/plain; charset=utf-8')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
