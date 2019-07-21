## 301 Moved Permanently
[![CircleCI](https://circleci.com/gh/emoji-gen/web-redirect/tree/master.svg?style=shield)](https://circleci.com/gh/emoji-gen/web-redirect/tree/master)
[![Requirements Status](https://requires.io/github/emoji-gen/web-redirect/requirements.svg?branch=master)](https://requires.io/github/emoji-gen/web-redirect/requirements/?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/56377d1a156e44fc93d98dbae392dad4)](https://www.codacy.com/app/pinemz/web-redirect?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=emoji-gen/web-redirect&amp;utm_campaign=Badge_Grade)
[![License](https://img.shields.io/github/license/emoji-gen/web-redirect.svg)](https://opensource.org/licenses/MIT)

:boat: The web application to redirect from old domain

![](assets/resized.jpg)<br>
<sup><sup>&copy; tsuneo/123RF.COM</sup></sup>
<br>
<br>

## Requirements

- Python `$(cat .python-version)`

## Libraries

- [aiohttp](https://github.com/aio-libs/aiohttp) - Server-side framework

## Getting started

```
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ python app.py
```

## Test

```
$ pip install -r requirements-dev.txt
$ pytest
```

## Publish
### Requirements

- [Heroku account](https://heroku.com/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

### Commands

```
$ heroku create your-app-name
$ heroku config:set ROOT_LOG_LEVEL=INFO
$ git push heroku master
```

## License

MIT &copy; [Emoji Generator](https://emoji-gen.ninja)
