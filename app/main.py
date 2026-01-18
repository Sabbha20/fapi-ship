from fastapi import FastAPI

app = FastAPI()

@app.get("/shipment")
def shipment():
    return {
        "content": "wooden table",
        "status": "in transit"
    }