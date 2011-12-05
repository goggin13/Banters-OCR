

# Install gdata-python-client
`wget http://gdata-python-client.googlecode.com/files/gdata-2.0.15.tar.gz`
`tar zxvf gdata-2.0.15.tar.gz`
`cd gdata-2.0.15`
`./setup.py install`
`./tests/run_data_tests.py`

# Create auth file with your Google credentials
echo '{"username": "USERNAME", "password": "PASSWORD"}' > auth2.js