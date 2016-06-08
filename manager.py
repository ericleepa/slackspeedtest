import os
import config

result = os.popen(config.speedtest_cli_dir).read()

print(result)