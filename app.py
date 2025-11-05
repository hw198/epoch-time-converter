from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/convert', methods=['GET'])
def convert_epoch():
    epoch = request.args.get('epoch')
    
    if not epoch:
        return jsonify({"error": "Missing 'epoch' parameter"}), 400
    
    try:
        epoch = int(epoch)
    except ValueError:
        return jsonify({"error": "Epoch must be an integer"}), 400
    
    try:
        # Convert epoch to UTC datetime
        dt = datetime.utcfromtimestamp(epoch)
        formatted = dt.strftime('%Y-%m-%d %H:%M:%S UTC')
        
        return jsonify({
            "epoch": epoch,
            "datetime_utc": formatted,
            "iso_8601": dt.isoformat() + "Z"
        })
    except Exception as e:
        return jsonify({"error": "Invalid timestamp"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
