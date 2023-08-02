# from app import create_app
import uvicorn

from app import create_app
import config 

app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, port=int(config["PORT"]))