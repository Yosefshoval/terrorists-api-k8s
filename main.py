from fastapi import FastAPI
import models
import db

""" This file is to router, get the file and forward it to models to process it. Then return message. """


app = FastAPI()

@app.post('/top-threats')
def post_terrorists_file():
    # Flow:
    csv = file
    models.validate_file(csv)
    models.clean_file(csv)
    db.save_file(csv)
    return {'message'}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app=app,
        host='0.0.0.0',
        port=8000
    )