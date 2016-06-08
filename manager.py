import os
import config
from datetime import datetime


def doSpeedTest():

    result = os.popen(config.speedtest_cli_dir).read()

    resultSet = result.split('\n')
    pingResult = resultSet[0]
    downloadResult = resultSet[1]
    uploadResult = resultSet[2]

    pingResult = float(pingResult.replace('Ping: ', '').replace(' ms', ''))
    downloadResult = float(downloadResult.replace('Download: ', '').replace(' Mbit/s', ''))
    uploadResult = float(uploadResult.replace('Upload: ', '').replace(' Mbit/s', ''))

    print(pingResult, downloadResult, uploadResult)

doSpeedTest()
