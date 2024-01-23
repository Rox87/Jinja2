### RUNNING
# poetry run uvicorn WrapperFunction.jinja:app

### TIPS
# *******************************
# p/ adicionar várias rotas de uma vez na FASTAPI

# routes.py

# --------
# from fastapi import APIRouter

# router = APIRouter()

# @router.get("/ping")
# async def ping_check():
#     return {"msg": "pong"}
# ...
# --------
# app.include_router(routes.router,prefix="/api")