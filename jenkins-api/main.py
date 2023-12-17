from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from requests.auth import HTTPBasicAuth
import requests
import jenkins

app = FastAPI()

# Replace these variables with your Jenkins server details
jenkins_url = 'http://localhost:8080'
username = 'admin'
password = '203c177f49be4b639d2fa47174f4c8eb'

server = jenkins.Jenkins(jenkins_url, username=username, password=password)

# Endpoint to test if working 
@app.get("/")
def home():
    user = server.get_whoami()
    version = server.get_version()
    return {'message': f'Hello {user["fullName"]} from Jenkins {version}'}