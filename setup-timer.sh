#!/bin/bash

PYTHON=`which python3`
CD=`which cd`
WD=`pwd`
echo ${WD}
PYTHON_SCRIPT=${PYTHON}\ ${WD}/downloader.py

echo ${PYTHON_SCRIPT}

echo ${CHANGE_DIR}
sed -e "s^<CD>^WorkingDirectory=`echo ${WD}`^g" downloader.service-config > downloader.service
sed -i -e "s^<CMD>^ExecStart=`echo ${PYTHON_SCRIPT}`^g" downloader.service


mkdir -p ~/.config/systemd/user
cp downloader.service ~/.config/systemd/user/downloader.service
cp downloader.timer ~/.config/systemd/user/downloader.timer

systemctl --user daemon-reload 
systemctl --user enable downloader.service
systemctl --user enable downloader.timer
systemctl --user start downloader.timer
systemctl --user list-timers --all
