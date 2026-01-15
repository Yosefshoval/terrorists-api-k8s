from pydantic import BaseModel, Field
from typing import Annotated, Optional

""" This file get csv file from fastapi, process it via Pandas, and forward it to db.py for saving in mongodb.  """

class Terrorist(BaseModel):
    name: str = Annotated[str, Field(...)]
    location: str = Annotated[str, Field(...)]
    danger_rate: int = Annotated[int, Field(int, le=10, ge=0)]
