from groundx import AsyncGroundX

async def get_health_in_Groundx(groundx_api_key: str, service: str) -> dict:
    """
    Look up the current health status of a specific service. Statuses update every 5 minutes.
    
    See: https://docs.eyelevel.ai/reference/api-reference/health/get

    Args:
        groundx_api_key (str): The API key for GroundX.
        service (str): The name of the service to look up.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        response = await client.health.get(service=service)
        return response
    except Exception as e:
        return {"error": f"Failed to get health: {str(e)}"}
