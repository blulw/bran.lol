from fastapi import FastAPI, HTTPException, Response, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse, HTMLResponse
import httpx
import urllib.parse

app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    print(f"Response: {response.status_code}")
    return response

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


@app.post("/success", response_class=HTMLResponse)
async def success(filename: str):
    safe_filename = urllib.parse.quote(filename)

    html_content = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Comic+Neue:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700&display=swap" rel="stylesheet">
            <link rel="icon" href="favicon.ico">
            <link rel="stylesheet" href="/static/styles.css">
            <meta content="Page not found" property="og:title" />
            <meta content="This page does not exist" property="og:description" />
            <meta content="https://bran.lol/" property="og:url" />
            <meta content="https://media.bran.lol/glaive.png" property="og:image" />
            <meta content="#B4B4B4" data-react-helmet="true" name="theme-color" />
        </head>
        <body>
            <img src="https://media.bran.lol/bg.gif" id="backvid" alt="Background Video">
            File name: {filename} <br>
            <button id="copyLinkButton">Copy Link</button>

            <script>
                document.getElementById('copyLinkButton').addEventListener('click', function() {{
                    const filename = "{safe_filename}";
                    const link = "https://bran.lol/file/" + filename;
                    navigator.clipboard.writeText(link)
                        .then(() => {{
                            alert('Link copied to clipboard: ' + link);
                        }})
                        .catch(err => {{
                            console.error('Error copying link: ', err);
                        }});
                }});
            </script>
        </body>
        <style>
          body {{
              background-color: #1a1a1a;
              font-size: 2rem;
              text-align: center;
              margin-top: 25%;
          }}
        </style>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/file/{filename}")
async def fetch_user_file(filename: str):
    decoded_filename = urllib.parse.unquote(filename)

    file_url = f"https://api.bran.lol/userfiles/{decoded_filename}"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(file_url)

        if response.status_code == 200:
            return Response(
                content=response.content,
                media_type=response.headers.get(
                    "content-type", "application/octet-stream"),
                headers={
                    "Content-Disposition": f"inline; filename={decoded_filename}"}
            )
        else:
            return FileResponse("templates/404.html")

    except httpx.RequestError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving file from api.bran.lol: {str(e)}"
        )


@app.get("/{path:path}")
async def catch_all(path: str):
    return FileResponse("templates/404.html")


def main() -> None:
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
