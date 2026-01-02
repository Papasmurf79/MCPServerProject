# Note: I am getting a MCP connection error in the MCP inspector
# However, the app is working fine on the localhost:8001 endpoint.

#Http
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

#Lets's create a FastAPI (api) app first
app = FastAPI(title="Calculator API")

@app.post("/multiply")
def multiply(a: float, b: float) -> float: 
    """Multiplies two numbers and returns the result.
    
    args: a = float(a) - The First Number
          b = float(b) - The Second Number
     returns: float: the product of two numbers a and b.     
     """
    return a * b
    return {"result": result}

@app.post("/add")
def add(a: float, b: float) -> float:
    """Adds two numbers and returns the result.
    
    args: a = float(a) - The First Number
          b = float(b) - The Second Number
     returns: float: the sum of two numbers a and b.     
     """
    return a + b
    return {"result": result}

@app.post("/subtract")
def subtract(a: float, b: float) -> float:
    """Subtracts two numbers and returns the result.
    
    args: a = float(a) - The First Number
          b = float(b) - The Second Number
     returns: float: the difference of two numbers a and b.     
     """
    return a - b
    return {"result": result}

@app.post("/divide")
def divide(a: float, b: float) -> float:
    """Divides two numbers and returns the result.
    
    args: a = float(a) - The First Number
          b = float(b) - The Second Number
     returns: float: the quotient of two numbers a and b.     
     """
    if b == 0:
        raise ValueError("Cannot divide by zero")   
     
    return a / b
    return {"result": result}

# Converting it to MCP uvicorn app
mcp = FastApiMCP(app, name="Calculator MCP")
mcp.mount_http()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8001)
