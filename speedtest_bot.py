import config
import requests

#Example formatting
data = {
    "attachments": [
        {
            "fallback": "No speedtest data",
            "pretext": "Speed test results",
            "title": "Speedtest.net",
            "title_link": "https://speedtest.net/run",
            "text": "1up, 1down, ping 10ms",
            "color": "good"
        }
    ]
}

def post_to_slack(var):
    r = requests.post(config.slack_webhook_url, json=var)
    print(r)


