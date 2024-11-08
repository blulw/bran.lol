from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
import httpx
import urllib.parse

app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Request: {request.method} {request.url}")
    response = await call_next(request)
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
async def success(filename: str = "filename"):

    safe_filename = urllib.parse.quote(filename)

    html_content = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Comic+Neue:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700&display=swap" rel="stylesheet">
            <link rel="icon" href="https://media.bran.lol/favicon.ico">
            <link rel="stylesheet" href="/static/styles.css">
            <meta content="File Upload Success" property="og:title" />
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


@app.get("/file/{filename}", response_class=HTMLResponse)
async def fetch_user_file(filename: str):
    decoded_filename = urllib.parse.unquote(filename)
    file_url = f"https://api.bran.lol/userfiles/{decoded_filename}"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(file_url)

        if response.status_code == 200:
            content_length = response.headers.get("Content-Length")
            if content_length is not None:
                file_size = int(content_length)
                if file_size >= 1024 ** 3:
                    formatted_size = f"{file_size / 1024 ** 3:.2f} GB"
                elif file_size >= 1024 ** 2:
                    formatted_size = f"{file_size / 1024 ** 2:.2f} MB"
                elif file_size >= 1024:
                    formatted_size = f"{file_size / 1024:.2f} KB"
                else:
                    formatted_size = f"{file_size} bytes"
            else:
                formatted_size = "Unknown size"

            html_content = f"""
            <html>
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <meta property="og:title" content="{decoded_filename} - bran.lol" />
                    <meta property="og:description" content="File: {decoded_filename}&#10;File Size: {formatted_size}" />
                    <meta property="og:image" content="{file_url}" />
                    <meta property="og:url" content="https://bran.lol/" />
                    <meta name="twitter:card" content="summary_large_image" />
                    <title>{decoded_filename}</title>
                    <link rel="stylesheet" href="/static/styles.css">
                    <link rel="icon" href="https://media.bran.lol/favicon.ico">
                    <style>
                        body {{
                            
                            text-align: center;
                            color: black;
                            margin: 0;
                            padding: 20px;
                        }}
                        h1 {{
                            margin-top: 20px;
                        }}
                        p {{
                            margin: 10px 0;
                        }}
                        a {{
                            display: inline-block;
                            margin: 20px 0;
                            padding: 10px 20px;
                            color: #1a1a1a;
                            text-decoration: none;
                            background-color: #fafafa;
                            border-radius: 5px;
                        }}
                        a:hover {{
                            background-color: #a6a6a6;
                        }}
                        #img-container {{
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            overflow: hidden;
                            padding: 10px;
                            box-sizing: border-box;
                            margin: 0 auto;
                        }}
                        #img-container img {{
                            max-width: 60%;
                            max-height: 40%;
                            width: auto;
                            height: auto;
                            display: block;
                        }}
                        @media (max-width: 768px) {{
                            #img-container {{
                                max-height: 60vh;
                            }}
                        }}
                    </style>
                </head>
                <body>
                    <img src="https://media.bran.lol/bg.gif" id="backvid">
                    <h1>{decoded_filename}</h1>
                    <p>File size: {formatted_size}</p>
                    <a href="{file_url}" download="{decoded_filename}">Download</a>
                    <div id="img-container">
                        <img src="{file_url}" alt="{decoded_filename}"/>
                    </div>
                </body>
            </html>
            """
            return HTMLResponse(content=html_content, status_code=200)
        else:
            return FileResponse("templates/404.html")

    except httpx.RequestError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving file from api.bran.lol: {str(e)}"
        )


# This should be the last route


@ app.get("/{path:path}")
async def catch_all(path: str):
    return FileResponse("templates/404.html")


def main() -> None:
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
