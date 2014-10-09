from setuptools import setup, find_packages

__version__ = None
with open('bluesnap/version.py') as f:
    exec(f.read())

with open('README.md') as f:
    long_description = f.read()

setup(
    name='bluesnap',
    version=__version__,
    author='Jian Yuan Lee',
    author_email='jian@justyoyo.com',
    url='https://github.com/justyoyo/bluesnap-python',
    # license='TODO',
    description='Python module to interact with Bluesnap API.',
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'lxml==3.4.0',
        'requests==2.4.3'
    ],
)
