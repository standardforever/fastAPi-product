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

@app.get('/api/negative-prompt')
async def textPrompts():
    random_value = [ "negative1", "negative2", "negative3", "negative4", "negative5"]
    num = random.randint(0, len(random_value))
    return({"negative-prompts": random_value[num-1]})


handler = Mangum(app)

def lambda_handler(event, context):
    context.callbackWaitsForEmptyEventLoop = False
    if event.get("source") == "serverless-plugin-warmup":
        return {}
    return handler(event, context)

