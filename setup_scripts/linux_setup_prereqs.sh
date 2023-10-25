curl -O https://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0-noarch.deb
sudo apt install ./couchbase-release-1.0-noarch.deb
sudo apt update
sudo apt install libcblite
rm ./couchbase-release-1.0-noarch.deb

mkdir ~/Documents/code
cd ~/Documents/code
git clone https://github.com/couchbaselabs/couchbase-lite-python


pip3 install cffi
cd couchbase-lite-python
cp /usr/lib/aarch64-linux-gnu/libcblite* ./CouchbaseLite
./build.sh