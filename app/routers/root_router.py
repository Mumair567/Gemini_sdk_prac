from fastapi import FastAPI, APIRouter,HTTPException

root_route=APIRouter(tags=["Home"])
@root_route.get("/")
def read_root():
    try:
        return(
            {"status_code":200,
            "message" : "welcome to our site "
            }
        )
    except Exception:
        raise HTTPException(status_code=500,detail="Internal server Error")