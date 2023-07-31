import os
import sys
import json
import pathlib
import pytest

# sys.path.append(os.path.join(os.path.dirname(__file__),"..", ".."))
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
parent_dir = pathlib.Path(__file__).parent.resolve()
sys.path.append(os.path.join(parent_dir, '..', 'src'))
import lambdas.demo_lambda as handler


def test_init():                  
    event = {}
    context = None
    payload = handler.lambda_handler(event, context)
    assert payload['statusCode'] == 200

def test_s3_notify():
    # dirr = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
    # event_file_dir = os.path.join(dirr,"events/event.json")
    event_file_dir = os.path.join(parent_dir, '..', 'events/event.json')
    with open(event_file_dir, 'r') as json_file:
        event = json.load(json_file)
    context = None
    payload = handler.lambda_handler(event, context)
    assert payload['statusCode'] == 200
    assert payload['body'] == "Function invoked"

if __name__ == '__main__':
    test_s3_notify()