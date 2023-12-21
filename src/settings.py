"""
    This file includes all the configuration file for API
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Handles documentation title
app = FastAPI(
    version="version 1.0.0",
    title="Recipe Calculator",
    description="API helper to interact with the CV Parser",
    debug=True,
    docs_url="/",
    redoc_url=None,
)

# Handles cors
origins = ["http://0.0.0.0:7860"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
