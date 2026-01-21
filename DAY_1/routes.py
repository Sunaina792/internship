from fastapi import APIRouter, HTTPException
from schema import item
from db import items_collection

router = APIRouter()

# create
@router.post("/items")
async def create_items(item: item):
    await items_collection.insert_one(item.dict())
    return { "msg": "Item added", "item": item}

# read(all)
@router.get("/items")
async def get_items():
    items = []
    async for item in items_collection.find():
        item["_id"] = str(item["_id"])
        items.append(item)
    return items

@router.get("/items/{name)")
async def get_item_by_name(name: str):
    item = await items_collection.find_one({"name": name})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")   
    
    item["_id"] = str(item["_id"])
    return item



@router.put("/items/{name}")
async def update_item(name: str, item: item):
    result = await items_collection.update_one(
        {"name": name},
        {"$set": item.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"msg": "Item updated successfully"}

@router.delete("/items/{name}")
async def delete_item(name: str):
    result = await items_collection.delete_one({"name": name})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"msg": "Item deleted successfully"}
