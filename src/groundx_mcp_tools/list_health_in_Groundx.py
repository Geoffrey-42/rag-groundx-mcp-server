from groundx import AsyncGroundX

async def list_health_in_Groundx(groundx_api_key: str) -> dict:
    """
    List the current health status of all services. Statuses update every 5 minutes.
    
    See: https://docs.eyelevel.ai/reference/api-reference/health/list

    Args:
        groundx_api_key (str): The API key for GroundX.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        response = await client.health.list()
        return response
    except Exception as e:
        return {"error": f"Failed to list health: {str(e)}"}
