from setuptools import find_packages, setup

setup(
    name='tweetstorm',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tweetstorm=tweetstorm.__main__:main'
        ]
    },
)
