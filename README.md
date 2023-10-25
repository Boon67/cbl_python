# Python Bindings For Couchbase Lite
This directory contains a Python API binding of [Couchbase Lite][CBL], an embedded NoSQL document database engine with sync. It consists of Python classes that call glue generated by [CFFI][CFFI], which calls into [Couchbase Lite's C API][CBL_C].

It's assumed you have a functioning python environment (v3.x)

### Setup Process
This process uses the CBLite C api to build the libraries for Python to leverage. In order to setup the preqs and test it, run the appropriate file in the `setup_scripts` folder for your OS. It's forked off the CouchbaseLabs experimental bindings: https://github.com/couchbaselabs/couchbase-lite-python. It will ask you for a password as some of the commands require sudo

### Testing 
After successful completion of the setups scripts you can run the demo.py file. This will create some simple records and allow for you to extend, test from their. 

If you want to review the data in the DB, https://sqlitebrowser.org/ is a fantastic tool for inpecting the DB

