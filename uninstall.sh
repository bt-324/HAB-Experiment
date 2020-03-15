#!/bin/bash

exec systemctl stop geiger.service 

rm /etc/systemd/system/geiger.service

systemctl daemon-restart
