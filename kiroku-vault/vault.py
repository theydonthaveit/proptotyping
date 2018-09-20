"""
Quart server imitating Vault
"""
import json
from quart import Quart

app = Quart(__name__)


@app.route('/', methods=['GET'])
async def home():
    """
    Async call initial
    """
    ALL_SECRETS = {
        'NEO4J_PASSWORD': 'K1r0ku',
        'FIREBASE_API': 'AIzaSyBJbaXJ-2oLLnkwivOEGRYcOOAgeePLKtY'
    }

    return json.dumps(ALL_SECRETS)

if __name__ == '__main__':
    app.run(debug=True, port=9999, host='0.0.0.0')
