from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI() # Create an instance of the FastAPI

'''
#@app --> path operation decorater
get --> operation
('/') --> Path
def index(): --> Path Operation Function
    return "something" 
'''

# @app.get('/') # But routes/endpoints/path should be different. Path is preferable
# def index(): # You can give any name to the function.
#     return {'data':'blog list'}


@app.get('/blog')  
def index(limit=10,published: bool=True, sort: Optional[str] = None):  
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}
    
@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    # Fetch blog with id = id
    return {'data': id}

@app.get('/blog/{id}/comments')
def comment(id, limit=10):
    # Fetch comments of blog with id = id
    return {'data': {'1','2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"Blog is created with title as {blog.title}"}
