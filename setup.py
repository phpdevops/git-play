from distutils.core import setup

try:
    ldsc = open("README.rst").read()
except:
    ldsc = ""

setup(
    name="git-play",
    version="0.12",
    author="Ju-yeong Park",
    author_email="interruptz@gmail.com",
    scripts=["bin/git-play"],
    url="http://github.com/interruptz/git-play",
    license="MIT LICENSE",
    description="Git-play is a custom git command for deploying an application server very easily from a remote git repository. It checks the remote git repository every minute and if something has changed, it will restart the application server automatically.",
    long_description = ldsc,
    install_requires=[
        'PyYAML==3.10',
        'GitPython==0.3.2.RC1'      
    ]
)
