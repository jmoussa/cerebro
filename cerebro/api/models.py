from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId


class NodeList(BaseModel):
    conn_id: str
    conn_url: str


class NodeListInDB(NodeList):
    _id: ObjectId
    date_created: datetime = Field(default_factory=datetime.utcnow)
