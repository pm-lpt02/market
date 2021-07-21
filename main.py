from fastapi import FastAPI
from models import symbols, exchanges, gics
from routers import symbolRouter, gicsRouter, exchangeRouter
from databases import engine


app = FastAPI()

symbols.Base.metadata.create_all(engine)
exchanges.Base.metadata.create_all(engine)
gics.Base.metadata.create_all(engine)

app.include_router(symbolRouter.router)
app.include_router(gicsRouter.router)
app.include_router(exchangeRouter.router)
