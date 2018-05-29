#!/bin/bash

set -eu -o pipefail

curl https://raw.githubusercontent.com/kadwanev/retry/master/retry -o /usr/bin/retry
chmod +x /usr/bin/retry

