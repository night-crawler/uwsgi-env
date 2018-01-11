from setuptools import setup, find_packages
from uwsgi_env import __version__


try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = ''


setup(
    name='uwsgi-env',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/night-crawler/uwsgi-env',
    license='MIT',
    author='night-crawler',
    author_email='lilo.panic@gmail.com',
    description='Automatically populate env with UWSGI_ variables and run uwsgi',
    long_description=long_description,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
    ],
    requires=['uwsgi']
)
