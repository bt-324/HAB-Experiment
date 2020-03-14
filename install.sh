#!/bin/bash

cp geiger.service /etc/systemd/system/

systemctl start geiger.service
