# Question 01

# from fastapi import FastAPI, Response

# app = FastAPI()

# @app.get('/')
# def read_root():
#     return "Bienvenue Valeria !"

# @app.get('/ping')
# def ping():
#     return Response(content="pong", media_type="text/plain")

# if __name__ == '__main__':
#     import uvicorn


# Question 02
# from fastapi import FastAPI, Response
# from fastapi.responses import HTMLResponse

# app = FastAPI()

# @app.get('/ping')
# def ping():
#     return Response(content="pong", media_type="text/plain")

# @app.get('/home', response_class=HTMLResponse)
# def home():
#     html_content = """
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Home</title>
#     </head>
#     <body>
#         <h1>Welcome home!</h1>
#     </body>
#     </html>
#     """
#     return html_content

# if __name__ == '__main__':
#     import uvicorn

# Question 03

# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse, PlainTextResponse
# from fastapi.exceptions import HTTPException as StarletteHTTPException

# app = FastAPI()

# @app.exception_handler(StarletteHTTPException)
# async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
#     if exc.status_code == 404:
#         html_content = """
#         <!DOCTYPE html>
#         <html>
#         <head>
#             <title>404 Not Found</title>
#         </head>
#         <body>
#             <h1>404 NOT FOUND</h1>
#         </body>
#         </html>
#         """
#         return HTMLResponse(content=html_content, status_code=404)

#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# @app.get('/ping')
# def ping():
#     return PlainTextResponse(content="pong", media_type="text/plain")

# @app.get('/home', response_class=HTMLResponse)
# def home():
#     html_content = """
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Home</title>
#     </head>
#     <body>
#         <h1>Welcome home!</h1>
#     </body>
#     </html>
#     """
#     return html_content

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8800)


# Question 04

# from fastapi import FastAPI, Request, status
# from fastapi.responses import HTMLResponse, PlainTextResponse
# from fastapi.exceptions import HTTPException as StarletteHTTPException
# from pydantic import BaseModel
# from typing import List
# from datetime import datetime

# app = FastAPI()


# class Post(BaseModel):
#     author: str
#     title: str
#     content: str
#     creation_datetime: datetime

# posts_db: List[Post] = [
#     Post(author="Valeria", title="La vie", creation_datetime=datetime(2025, 7, 25, 10, 0, 0), content="Parle de la vie"),
#     Post(author="Nambinintsoa", title="Le bien", creation_datetime=datetime(2025, 7, 25, 11, 30, 0), content="Parle du bien")
# ]


# @app.exception_handler(StarletteHTTPException)
# async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
#     if exc.status_code == 404:
#         html_content = """
#         <!DOCTYPE html>
#         <html>
#         <head>
#             <title>404 Not Found</title>
#         </head>
#         <body>
#             <h1>404 NOT FOUND</h1>
#         </body>
#         </html>
#         """
#         return HTMLResponse(content=html_content, status_code=404)
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)



# @app.get('/ping')
# def ping():
#     return PlainTextResponse(content="pong")

# @app.get('/home', response_class=HTMLResponse)
# def home():
#     html_content = """
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Home</title>
#     </head>
#     <body>
#         <h1>Welcome home!</h1>
#     </body>
#     </html>
#     """
#     return html_content
# @app.get("/posts")
# def get_posts():

#     return posts_db


# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(posts: List[Post]):
 
#     posts_db.extend(posts)
#     return posts_db


# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8800, reload=True)

# Question 06

# from fastapi import FastAPI, Request, status, HTTPException
# from fastapi.responses import HTMLResponse, PlainTextResponse
# from fastapi.exceptions import HTTPException as StarletteHTTPException
# from pydantic import BaseModel
# from typing import List, Optional
# from datetime import datetime

# app = FastAPI()

# class Post(BaseModel):
#     author: str
#     title: str
#     content: str
#     creation_datetime: datetime
#     last_update_datetime: Optional[datetime] = None

# posts_db: List[Post] = []


# @app.exception_handler(StarletteHTTPException)
# async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
#     if exc.status_code == 404:
#         html_content = """
#         <!DOCTYPE html>
#         <html>
#         <head>
#             <title>404 Not Found</title>
#         </head>
#         <body>
#             <h1>404 NOT FOUND</h1>
#         </body>
#         </html>
#         """
#         return HTMLResponse(content=html_content, status_code=404)
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# @app.get('/ping')
# def ping():
#     return PlainTextResponse(content="pong")

# @app.get('/home', response_class=HTMLResponse)
# def home():
#     html_content = """
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Home</title>
#     </head>
#     <body>
#         <h1>Welcome home!</h1>
#     </body>
#     </html>
#     """
#     return html_content


# @app.get("/posts")
# def get_posts():
 
#     return posts_db

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(posts: List[Post]):

#     posts_db.extend(posts)
#     return posts_db

# @app.put("/posts", status_code=status.HTTP_200_OK)
# def update_or_create_post(post: Post):
  
#     for index, existing_post in enumerate(posts_db):
#         if existing_post.title == post.title:
#             posts_db[index] = post
#             posts_db[index].last_update_datetime = datetime.now()
#             return posts_db[index]
    
#     posts_db.append(post)
#     return post

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8800, reload=True)