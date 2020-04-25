#!/bin/bash

WD=`pwd`
echo ${WD}
PYTHON_SCRIPT=`which python3`\ ${WD}/downloader.py

echo ${PYTHON_SCRIPT}

sed -i -e "s^<CMD>^ExecStart=`echo ${PYTHON_SCRIPT}`^g" downloader.service

