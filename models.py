from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., example="Evangelista")
    age: int = Field(..., example=24)