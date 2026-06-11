from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

ORIGINAL_API = "https://ravenxkiller.site/rz/r.php"

@app.route('/check', methods=['GET'])
def check():
    cc = request.args.get('cc')
    site = request.args.get('site')
    proxy = request.args.get('proxy')
    
    if not cc or not site or not proxy:
        return jsonify({"error": "Missing cc, site, or proxy"}), 400
    
    resp = requests.get(ORIGINAL_API, params={'cc': cc, 'site': site, 'proxy': proxy})
    data = resp.json()
    
    # Print exact response to console
    print(json.dumps(data, indent=2))
    
    # Return exact response
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
