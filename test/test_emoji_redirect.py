import pytest

from emoji_redirect import app_provider


async def test_healthcheck(test_client):
    app = app_provider()
    client = await test_client(app)
    resp = await client.get('/healthcheck')
    assert resp.status == 200
    assert resp.headers['Content-Type'] == 'text/plain; charset=utf-8'
    assert resp.headers['Cache-Control'] == 'private, no-store, no-cache, must-revalidate'
    assert await resp.text() == 'OK'


async def test_favicon(test_client):
    app = app_provider()
    client = await test_client(app)
    resp = await client.get('/favicon.ico')
    assert resp.status == 404


async def test_robots(test_client):
    app = app_provider()
    client = await test_client(app)
    resp = await client.get('/robots.txt')
    assert resp.status == 404


async def test_sitemap(test_client):
    app = app_provider()
    client = await test_client(app)
    resp = await client.get('/sitemap.xml')
    assert resp.status == 404


async def test_redirect_root(test_client):
    app = app_provider()
    client = await test_client(app)
    resp = await client.get('/', allow_redirects=False)
    assert resp.status == 301
    assert resp.headers['Location'] == 'https://emoji-gen.ninja/'
    assert resp.headers['Cache-Control'] == 'public, max-age=600'


async def test_redirect_path(test_client):
    app = app_provider()
    client = await test_client(app)
    resp = await client.get('/foo/bar', allow_redirects=False)
    assert resp.status == 301
    assert resp.headers['Location'] == 'https://emoji-gen.ninja/foo/bar'
    assert resp.headers['Cache-Control'] == 'public, max-age=600'
