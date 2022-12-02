## 301 Moved Permanently
[![CircleCI](https://circleci.com/gh/emoji-gen/web-redirector/tree/master.svg?style=shield)](https://circleci.com/gh/emoji-gen/web-redirector/tree/master)
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
$ heroku addons:create heroku-redis:hobby-dev
$ heroku buildpacks:add https://github.com/heroku/heroku-buildpack-multi.git
$ git push heroku master
```

## License

MIT &copy; [Emoji Generator](https://emoji-gen.ninja)
