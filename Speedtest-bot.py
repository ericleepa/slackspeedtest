import config
import requests

data = {
    "attachments": [
        {
            "fallback": "Speedtest",
            "pretext": "Speed test results,
            "title": "Results",
            "title_link": "https://speedtest.net/run",
            "text": "1up, 1down, ping 10ms",
            "color": "good"
        }
    ]
}

def Post_to_slack(data):
    requests.post(config.slack_webhook_url, json=data)


Post_to_slack(data)