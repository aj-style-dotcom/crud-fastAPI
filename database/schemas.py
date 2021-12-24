from pydantic import BaseModel


class postSchema(BaseModel):
	id:int
	title:str
	body:str