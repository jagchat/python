from fastapi import FastAPI
import asyncio
from logger import get_logger

class App:
    def __init__(self, config_loader):
        self.logger = get_logger(__name__)
        self.logger.info("App.init: Started..")
        self.config_loader = config_loader
        self.theapp = FastAPI()
        self.setup_routes()
        self.logger.info("App.init: Completed")

    def setup_routes(self):
        self.logger.info("App.setup_routes: Started..")

        # Define routes
        @self.theapp.get("/")
        async def read_root():
            self.logger.info("App.read_root: Started..")
            try:
                self.logger.info("App.read_root: Completed..")
                return {"Hello": "World"}
            except Exception as e:  # Catch all other exceptions here
                print(f"ERROR at App.read_root: {e}")
                self.logger.error(f"ERROR at App.read_root: {e}")

        self.logger.info("App.setup_routes: Completed")

    async def __call__(self, scope, receive, send): #essential for uvicorn ASGI compliance
        await self.theapp(scope, receive, send)

    async def graceful_shutdown(self):
        self.logger.info("App.graceful_shutdown: Started..")
        print("Shutting down gracefully...")
        await asyncio.sleep(1)  # Simulate a short delay for cleanup
        print("Gracefully Shutdown")
        self.logger.info("App.graceful_shutdown: Completed..")