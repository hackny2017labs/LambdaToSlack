import requests

url = 'https://hooks.slack.com/services/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'
#Could change to <!here>
text = "<!channel> Someone is at the :door:! (624)"

def handler(event, context):
    requests.post(url, json={"text": text + event.clickType})

