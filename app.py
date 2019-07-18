#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import os
from pathlib import Path

from aiohttp.web import run_app

src_path = str(Path(__file__).resolve().parent.joinpath('src'))
sys.path.append(src_path)

# ------------------------------------------------------------------------------

from server import app_factory

if __name__ == '__main__':
    run_app(app_factory(), host='0.0.0.0', port=5000)
