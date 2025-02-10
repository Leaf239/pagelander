from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/<path:url>', methods=['GET'])
def proxy(url):
    target_url = f"http://{url}"
    
    try:
        response = requests.get(target_url)
        return Response(response.content, status=response.status_code, content_type=response.headers['Content-Type'])
    except requests.exceptions.RequestException as e:
        return f"Error accessing {target_url}: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
