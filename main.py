from fastapi import FastAPI, HTTPException, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
import httpx

app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")


@app.get("/")
async def root():
    return FileResponse("templates/index.html")


@app.get("/py")
async def py():
    return FileResponse("templates/py.html")


@app.get("/keiran")
async def keiran():
    return FileResponse("templates/keiran.html")


@app.get("/bran")
async def bran():
    return FileResponse("templates/bran.html")


@app.get("/web")
async def web():
    return FileResponse("templates/web.html")


@app.get("/upload")
async def upload():
    return FileResponse("templates/upload.html")


@app.get("/bio")
async def bio():
    return RedirectResponse("https://e-z.bio/bran")


@app.get("/file/{filename}")
async def fetch_user_file(filename: str):
    file_url = f"https://api.bran.lol/userfiles/{filename}"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(file_url)

        if response.status_code != 200:
            return FileResponse("templates/404.html")

        return Response(
            content=response.content,
            media_type=response.headers.get(
                "content-type", "application/octet-stream"),
            headers={"Content-Disposition": f"inline; filename={filename}"}
        )

    except httpx.RequestError:
        raise HTTPException(
            status_code=500, detail="Error retrieving file from api.bran.lol.")

# This should be the last route


@app.get("/{path:path}")
async def catch_all(path: str):
    return FileResponse("templates/404.html")


def main() -> None:
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
