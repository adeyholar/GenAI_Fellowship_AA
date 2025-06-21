from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

# FastAPI App Setup
app = FastAPI(
    title="Calculator API",
    description="A REST API for basic arithmetic operations",
    version="1.0.0"
)

# Pydantic Model for Request Validation
class CalculationRequest(BaseModel):
    operation: str
    num1: float
    num2: float

# API Endpoints
@app.get("/")
async def root():
    return {"message": "Welcome to the Calculator API. Visit /docs for API documentation."}

@app.post("/calculate")
async def calculate(request: CalculationRequest):
    try:
        if request.operation == "add":
            result = request.num1 + request.num2
        elif request.operation == "subtract":
            result = request.num1 - request.num2
        elif request.operation == "multiply":
            result = request.num1 * request.num2
        elif request.operation == "divide":
            if request.num2 == 0:
                raise HTTPException(status_code=400, detail="Division by zero is not allowed")
            result = request.num1 / request.num2
        else:
            raise HTTPException(status_code=400, detail="Invalid operation. Use add, subtract, multiply, or divide")
        
        return {"operation": request.operation, "num1": request.num1, "num2": request.num2, "result": result}
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid input. Numbers must be valid floats")

# Run FastAPI Server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)