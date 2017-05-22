#!/bin/bash

screen_name=status_app

case $1 in
"start")
  screen -dmS $screen_name python3 app.py
  ;;
"stop")
  screen -S $screen_name -X quit
  ;;
"restart")
  screen -S $screen_name -X quit
  screen -dmS $screen_name python3 app.py
  ;;
*)
  echo "Usage: $0 <start|stop|restart>"
  exit 1
esac
