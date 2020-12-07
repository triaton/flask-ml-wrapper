from flask import Flask, request
import json
import base64
import your_module_name

app = Flask(__name__)

@app.route('/health')
def health():
    return 'the api server is healthy!'

@app.route('/api/parse', methods=['POST'])
def parse():
    # the request.data is a raw buffer and it should be encoded into a string
    payload_str = str(request.data, 'utf-8')
    
    # parse the json encoded stirng to a python dictionary object
    payload = json.loads(payload_str)

    # get image data from the payload (it should be base64 encoded)
    image_data =  payload['image']
    raw_image_data = base64.b64decode(image_data)
    # TODO: add your ML integration and put it to result_array
    result_array = your_module_name.process(raw_image_data)
    # result_array = []
    # result_array.append(str(raw_image_data))
    # result_array.append('another value')

    return {'result': result_array}
