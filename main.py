from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config.constants import APP_VERSION, APP_NAME
from controller import users
from db_conn.connection import async_engine
from utility.logger.logger import logger
import uvicorn

# Create FastAPI app
app = FastAPI(title=APP_NAME, version=APP_VERSION)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this to restrict origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(users.router, prefix="/api", tags=["Users"])

# Startup event
@app.on_event("startup")
async def startup():
    """Run this on application startup"""
    logger.info("Starting FastAPI Application...")
    async with async_engine.begin() as conn:
        await conn.run_sync(lambda x: None)  # Dummy call to validate DB connection
    logger.info("Database connection successful!")

# Shutdown event
@app.on_event("shutdown")
async def shutdown():
    """Run this on application shutdown"""
    logger.info("Shutting down FastAPI Application...")

# Root endpoint
@app.get("/")
async def health_check():
    """Check if the API is running"""
    return {"message": "FastAPI is up and running 🚀"}

# Run the server
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
