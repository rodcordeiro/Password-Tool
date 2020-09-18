# /usr/bin/Password-Tool

py_version=`cat python_version.txt`
py_version=${py_version%.*}
current_dir=`pwd`

# This just executes the main.py file and makes it easier to debug
python${py_version} ${current_dir}/main.py

