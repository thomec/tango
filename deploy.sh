#! bin/bash

if [ -e ~/.virualenv/tango || -e ~/devel/virtualenv/tango ]
    then
        workon tango
    else
        mkvirtualenv -p /usr/bin/python3 tango

git clone https://github.com/thomec/tango.git tango 
