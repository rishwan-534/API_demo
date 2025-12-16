from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 1. Define the data structure (Optional but recommended in FastAPI)
class User(BaseModel):
    username: str
    password: str

# 2. A Simple GET Endpoint
@app.get("/status")
def get_status():
    return {
        "status": "Running",
        "framework": "FastAPI",
        "speed": "Super Fast"
    }

# 3. A Simple POST Endpoint
@app.post("/login")
def login_user(user: User):
    # FastAPI automatically validates that 'user' contains a username and password
    if user.username == "admin" and user.password == "1234":
        return {"message": "Login Successful", "token": "FAST-API-TOKEN"}
    else:
        # Built-in error handling
        raise HTTPException(status_code=401, detail="Invalid Credentials")