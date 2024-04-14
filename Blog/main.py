from .routers import blog, user, authentication
from .database import engine
from . import models
from fastapi import FastAPI

app = FastAPI()  # Create an instance of the FastAPI


app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog.router)

# My Starting code is below:
# from typing import List
# from fastapi import HTTPException
# from fastapi import status
# from fastapi import FastAPI,Depends,status,Response,HTTPException
# from . import schemas,models
# from .database import engine, SessionLocal
# from sqlalchemy.orm import Session
# from .hashing import Hash
# from routers import blog

# app = FastAPI()  # Create an instance of the FastAPI

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# models.Base.metadata.create_all(engine)

# @app.post('/blog',status_code=status.HTTP_201_CREATED, tags=['blogs'])
# def create(request:schemas.Blog, db:Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# # Way 1:
# @app.delete('/blog/{id}',
#             status_code=status.HTTP_204_NO_CONTENT,
#             tags=['blogs'])
# def destroy(id,db: Session = Depends(get_db)):
#     db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
#     db.commit()
#     return "done" # Since we are using HTTP_204_NO_CONTENT it is not returning anything


# # Way 2:
# # @app.delete('/blog/{id}', status_code=status.HTTP_200_OK)
# # def destroy(id, db: Session = Depends(get_db)):
# #     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
# #     if blog:
# #         db.delete(blog)
# #         db.commit()
# #         return {'detail': f"Blog with id {id} has been deleted"}
# #     else:
# #         raise HTTPException(
# #             status_code=status.HTTP_404_NOT_FOUND,
# #      detail=f"Blog with id {id} not found")

# # Way 1:
# # @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
# # def update(id, request:schemas.Blog,db: Session = Depends(get_db)):
# #     db.query(models.Blog).filter(models.Blog.id == id).update(
# #         {"title": request.title, "body": request.body}
# #     )  # **passed each field in a dict**

# #     db.commit()

# #     return "Record with id {id} updated successfully!"

# # Way 2:
# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
# def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if blog:
#         blog.title = request.title
#         blog.body = request.body
#         db.commit()
#         return f"Record with id {id} updated successfully!"
#     else:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with id {id} is not found")

    
# @app.get('/blog', response_model=List[schemas.ShowBlog], tags=['blogs'])
# def all(db: Session=Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


# @app.get('/blog/{id}', status_code=status.HTTP_200_OK,
#          response_model=schemas.ShowBlog, tags=['blogs'])
# def show(id,response:Response,db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         # Way 2:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Blog with the given id:{id} is not found")
#         # Way 1:
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'detail':f"Blog with the given id:{id} is not found"}
#     return blog
   

# @app.post('/user', response_model=schemas.ShowUser, tags=['users'])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     new_user = models.User(name=request.name, email=request.email,password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @app.get('/user/{id}', response_model=schemas.ShowUser, tags=['users'])
# def get_user(id, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         # Way 2:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"User with the given id:{id} is not found")
#         # Way 1:
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'detail':f"Blog with the given id:{id} is not found"}
#     return user
