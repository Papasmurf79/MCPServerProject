from fastmcp import FastMCP

mcp = FastMCP(name = "Calculator")

@mcp.tool()
def multiply(a: float, b: float) -> float: 
    
    """Multiplies two numbers and returns the result.
    
    args: a = float(a) - The First Number
          b = float(b) - The Second Number
     returns: float: the product of two numbers a and b.     
     """
    return a * b

@mcp.tool(
    name="add",
    description="Adds two numbers and returns the result.",
    tags=["arithmetic", "addition"] 
)
def add(a: float, b: float) -> float:
    """Adds two numbers and returns the result.
    
    args: a = float(a) - The First Number
          b = float(b) - The Second Number
     returns: float: the sum of two numbers a and b.     
     """
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtracts two numbers and returns the result.
    
    args: a = float(a) - The First Number
          b = float(b) - The Second Number
     returns: float: the difference of two numbers a and b.     
     """
    return a - b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divides two numbers and returns the result.
    
    args: a = float(a) - The First Number
          b = float(b) - The Second Number
     returns: float: the quotient of two numbers a and b.     
     """
    return a / b

if __name__ == "__main__":
    mcp.run() #STDIO by default