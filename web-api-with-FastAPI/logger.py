import argparse
import logging
from logging.handlers import TimedRotatingFileHandler

#default_log = "console"
default_log = "file"
default_log_file_path = "app-log.log"

def parse_arguments():
    parser = argparse.ArgumentParser(description="Specify log output destination and file name.")
    parser.add_argument("--log-output", choices=["file", "console"], default=default_log,
                        help="Specify whether logs go to a file or console.")
    parser.add_argument("--log-file", type=str, default=default_log_file_path,
                        help="Specify the log file path and name (used only if output is 'file').")
    return parser.parse_args()

def get_logger(name):
    args = parse_arguments()
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if args.log_output == "file":
        # Create a TimedRotatingFileHandler to rotate logs daily
        handler = TimedRotatingFileHandler(args.log_file, when="d", interval=1, backupCount=90)
    elif args.log_output == "console":
        # Create a StreamHandler for console logging
        handler = logging.StreamHandler()
    else:
        raise ValueError("Invalid output option. Use 'file' or 'console'.")

    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s"))
    logger.addHandler(handler)

    return logger