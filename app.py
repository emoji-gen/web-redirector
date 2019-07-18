#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import os
from pathlib import Path

from aiohttp.web import run_app

src_path = str(Path(__file__).resolve().parent.joinpath('src'))
sys.path.append(src_path)

# ------------------------------------------------------------------------------

from emoji_redirect import provide_app
app = provide_app()

if __name__ == '__main__':
    run_app(app, host='0.0.0.0', port=5001)
