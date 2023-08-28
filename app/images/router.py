from fastapi import APIRouter, UploadFile
import shutil

router = APIRouter(
    prefix="/images",
    tags=["Upload images"]
)


@router.post("/hotel")
async def add_hotel_image(name: int, file: UploadFile):
    print(file.filename)
    with open(f"app/static/images/{name}.webp", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    return
