## Installation
```bash
pip install -e git+https://github.com/night-crawler/uwsgi-env.git#egg=uwsgi-env
    # OR
pip install uwsgi-env
```

### Usage

```python
@manager.option('-h', '--host', dest='host')
@manager.option('-p', '--port', dest='port')
def uwsgi(host=None, port=None,):
    from uwsgi_env.utils import uwsgi as _uwsgi
    return _uwsgi(host=host, port=port, project='my_project')

```

Original by @unbit, [django-uwsgi](https://github.com/unbit/django-uwsgi)
