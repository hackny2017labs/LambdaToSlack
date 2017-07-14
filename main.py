import requests

url = 'https://hooks.slack.com/services/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'

def handler(event, context):
    suite = ""
    if (event["clickType"] == "SINGLE"):
        suite = "624"
    elif (event["clickType"] == "DOUBLE"):
        suite = "622"
    text = "<!channel> Someone is at the " + suite + " :door:!"
    requests.post(url, json={"text": text})