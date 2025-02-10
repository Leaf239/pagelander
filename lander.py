from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/<path:url>', methods=['GET'])
def proxy(url):
    scheme = 'https' if request.url.startswith('https') else 'http'
    target_url = f"{scheme}://{url}"
    
    try:
        headers = {k: v for k, v in request.headers if k.lower() != 'host'}
        r = requests.get(target_url, headers=headers, stream=True)
        return Response(r.raw, status=r.status_code, content_type=r.headers.get('Content-Type'))
    except:
        return 'Error', 500

app.run(host='0.0.0.0', port=80)
