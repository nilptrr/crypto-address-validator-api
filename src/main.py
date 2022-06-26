from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from crypto_address_validator import validate
import uvicorn


app = FastAPI()


@app.get('/validate', response_class=HTMLResponse)
def validate_address(symbol: str, address: str):
    """Validates the address of the passed symbol.

    Args:
        symbol (str): Currency symbol, e.g. 'btc' or 'atom'.
        address (str): Currency address to validate.

    Returns:
        bool: Result of address validation.
    """
    is_valid = validate(symbol, address)
    validation_result = True if is_valid else False
    return str(validation_result)


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)
