"""
Master Node API
- Connects to (decentralized) db
- Fetches a node list
- /node_list
"""
import logging
from uuid import uuid4

from cerebro.api.controllers.node_list import get_node_list, create_node
from cerebro.api.models import ConnectionRequest
from fastapi import APIRouter

router = APIRouter()
logger = logging.getLogger(__name__)
node_identifier = str(uuid4()).replace("-", "")


@router.get("/list_node", tags=["Blockchain", "GET"])
async def fetch_node_list():
    # We run the proof of work algorithm to get the next proof...
    response = await get_node_list()
    return response


@router.post("/node", tags=["Blockchain", "POST"])
async def add_node(body: ConnectionRequest):
    response = await create_node(body["conn_id"], body["conn_url"])
    return response
