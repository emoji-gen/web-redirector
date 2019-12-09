import pytest

from pkgs.entry import create_app


@pytest.fixture
def cli(loop, aiohttp_client):
    app = loop.run_until_complete(create_app())
    cli = loop.run_until_complete(aiohttp_client(app))
    return cli


async def test_healthcheck(cli):
    resp = await cli.get('/health')
    assert resp.status == 200
    assert resp.headers['Content-Type'] == 'text/plain; charset=utf-8'
    assert resp.headers['Cache-Control'] == 'private, no-cache, no-store, must-revalidate'
    assert await resp.text() == 'OK'


async def test_favicon(cli):
    resp = await cli.get('/favicon.ico')
    assert resp.status == 404


async def test_robots(cli):
    resp = await cli.get('/robots.txt')
    assert resp.status == 404


async def test_sitemap(cli):
    resp = await cli.get('/sitemap.xml')
    assert resp.status == 404


async def test_redirect_root(cli):
    resp = await cli.get('/', allow_redirects=False)
    assert resp.status == 301
    assert resp.headers['Location'] == 'https://emoji-gen.ninja/'
    assert resp.headers['Cache-Control'] == 'public, max-age=10'


async def test_redirect_path(cli):
    resp = await cli.get('/foo/bar', allow_redirects=False)
    assert resp.status == 301
    assert resp.headers['Location'] == 'https://emoji-gen.ninja/foo/bar'
    assert resp.headers['Cache-Control'] == 'public, max-age=10'
