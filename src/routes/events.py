from fastapi import APIRouter

event_router = APIRouter(
    prefix="/events",
    tags=["Events"]
)

@event_router.get("/")
async def get_all_events():
    return []