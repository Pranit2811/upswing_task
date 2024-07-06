from fastapi import FastAPI, status, Query, Depends
from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime
from fastapi.responses import JSONResponse
from pymongo import MongoClient



app = FastAPI()

client = MongoClient('mongodb+srv://pranitraut8625:VMraAerXKOwFa179@cluster0.386qnbl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['upswing_report']
collection = db['upswing']



class Daterange(BaseModel):
    start_date : Optional[datetime] = Query(None, description="Start date in YYYY-MM-DD format")
    end_date : Optional[datetime] = Query(None, description="End date in YYYY-MM-DD format")

@app.get("/status/")
def get_count(dates: Daterange= Depends()):
    start_date = dates.start_date.strftime("%Y-%m-%d %H:%M:%S")
    end_date = dates.end_date.strftime("%Y-%m-%d %H:%M:%S")
    query = {
	"timestamp": {
		"$gte": start_date,
		"$lte": end_date
	}
}
    count = collection.count_documents(query)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"total_message_count":count})


