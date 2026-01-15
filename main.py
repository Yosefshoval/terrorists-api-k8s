from fastapi import FastAPI, UploadFile, HTTPException, status
import pandas as pd
from tenacity import retry_if_exception

import db
import models
# import db

""" This file is to router, get the file and forward it to models to process it. Then return message. """


app = FastAPI()

@app.post('/top-threats')
def post_terrorists_file(file: UploadFile):
    if not file:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"detail": "No file provided"})

    if not file.filename.lower().endswith(('.csv', ".xlsx", ".xls")):
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={'detail': 'Invalid CSV file'})

    try:
        df = pd.read_csv(file.file)
        sorted_df = models.sort_file(df)

    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail={'detail': str(e)})

    try: top = models.clean_top_5(sorted_df)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail={'detail': str(e)})

    if not top: return HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        detail={'detail': 'Not content valid to save in MongoDB'})

    try:
        client = db.client_connection()
        collection = db.get_collection(client)
        is_saved = db.save_documents(collection, top)

        if not is_saved: raise Exception('Database unavailable')
        return {'message': 'is_saved', 'top 5': top}

    except Exception as e:
        return HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail={'detail': str(e)})




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app='main:app',
        host='0.0.0.0',
        port=8000,
        reload=True
    )