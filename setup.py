from setuptools import setup, find_packages

setup(
    name='my_web_framework',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'my_web_framework = my_web_framework.core:start_server',
        ],
    },
)
