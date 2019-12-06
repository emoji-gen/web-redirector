#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from aiohttp.web import run_app

from pkgs.entry import create_app

if __name__ == '__main__':
    run_app(create_app(), host='0.0.0.0', port=5000)
