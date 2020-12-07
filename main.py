from flask import Flask, request
import json
import base64

app = Flask(__name__)

@app.route('/health')
def health():
    return 'the api server is healthy!'

@app.route('/api/parse', methods=['POST'])
def parse():
    payload = json.loads(str(request.data, 'utf-8'))
    image_data =  payload['image']
    raw_image_data = base64.b64decode(image_data)
    # TODO: add your ML integration and put it to result_array
    result_array = []
    result_array.append(str(raw_image_data))
    result_array.append('another value')

    return {'result': result_array}
