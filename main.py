import requests

def handler(event, context):
    requests.post('https://hooks.slack.com/services/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',json={"text" : "Someone is at the :door:! (624)" })
