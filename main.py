from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config.constants import APP_VERSION, APP_NAME
from controller import users
from db_conn.connection import async_engine
from middleware.exception_handler import add_exception_handlers
from utility.logger.logger import logger
import uvicorn

# Create FastAPI app
app = FastAPI(title=APP_NAME, version=APP_VERSION)

# Include Routers
app.include_router(users.router, prefix="/api", tags=["Users"])

# Include Middleware e.g. Global Exception, Custom Exception, Authentication, Rate Limiting, PreSet Headers, CORS etc.
add_exception_handlers(app)

# Startup event
@app.on_event("startup")
@logger.execution_timer
async def startup():
    """Run this on application startup"""
    logger.info("Starting FastAPI Application...")
    async with async_engine.begin() as conn:
        await conn.run_sync(lambda x: None)  # Dummy call to validate DB connection
    logger.info("Database connection successful!")

# Shutdown event
@app.on_event("shutdown")
@logger.execution_timer
async def shutdown():
    """Run this on application shutdown"""
    logger.info("Shutting down FastAPI Application...")

# Root endpoint
@app.get("/")
@logger.execution_timer
async def health_check():
    """Check if the API is running"""
    return {"message": "FastAPI is up and running 🚀"}

# Run the server
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
