cd ..
pip3 install cffi
curl https://packages.couchbase.com/releases/couchbase-lite-c/3.1.1/couchbase-lite-c-enterprise-3.1.1-macos.zip --output ./couchbase-lite-c-enterprise-3.1.1-macos.zip
unzip ./couchbase-lite-c-enterprise-3.1.1-macos.zip 
sudo mkdir /usr/local/include/
sudo cp -r ./libcblite-3.1.1/include/ /usr/local/include/
sudo cp -r ./libcblite-3.1.1/lib/libcblite* /usr/local/lib/
cp -r ./libcblite-3.1.1/lib/libcblite* ./CouchbaseLite
rm -Rf ./libcblite-3.1.1
rm couchbase-lite-c-enterprise-3.1.1-macos.zip

#Now Build it
cd CouchbaseLite #Have to be in this folder
../build.sh