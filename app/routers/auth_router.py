from fastapi import FastAPI,HTTPException,APIRouter
from app.schemas.auth import SignUp,Login
from app.userdb.users import users,user_count

auth_router=APIRouter(prefix="/auth",tags=["Auth"])

@auth_router.post("/signup/")
def user_signup(user:SignUp):
    global user_count
    for u in users:
        if u["email"]==user.email:
            raise HTTPException(status_code=400,description="Email already exist ")
    new_user={
            "id":user_count,
            "full_name":user.full_name,
            "email"   : user.email,
            "age"     : user.age,
            "password": user.password
        }
    users.append(new_user)
    user_count+=1
    return{
        "id":new_user["id"],
        "full_name":new_user["full_name"],
        "email":new_user["email"],
        "age"  : new_user["age"],
        "message":" Welcome to our website"
    }

@auth_router.post("/login/")
def login_user(user:Login):
    found_user=None
    for u in users:
        if u["email"]==user.email:
            found_user=u
            break
        if not found_user:
            return HTTPException(status_code=404,description="user not found ")
        if u["password"]!=user.password:
            return HTTPException(status_code=404,description="incorrect password")
    return{
        "id":found_user["id"],
        "full_name":found_user["full_name"],
        "age"  : found_user["age"],
        "message": "welcome back"
    }