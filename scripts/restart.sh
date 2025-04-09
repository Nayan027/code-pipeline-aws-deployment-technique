#!/bin/bash

echo "running restart.sh ..." >> /home/ubuntu/restart.log

bash /home/ubuntu/scripts/stop.sh
sleep 2  # Give time to shut down properly
bash /home/ubuntu/scripts/start.sh

if [ $? -eq 0 ]; then
    echo "restart.sh completed successfully" >> /home/ubuntu/restart.log
else
    echo "restart.sh failed!" >> /home/ubuntu/restart.log
    exit 1
fi
