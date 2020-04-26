#!/bin/bash

PYTHON=`which python3`
CD=`which cd`
WD=`pwd`
echo ${WD}
PYTHON_SCRIPT=${PYTHON}\ ${WD}/src/downloader.py

echo ${PYTHON_SCRIPT}

echo ${CHANGE_DIR}
sed -e "s^<CD>^WorkingDirectory=`echo ${WD}`^g" ./scripts/downloader.service-config > ./scripts/downloader.service
sed -i -e "s^<CMD>^ExecStart=`echo ${PYTHON_SCRIPT}`^g" ./scripts/downloader.service


mkdir -p ~/.config/systemd/user
cp scripts/downloader.service ~/.config/systemd/user/downloader.service
cp scripts/downloader.timer ~/.config/systemd/user/downloader.timer

systemctl --user daemon-reload 
systemctl --user enable downloader.service
systemctl --user enable downloader.timer
systemctl --user start downloader.timer
systemctl --user list-timers --all
