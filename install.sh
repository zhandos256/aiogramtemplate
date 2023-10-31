#!/bin/bash

sudo apt update && apt install git wget curl build-essential gdb lcov pkg-config \
      libbz2-dev libffi-dev libgdbm-dev libgdbm-compat-dev liblzma-dev \
      libncurses5-dev libreadline6-dev libsqlite3-dev libssl-dev \
      lzma lzma-dev tk-dev uuid-dev zlib1g-dev -y

sudo mkdir /var/log/aiogramtemplatelogs/
sudo chmod +x ./systemd/template.service
sudo cp ./systemd/template.service /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl enable template.service
sudo systemctl start template.service
sudo systemctl status template.service