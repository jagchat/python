Demonstrates following:

- Reading config from "config.json"
- Reading environment variables to override config.json
- Logging to console and file
- Reading command line arguments for log output
- Working with FastAPI (and uvicorn)
- Graceful shutdown

Steps to run:

- Ensure "venv" is up
- Following writes to "app-log.log" by default in current app folder

```commandline
python main.py
```

Following are supported

```commandline
python main.py --log-output console
python main.py --log-output file --log-file c:/t/custom_log.log
```
