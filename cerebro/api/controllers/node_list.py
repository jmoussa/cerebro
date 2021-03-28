import json
import logging

from bson import ObjectId
from cerebro.api.db import get_nosql_db
from cerebro.api.models import NodeListInDB
from cerebro.config import config
from cerebro.api.utils import format_ids

logger = logging.getLogger(__name__)


async def get_node_list(filter_list: list = None):
    client = await get_nosql_db()
    db = client[config.db_name]
    collection = db.master_node_conn_list
    if filter_list is None:
        rows = collection.find()
    else:
        rows = collection.find({"conn_id": {"$in": filter_list}})

    row_list = []
    for row in rows:
        f_row = format_ids(row)
        row_list.append(f_row["conn_url"])
    return row_list
