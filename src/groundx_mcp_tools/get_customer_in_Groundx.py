from groundx import AsyncGroundX

async def get_customer_in_Groundx(groundx_api_key: str) -> dict:
    """
    Get the account information associated with the API key.
    
    See: https://docs.eyelevel.ai/reference/api-reference/customer/get

    Args:
        groundx_api_key (str): The API key for GroundX.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        response = await client.customer.get()
        return response
    except Exception as e:
        return {"error": f"Failed to get customer: {str(e)}"}