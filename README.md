# slackspeedtest
A python app that uses [speedtest-cli](https://github.com/sivel/speedtest-cli) to run a speed test and post the results to a slack channel.


###Config file

```
# config.py

speedtest_cli_dir = "Location of the directory in which speedtest-cli is installed"
slack_webhook_url ='Your slack incoming webhook url'
#Numbers below the down and upload threshold will trigger warning status
download_threshold = 10
upload_threshold = 5
#numbers above the ping threshold wil trigger warning status
ping_threshold = 20
log_file = "Location of where you would like to put a log file (csv) ex: C:/log.csv"
```



