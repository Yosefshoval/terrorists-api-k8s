from pandas import DataFrame
from pydantic import BaseModel, Field
from typing import Annotated, Optional

""" This file get csv file from fastapi, process it via Pandas, and forward it to db.py for saving in mongodb.  """

class Terrorist(BaseModel):
    name: str = Annotated[str, Field(...)]
    location: str = Annotated[str, Field(...)]
    danger_rate: int = Annotated[int, Field(int, le=10, ge=0)]



def sort_file(file: DataFrame):
    file.sort_values(by='danger_rate', ascending=True)
    top_5 = file.head(5)
    return top_5



def clean_top_5(df: DataFrame):
    df = df['name', 'location', 'danger_rate']

    for terrorist in df:
        try:
            Terrorist(**terrorist)
        except:
            continue

    length = len(df)
    if not length:
        return False

    return {
        'count' : length,
        'top':list(df)
            }
