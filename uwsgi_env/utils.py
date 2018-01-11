import os
import sys
import multiprocessing


# https://github.com/unbit/django-uwsgi
def uwsgi(host=None, port=None, root=None, project=None, debug=False, static_url=None, static_root=None):
    host = host or os.getenv('HOST', '0.0.0.0')
    root = root or os.getenv('ROOT', os.getcwd())
    project = project or os.getenv('PROJECT', os.path.basename(root))
    http_port = port or os.getenv('PORT', port) or '8000'

    sys.stdout.write('=' * 80 + '\n')
    sys.stdout.write('\tROOT: %s\n' % root)
    sys.stdout.write('\tHOST: %s\n' % host)
    sys.stdout.write('\tPORT: %s\n' % http_port)
    sys.stdout.write('\tPROJECT: %s\n' % project)
    sys.stdout.write('=' * 80 + '\n')
    sys.stdout.flush()

    os.environ.setdefault('UWSGI_MODULE', '%s.wsgi' % project)

    # set protocol as uwsgi
    os.environ.setdefault('UWSGI_PROTOCOL', 'uwsgi')
    os.environ['UWSGI_HTTP_SOCKET'] = '%s:%s' % (host, http_port)

    # set process names
    os.environ.setdefault('UWSGI_AUTO_PROCNAME', 'true')
    os.environ.setdefault('UWSGI_PROCNAME_PREFIX_SPACED', '[uWSGI %s]' % project)
    # remove sockets/pidfile at exit
    os.environ.setdefault('UWSGI_VACUUM', 'true')
    # retrieve/set the PythonHome
    os.environ.setdefault('UWSGI_VIRTUALENV', sys.prefix)
    # add project to python path
    os.environ.setdefault('UWSGI_PP', root)

    os.environ.setdefault('UWSGI_POST_BUFFERING', '1048576')
    os.environ.setdefault('UWSGI_RELOAD_ON_RSS', '300')
    # increase buffer size a bit
    os.environ.setdefault('UWSGI_BUFFER_SIZE', '65535')
    # some additions required by newrelic
    os.environ.setdefault('UWSGI_ENABLE_THREADS', 'true')
    os.environ.setdefault('UWSGI_LAZY_APPS', 'true')
    os.environ.setdefault('UWSGI_SINGLE_INTERPRETER', 'true')
    os.environ.setdefault('UWSGI_AUTOLOAD', 'true')
    # set 12 workers and cheaper to number of cpus
    os.environ.setdefault('UWSGI_WORKERS', '12')
    os.environ.setdefault('UWSGI_CHEAPER', str(multiprocessing.cpu_count()))
    # enable the master process
    os.environ.setdefault('UWSGI_MASTER', 'true')

    os.environ.setdefault('UWSGI_NO_ORPHANS', 'true')
    os.environ.setdefault('UWSGI_MEMORY_REPORT', 'true')
    os.environ.setdefault('UWSGI_DISABLE_LOGGING', 'true')

    # set harakiri
    os.environ.setdefault('UWSGI_HARAKIRI', '60')
    os.environ.setdefault('UWSGI_HARAKIRI_VERBOSE', 'true')

    # set uid and gid
    os.environ.setdefault('UWSGI_UID', str(os.getuid()))
    os.environ.setdefault('UWSGI_GID', str(os.getgid()))
    os.environ.setdefault('UWSGI_CACHE2', 'name=%s,items=20000,keysize=128,blocksize=4096' % project)

    if debug and static_url and static_root:
        # map and serve static files
        os.environ.setdefault('UWSGI_STATIC_MAP', '%s=%s' % (static_url, static_root))
        os.environ.setdefault('UWSGI_PY_AUTORELOAD', '2')

    return os.execvp('uwsgi', ('uwsgi',))
