from uvicorn import Config, Server
import asyncio
from app import App
from config_manager import ConfigManager
from logger import get_logger

logger = get_logger(__name__)

async def main():
    # Initialize the logger with the specified output and file name
    logger.info("main: started..")
    config_manager = ConfigManager()
    config_manager.override_with_env_vars()  # Override config with env vars before loading
    config = config_manager.get_config()

    if config is not None:
        api_config = config.get("api", {})
        api_host = api_config.get("host", "127.0.0.1")
        api_port = api_config.get("port", "9000")
        logger.info(f"main: Computed host/port: {api_host}:{api_port}")
        myapp = App(config_manager)
        config = Config(app=myapp, host=api_host, port=int(api_port))
        server = Server(config)
        try:
            logger.info("main: started listening..")
            await server.serve()
        except asyncio.CancelledError as e:
            print("Application Cancelled to stop..")
            await myapp.graceful_shutdown()
        except Exception as e:  # Catch all other exceptions here
            print(f"ERROR at main: {e}")
            logger.error(f"ERROR at main: {e}")
            await myapp.graceful_shutdown()
    else:
        print("ERROR at main: Application didn't start. Config.json is not found or parser error")
        logger.error(f"ERROR at main: Application didn't start. Config.json is not found or parser error")

    logger.info("main: completed..")

if __name__ == "__main__":
    print("Process: Started..")
    logger.info("Process: Started..")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Application stopped by user (Ctrl+C).")
        logger.info("Application stopped by user (Ctrl+C).")
        print("Shutdown complete.")
        logger.info("Shutdown complete.")
    except Exception as e:  # Catch all other exceptions here
        print(f"ERROR at root: {e}")
        logger.error(f"ERROR at root: {e}")
    print("Process: Stopped.")
    logger.info("Process: Stopped.")