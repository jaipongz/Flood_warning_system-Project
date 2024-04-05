import requests
import json
from fastapi import APIRouter 

from server.models.water import (
    ErrorResponseModel,
    ResponseModel,
)

router = APIRouter()

@router.get("/{id}", response_description="water data retrieved")
async def get_mockup_data(id):
    url = 'http://192.168.1.3:7078/'#+str(id)
    url = 'https://jsonplaceholder.typicode.com/albums'#/'+str(id)
    mockup = requests.get(url)
    if mockup:
        print(json.loads(mockup.text))
        return ResponseModel(str(mockup.text), "API data id:" +str(id) +" retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "data doesn't exist.")