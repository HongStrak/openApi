from fastapi import FastAPI, WebSocket, Request, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from apis import ml_tools


app = FastAPI()


app.include_router(ml_tools.router, tags=['ml_tools'], prefix='/ml/tools')
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)
