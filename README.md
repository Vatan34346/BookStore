# BookStore

Set up:
WITH DOCKER:
1) download repository.
2) navigate to project folder
3) use terminal in project (so: /path/project_name)
4) write in terminal: docker build . 
5) copy created image id (you can check images by docker images)
6) docker run  -d -p [you port(any)]:8000  [image_id] (in project i am using .env file but also i have default values so you we dont need to pass env vars to run script)
7) go to browser localhost:8000/docs here we have api documentation

WITH DOWNLOADED REPO:
1) donload repo from github
2) navigate to repository location
3) create vertuala env by writing in terminal: python -m venv venv
4) activate vertual invironment venv\Scripts\activate
5) in tetrminal: pip install -r requirements.txt
6) go to main.py file click start or in terminal write: python main.py
7) go to browser localhost:8000/docs here we have api documentation


BOOKSTORE API:

So in project i have jwt-auth.

WHAT WE NEED TO DO TO USE API:
1) go to Authentification section
2) click register
3) enter click try out
4) enter data in request body. 
5) click execute (Now we have already created user)
6) now in same Authentification section click on login and enter user data in request body
7) click execute
8) in response body we have {
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOnsiaWQiOjEsImVtYWlsIjoicGFhdGFAZ21haWwuY29tIiwicGFzc3dvcmQiOiIkMmIkMTIkNUVWQVROUEx2QjZ4T3cvU3phTEdTLjJGejlkNXRTcTlGOVBLN1h1ZGZZY2xoQTZhVTJwZ0ciLCJuYW1lIjoicGF0YSJ9LCJleHBpcnkiOjE2OTYxODAzNjYuMzUzODkwN30.XuBi2Gp19G2Sm8p7iOaiepwzQRfutxuMFLTaaxKXKrM",
  "token_type": "bearer"
   }
9) copy access_token without "" symbol
10) it should look like: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOnsiaWQiOjEsImVtYWlsIjoicGFhdGFAZ21haWwuY29tIiwicGFzc3dvcmQiOiIkMmIkMTIkNUVWQVROUEx2QjZ4T3cvU3phTEdTLjJGejlkNXRTcTlGOVBLN1h1ZGZZY2xoQTZhVTJwZ0ciLCJuYW1lIjoicGF0YSJ9LCJleHBpcnkiOjE2OTYxODAzNjYuMzUzODkwN30.XuBi2Gp19G2Sm8p7iOaiepwzQRfutxuMFLTaaxKXKrM
11)    Now scroll up
12)in top right corner you will see Authorize button.(click on it)
13) past access_token
14) click Authorize
15) and close (click X or Close button)
16) Now we can you api
   

