* [OSError](https://forum.pycom.io/topic/6375/lte-modem-lockup-all-methods-throw-oserror-the-requested-operation-failed/9)
* [troubleshooting LTE issues](https://docs.pycom.io/tutorials/networks/lte/)
* [logging screen output](https://fvdm.com/code/howto-write-screen-output-to-a-log-file)
```
# Start session with logging
screen -dmS test -L

# Enable realtime logging
screen -S test -X colon "logfile flush 0^M"

# Go to session
screen -r test

# Or follow the log
tail -Fn 0 screenlog.0
```
* [more on logging screen](https://unix.stackexchange.com/questions/416144/how-to-run-gnu-screen-in-detached-mode-over-serial-console-and-save-output)
