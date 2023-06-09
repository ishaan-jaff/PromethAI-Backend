from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
import os

from dotenv import load_dotenv
import logging
from typing import Dict, Any

from chains import Agent
import asyncio
import json

CANNED_RESPONSES=False

# Set up logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s [%(levelname)s] %(message)s",  # Set the log message format
)

logger = logging.getLogger(__name__)
from dotenv import load_dotenv


# def establish_connection():
#     AGENT_NAME = os.getenv("AGENT_NAME") or "my-agent"
#
#     agent = Agento(AGENT_NAME)
#     agent.createIndex()
#     return agent
load_dotenv()


app = FastAPI(debug=True)

class Payload(BaseModel):
    payload: Dict[str, Any]

class ImageResponse(BaseModel):
    success: bool
    message: str

@app.get("/")
async def root():
    return {"message": "Hello, World, I am alive!"}



@app.post("/prompt-to-choose-meal-tree", response_model=dict)
async def prompt_to_choose_meal_tree(request_data: Payload) -> dict:
    if CANNED_RESPONSES:
        with open('fixtures/choose_meal_tree_response.json', 'r') as f:
            json_data = json.load(f)
            stripped_string_dict = {"response": json_data}
            return JSONResponse(content=stripped_string_dict)


    json_payload = request_data.payload
    agent = Agent()
    agent.set_user_session(json_payload["user_id"], json_payload["session_id"])
    output = agent.prompt_to_choose_meal_tree(json_payload["prompt"], model_speed= json_payload["model_speed"])

    return JSONResponse(content={"response":output})
from typing import Any, Generator
from starlette.responses import StreamingResponse
@app.post("/prompt-to-decompose-meal-tree-categories", response_model=dict)
async def prompt_to_decompose_meal_tree_categories(request_data: Payload)-> dict:

    json_payload = request_data.payload
    agent = Agent()
    agent.set_user_session(json_payload["user_id"], json_payload["session_id"])
    loop = asyncio.get_event_loop()
    output = await agent.prompt_decompose_to_meal_tree_categories(json_payload["prompt_struct"], model_speed= json_payload["model_speed"])
    # loop.close()
    return JSONResponse(content={"response":output})
    # async def stream():
    #     async for output in agent.prompt_decompose_to_meal_tree_categories(json_payload["prompt_struct"], model_speed= json_payload["model_speed"]):
    #         yield json.dumps({"response": output}).encode("utf-8")
    # return StreamingResponse(stream())

@app.post("/prompt-to-update-meal-tree", response_model=dict)
async def prompt_to_update_meal_tree(request_data: Payload) -> dict:
    # if CANNED_RESPONSES:
    #     with open('fixtures/update_meal_tree_response.json', 'r') as f:
    #         json_data = json.load(f)
    #         stripped_string_dict = {"response": json_data}
    #         return JSONResponse(content=stripped_string_dict)

    json_payload = request_data.payload
    agent = Agent()
    agent.set_user_session(json_payload["user_id"], json_payload["session_id"])
    output = agent.prompt_to_update_meal_tree(json_payload["category"], json_payload["from"], json_payload["to"], model_speed= json_payload["model_speed"])
    print("HERE IS THE OUTPUT", output)
    return JSONResponse(content={"response":output})


@app.post("/recipe-request", response_model=dict)
async def recipe_request(request_data: Payload) -> dict:
    if CANNED_RESPONSES:
        with open('fixtures/recipe_response.json', 'r') as f:
            json_data = json.load(f)
            stripped_string_dict = {"response": json_data}
            return JSONResponse(content=stripped_string_dict)

    json_payload = request_data.payload
    # factors_dict = {factor['name']: factor['amount'] for factor in json_payload['factors']}
    agent = Agent()
    agent.set_user_session(json_payload["user_id"], json_payload["session_id"])

    output = agent.recipe_generation(json_payload["prompt"], model_speed="slow")
    return JSONResponse(content={"response":json.loads(output)});


@app.post("/restaurant-request", response_model=dict)
async def restaurant_request(request_data: Payload) -> dict:
    json_payload = request_data.payload
    agent = Agent()
    agent.set_user_session(json_payload["user_id"], json_payload["session_id"])
    output = agent.restaurant_generation(json_payload["prompt"], model_speed="slow")
    return JSONResponse(content={"response":{"restaurants": output}});

@app.post("/delivery-request", response_model=dict)
async def delivery_request(request_data: Payload) -> dict:
    json_payload = request_data.payload
    # factors_dict = {factor['name']: factor['amount'] for factor in json_payload['factors']}
    agent = Agent()
    agent.set_user_session(json_payload["user_id"], json_payload["session_id"])
    output = await agent.delivery_generation( json_payload["prompt"], zipcode=json_payload["zipcode"], model_speed="slow")
    print("HERE IS THE OUTPUT", output)
    return JSONResponse(content={"response": {"url": output}})

@app.post("/voice-input", response_model=dict)
async def voice_input(request_data: Payload) -> dict:
    json_payload = request_data.payload
    agent = Agent()
    agent.set_user_session(json_payload["user_id"], json_payload["session_id"])
    output = agent.voice_input(query=json_payload["query"], model_speed= json_payload["model_speed"])
    return JSONResponse(content={"response":json.loads(output)})

@app.get("/health")
def health_check():
    return {"status": "OK"}

def start_api_server():
    # agent = establish_connection()
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    start_api_server()
