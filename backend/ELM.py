from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

# Mount the 'static' directory at the '/static' route.
app.mount("/static", StaticFiles(directory="D:/PROJECT/Newfolder/its/backend/static"), name="static")

@app.get("/{filename}")
async def get_image(filename: str):
    file_path = Path(f"D:/PROJECT/Newfolder/its/backend/static/{filename}")
    if not file_path.is_file():
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(file_path)