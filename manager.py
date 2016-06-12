import os
import config
import speedtest_bot


def doSpeedTest():
    result = os.popen(config.speedtest_cli_dir).read()

    resultSet = result.split('\n')
    pingResult = resultSet[0]
    downloadResult = resultSet[1]
    uploadResult = resultSet[2]

    pingfloat = float(pingResult.replace('Ping: ', '').replace(' ms', ''))
    downloadfloat = float(downloadResult.replace('Download: ', '').replace(' Mbit/s', ''))
    uploadfloat = float(uploadResult.replace('Upload: ', '').replace(' Mbit/s', ''))

    print(pingResult, downloadResult, uploadResult)
    buildjson(downloadResult, uploadResult, pingResult)


def buildjson(down, up, ping):
    test_to_string = ("%s  \n%s \n%s" % (down, up, ping))
    list = []
    print(test_to_string)
    test = {'text': test_to_string, 'color': 'good', 'fallback': 'No speedtest data', 'title': 'Speedtest.net',
            'pretext': 'Speed test results', 'title_link': 'https://speedtest.net/run'}
    list.append(test)
    payload = {'attachments': list}
    print(payload)
    speedtest_bot.post_to_slack(payload)


doSpeedTest()
