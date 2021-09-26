from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tracardi-mysql-connector',
    version='0.1',
    description='This plugin connect to Mysql database',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Patryk Migaj',
    author_email='patromi123@gmail.com',
    packages=['tracardi_mysql_connector'],
    install_requires=[
        'tracardi-plugin-sdk',
        'tracardi',
        'wheel',
        'twine'
        'sqlalchemy',
        'mysqlclient'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    keywords=['tracardi', 'plugin'],
    include_package_data=True,
    python_requires=">=3.8",
)