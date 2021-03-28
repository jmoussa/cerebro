"""
Master Node API
- Connects to (decentralized) db
- Fetches a node list
- /node_list
"""
import logging
from uuid import uuid4
from fastapi import APIRouter
from cerebro.api.controllers.node_list import get_node_list

router = APIRouter()
logger = logging.getLogger(__name__)
node_identifier = str(uuid4()).replace("-", "")


@router.get("/node_list", tags=["Blockchain", "GET"])
async def fetch_node_list():
    # We run the proof of work algorithm to get the next proof...
    response = await get_node_list()
    return response
