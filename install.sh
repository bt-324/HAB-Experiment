#!/bin/bash

cp geiger.service /etc/systemd/system/

systemctl daemon-reload

systemctl start geiger.service
systemctl enable geiger.service
