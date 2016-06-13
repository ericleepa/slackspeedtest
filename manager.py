import os
import config
import csv
import requests
from datetime import datetime

def do_speed_test():
    print("run speedtest_cli")
    result = os.popen(config.speedtest_cli_dir).read()
    print(result)

    resultSet = result.split('\n')
    pingResult = resultSet[0]
    downloadResult = resultSet[1]
    uploadResult = resultSet[2]

    pingfloat = float(pingResult.replace('Ping: ', '').replace(' ms', ''))
    downloadfloat = float(downloadResult.replace('Download: ', '').replace(' Mbit/s', ''))
    uploadfloat = float(uploadResult.replace('Upload: ', '').replace(' Mbit/s', ''))

    print(pingResult, downloadResult, uploadResult)

    with open(config.log_file, 'a', newline='') as log:
        csvw = csv.writer(log, delimiter=',')
        data = [str(pingfloat), str(downloadfloat), str(uploadfloat), str(datetime.now())]
        print(data)
        csvw.writerows([data])

    analyize_results(downloadfloat, uploadfloat, pingfloat, result)

def analyize_results(downmb, upmb, pingms, result):
    print(downmb)
    print(upmb)
    print(pingms)
    if downmb <= config.download_threshold or upmb <= config.upload_threshold or pingms >= config.ping_threshold:
        status = "danger"
        build_json(result, status)
    else:
        status = "good"
        build_json(result, status)

def build_json(result, status):
    test_to_string = ("%s" % (result))
    list = []
    print(test_to_string)
    test = {'text': test_to_string, 'color': status, 'fallback': 'New speed test', 'title': 'Speedtest.net',
            'pretext': "Speed test results", 'title_link': 'https://speedtest.net/run'}
    list.append(test)
    if status == "danger":
        test.update({"footer": "<!channel>"})
    payload = {'attachments': list}
    print(payload)
    post_to_slack(payload)

def post_to_slack(json):
    r = requests.post(config.slack_webhook_url, json=json)
    print(r)

do_speed_test()
