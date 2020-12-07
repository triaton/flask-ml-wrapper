# Getting Started
The api documentation can be found [here](#api-documentation).

## Requirements

* python3

### Clone the repository, Make virtual environment and install dependencies

* Windows
```
# clone the repository
git clone https://github.com/triaton/flask-ml-wrapper.git

cd flask-ml-wrapper

# make virtual environemnt
py -m venv env

# activate the virtual environment
.\env\Scripts\activate.bat

# install dependencies
py -m pip install -r requirements.txt

# start the server for development
set FLASK_APP=main.py
flask run
```

* Linux
```
# clone the repository
git clone https://github.com/triaton/flask-ml-wrapper.git

cd ml-wrapper

# make virtual environemnt
virtuanenv env

# activate the virtual environment
source ./env/Scripts/activate

# install dependencies
pip install -r requirements.txt

# start the server for development
export FLASK_APP=main.py
flask run
```

## How to test the api
You can test the API with PostMan and directly using curl command.
```bash
curl --data-raw "{\"image\":\"aGVsbG8sIHdvcmxkIQ==\"}" --location --request POST 'http://localhost:5000/api/parse' --header 'Content-Type: application/json'
```

## How to integrate the ML part
You can find the `# TODO` commented part from `main.py` file. You can customize the code there. That's all.

## API Documentation

1. parse api
```
url: /api/parse
method: POST
payload:
{
    "image": "string"
}
Response format
{
    "success": "boolean",
    "data": "string"
}
```