from pydantic import BaseModel
from typing import List

class PMRequest(BaseModel):
    features: List[float]
