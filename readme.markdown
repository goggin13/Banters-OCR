## Get the code
* `git clone git@github.com:goggin13/Banters-OCR.git`

## Dependencies
* Python 2.6  
* httplib2 - `easy_install-2.6 httplib2` (the '-2.6' is necessary if you have multiple python versions, e.g. OSX 10.7)  

## Install gdata-python-client  
* `wget http://gdata-python-client.googlecode.com/files/gdata-2.0.15.tar.gz`  
or  
* `curl -O http://gdata-python-client.googlecode.com/files/gdata-2.0.15.tar.gz`  
then  
* `tar zxvf gdata-2.0.15.tar.gz`  
* `cd gdata-2.0.15`  
* `./setup.py install`  
  (if python2.6 is not your system default, you may need to either make it, with `defaults write com.apple.versioner.python Version 2.6`, or find a pay to tell setup.py to install version 2.6)
* `./tests/run_data_tests.py`  
* clean up
  * `rm -r gdata-2.0.15`
  * `rm -r gdata-2.0.15.tar.gz`  

## Create auth file
Using your Google credentials, and a https://staging.banters.com session_id  
* `echo '{"username": "USERNAME", "password": "PASSWORD", "session_id": "SESSION_ID"}' > auth2.js`  

## Run it
* `python banters_ocr.py`
