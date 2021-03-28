from datetime import datetime

# from typing import List, Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class NodeList(BaseModel):
    conn_id: str
    conn_url: str


class NodeListInDB(NodeList):
    _id: ObjectId
    date_created: datetime = Field(default_factory=datetime.utcnow)


class ConnectionRequest(BaseModel):
    conn_id: str
    conn_url: str
