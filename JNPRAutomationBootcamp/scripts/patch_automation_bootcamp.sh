#!/usr/bin/env bash

sudo pip install virtualenv
mkdir ~/.virtualenvs
sudo pip install virtualenvwrapper
<<<<<<< HEAD
=======
export WORKON_HOME=~/.virtualenvs
. /usr/local/bin/virtualenvwrapper.sh
>>>>>>> 9d5b195a181f5da6323880bfae023539c72256e0
mkvirtualenv automation_bootcamp
