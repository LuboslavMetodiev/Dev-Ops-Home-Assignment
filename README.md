# Intro
This is a practice implementation for a homework assgment.  
The assigment is described [here](https://github.com/devops-pragmatic/web-app-challenge).  
It is using Docker containers to run Python environment and redis.  
1. What is done in Python environment:
- Uses Flask to host a site with 3 urls: /, /visited, /health
2. Redis is used for:
- to count the visits to /visited url.
  
On pull request workflow should be executed. It is located in  .github/workflows/test.yml
  
# How to run the site localy
### Software Requirements:
- Docker 
- Docker Compose

1. Make sure Docker engine is running
2. Download and store files localy
3. Open terminal or Visual studio code
4. Navigate to the folder where the files were sored
5. Run:  
```
docker-compose up --build -d 
```
Docker containers should be pulled and started
You can access the sites on (localhost:8000) (localhost:8000/visited) (localhost:8000/health)
