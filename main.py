from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="test test for free deplotment", description="free deployment")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/")
async def root():
    return JSONResponse({"message":"root api"})

@app.get("/score")
async def score(line:int, wall:int, enter:int, red:int, green:int, yellow:int, blue:int, out:int, bingo:int, supuerbingo: int):
    if red > 2 or green > 4 or yellow > 4 or blue > 10:
        return JSONResponse("Exceeding the amount")
    result = 0
    if line > 0:
        result += 50
    if wall > 0:
        result += 50
    if enter > 0:
        result += 10
    result += (red * 20) + (green * 5) + (yellow * 5) + blue
    if out > 0:
        result += 10
    if bingo > 0:
        result += 100
    if supuerbingo > 0:
        result += 100
    return JSONResponse({"result":f"{str(result)}"})