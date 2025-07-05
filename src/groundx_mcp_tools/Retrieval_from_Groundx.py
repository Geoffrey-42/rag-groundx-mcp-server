from groundx import AsyncGroundX
from typing import Optional, Dict, Any

async def Retrieval_from_Groundx(
    groundx_api_key: str,
    id: str,
    query: str,
    n: Optional[int] = None,
    next_token: Optional[str] = None,
    verbosity: Optional[int] = None,
    relevanced: Optional[float] = None,
    filter: Optional[Dict[str, Any]] = None
) -> str:
    """
    Search documents on GroundX for the most relevant information to a given query.
    
    See: https://docs.eyelevel.ai/reference/api-reference/search/content

    Args:
        groundx_api_key (str): The API key for GroundX.
        id (str): The bucketId, groupId, or documentId to be searched.
        query (str): The search query to be used to find relevant documentation.
        n (int, optional): The maximum number of returned search results. Accepts 1-100 with a default of 20.
        next_token (str, optional): A token for pagination. If the number of search results for a given query is larger than n, the response will include a "nextToken" value. That token can be included in this field to retrieve the next batch of n search results.
        verbosity (int, optional): The amount of data returned with each search result. 0 == no search results, only the recommended context. 1 == search results but no searchData. 2 == search results and searchData.
        relevanced (float, optional): The minimum search relevance score required to include the result. Defaults to 10.0.
        filter (dict, optional): A dictionary of key-value pairs that can be used to pre-filter documents prior to a search.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        params = {"id": id, "query": query}
        if n is not None:
            params["n"] = n
        if next_token is not None:
            params["next_token"] = next_token
        if verbosity is not None:
            params["verbosity"] = verbosity
        if relevanced is not None:
            params["relevanced"] = relevanced
        if filter is not None:
            params["filter"] = filter
        response = await client.search.content(**params)
        return response.search.text
    except Exception as e:
        return f"Error performing search: {str(e)}"
