from fastapi import FastAPI, Response, status, HTTPException
import random
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/api/text-prompts')
async def textPrompts():
    random_value = [ "text1", "text2", "text3", "text4", "text5"]
    num = random.randint(0, len(random_value))
    return({"text-prompts": random_value[num-1]})


handler = Mangum(app)

def lambda_handler(event, context):
    context.callbackWaitsForEmptyEventLoop = False
    if event.get("source") == "serverless-plugin-warmup":
        return {}
    return handler(event, context)

