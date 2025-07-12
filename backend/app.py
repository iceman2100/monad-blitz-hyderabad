from flask import Flask, jsonify
from datetime import datetime
app = Flask(__name__)


@app.route('/stream/<address>')
def stream_info(address):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({
        "address": address,
        "rate": "0.01 ETH/sec",
        "start_time": current_time,
        "status": "Streaming"
    })

if __name__ == '__main__':
    app.run(debug=True)
