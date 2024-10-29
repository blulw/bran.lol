from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse

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


@app.get("/bio")
async def bio():
    return RedirectResponse("https://e-z.bio/bran")


@app.get("/{path:path}")
async def catch_all(path: str):
    return FileResponse("templates/404.html")


def main() -> None:
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
