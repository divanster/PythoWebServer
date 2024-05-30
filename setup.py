from setuptools import setup, find_packages

setup(
    name='my_web_framework',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'jinja2',  # For template rendering
        # Remove 'sqlite3' as it is part of the standard library
    ],
    entry_points={
        'console_scripts': [
            'my_web_framework = my_web_framework.core:start_server',
        ],
    },
    include_package_data=True,
    package_data={
        '': ['static/*', 'templates/*'],
    },
)
