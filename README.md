## 301 Moved Permanently
[![CircleCI](https://circleci.com/gh/emoji-gen/web-redirect/tree/master.svg?style=shield)](https://circleci.com/gh/emoji-gen/web-redirect/tree/master) [![Requirements Status](https://requires.io/github/emoji-gen/web-redirect/requirements.svg?branch=master)](https://requires.io/github/emoji-gen/web-redirect/requirements/?branch=master) [![Osushi](https://img.shields.io/badge/donate-osushi-EA2F57.svg)](https://osushi.love/intent/post/9ad90add99954e62ac79251606c10eec)

:boat: The web application to redirect from old domain
<br>
<br>

## Requirements

- Python `$(cat .python-version)`

## Getting started

```
$ pip install -r requirements.txt
$ python app.py
```

## Publish
### Requirements

- [Heroku account](https://heroku.com/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

### Commands

```
$ heroku create
$ heroku buildpacks:set https://github.com/heroku/heroku-buildpack-multi.git
$ heroku config:set ROOT_LOG_LEVEL=INFO
$ git push heroku master
```

## License

MIT &copy; [Emoji Generator](https://emoji-gen.ninja)
