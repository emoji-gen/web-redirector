#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import os
from pathlib import Path

from aiohttp.web import run_app

src_path = str(Path(__file__).resolve().parent.joinpath('.'))
sys.path.append(src_path)

# ------------------------------------------------------------------------------

from pkgs.server import create_app

if __name__ == '__main__':
    run_app(create_app(), host='0.0.0.0', port=5000)
