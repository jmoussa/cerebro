from fastapi import APIRouter

from cerebro.api.master_node import router as master_node_router 

router = APIRouter()
router.include_router(master_node_router)