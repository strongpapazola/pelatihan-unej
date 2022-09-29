from flask import Flask, jsonify, make_response
app = Flask(__name__)
status = 'off'
@app.route('/')
def root():
    return 'Aplikasi Lampu IoT'
# http://127.0.0.1:3001/status_lampu
@app.route('/status_lampu')
def status_lampu():
    global status
    return make_response(jsonify({'status_lampu': status}), 200)
# http://127.0.0.1:3001/set_lampu/on
# http://127.0.0.1:3001/set_lampu/off
@app.route('/set_lampu/<set>')
def set_lampu(set):
    global status
    status = set
    return make_response('ok', 200)
if __name__ == '__main__':
    # port 1 - 65535
    app.run(host='0.0.0.0', port=3001, debug=True)