import logging

import pymongo
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from cerebro.api import router as api_router
from cerebro.api.db import close_mongo_connection, connect_to_mongo, get_nosql_db
from cerebro.config import config

app = FastAPI()
logger = logging.getLogger(__name__)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # can alter with time
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()
    client = await get_nosql_db()
    db = client[config.db_name]
    try:
        db.create_collection("master_node_conn_list")
    except pymongo.errors.CollectionInvalid as e:
        logging.warning(e)
        pass
    try:
        master_node_conn_list = db.master_node_conn_list
        master_node_conn_list.create_index("conn_url", name="conn_url", unique=True)
    except pymongo.errors.CollectionInvalid as e:
        logging.warning(e)
        pass


@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()


app.include_router(api_router, prefix="/api")
