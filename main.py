import requests

url = 'https://hooks.slack.com/services/services/T59Q8770T/B62RB8DEJ/mgtQWUwwoBGUQ0WqFe1KUV0O'

text = "Someone is at the :door:! (624)"

def handler(event, context):
    requests.post(url, json={"text": text})
