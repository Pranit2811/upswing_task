from fastapi import FastAPI, status, Query, Depends
import os
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from fastapi.responses import JSONResponse
from pymongo import MongoClient
import traceback
from config import get_config

CONFIG = get_config(os.getenv("ENV", "development"))

app = FastAPI()

client = MongoClient(CONFIG['MONGO_CLIENT'])
db = client[CONFIG['MONGO_DB']]
collection = db[CONFIG['MONGO_COLLECTION']]


class Daterange(BaseModel):
    start_date : Optional[datetime] = Query(None, description="Start date in YYYY-MM-DD format")
    end_date : Optional[datetime] = Query(None, description="End date in YYYY-MM-DD format")

@app.get("/status")
def get_count(dates: Daterange= Depends()):
    try:
        start_date = dates.start_date.strftime("%Y-%m-%d")
        end_date = dates.end_date.strftime("%Y-%m-%d")
        query = {
            	"timestamp": {
            		"$gte": start_date,
            		"$lte": end_date
            	}
            }
        count = collection.count_documents(query)
        return JSONResponse(status_code=status.HTTP_200_OK, content={"total_message_count":count})
    except Exception as e:
            traceback.print_exc()
            return {"status": "failed", "errors": "Contact administration for more info"},500

