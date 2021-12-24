from fastapi import FastAPI
from database.schemas import postSchema

posts=[
	{
	'id':1,
	'title':'title 1',
	'body':'thfebwuuuuuihfoe'
	},
	{
	'id':2,
	'title':'title 2',
	'body':'iuawieufnhwi'
	},
	{
	'id':3,
	'title':'title 3',
	'body':'aiusdiwudbksjc'
	},
	
]

app = FastAPI()

@app.get("/posts")
def get_all_posts():
	return {'posts':posts}

@app.get("/post/{id}")
def get_post(id:int):
	
	for post in posts:
		if post["id"]==id:
			return {'post':post}

	return {"info":"not found"}

		

@app.post("/post")
def add_post(post:postSchema):
	post.id = len(posts)+1
	posts.append(post.dict())
	return {
	"info":"post added"
	}

@app.put("/post/{id}")
def update_post(id:int, post:postSchema):
	for p in posts:
		if p["id"]==id:
			p["title"]=post.title
			p["body"]=post.body
			return {
				"info":"post updated"
			}
	return {"info":"not found"}


@app.delete("/post/{id}")
def delete_post(id:int):
	for p in posts:
		if p["id"]==id:
			posts.remove(p)
			return {"info":"post deleted"}

	return {"info":"not found"}