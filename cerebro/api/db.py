# from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
import logging
from cerebro.config import config


# MongoDB
class MongoDB:
    # client: AsyncIOMotorClient = None
    client: MongoClient = None


db = MongoDB()


async def get_nosql_db() -> MongoClient:
    return db.client


async def connect_to_mongo():
    db.client = MongoClient(
        str(config.db_url),
        maxPoolSize=config.db_max_connections_count,
        minPoolSize=config.db_min_connections_count,
    )
    logging.info("connected to mongodb")


async def close_mongo_connection():
    db.client.close()
    logging.info("closed mongo connection")
