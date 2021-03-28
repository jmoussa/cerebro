import logging

from cerebro.api.db import get_nosql_db
from cerebro.api.utils import format_ids
from cerebro.config import config

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


async def create_node(conn_id, conn_url):
    client = await get_nosql_db()
    db = client[config.db_name]
    collection = db.master_node_conn_list
    node = {"conn_id": conn_id, "conn_url": conn_url}
    try:
        response = collection.insert_one(node)
        block = collection.find({"_id": {"$in": [response.inserted_id]}})
        return {"status_code": 200, "block": block}
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        logging.error(f"Exception\n{message}")
        return {"status_code": 400, "id_inserted": None}
