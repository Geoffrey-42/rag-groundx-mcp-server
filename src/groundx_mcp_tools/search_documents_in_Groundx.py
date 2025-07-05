from groundx import AsyncGroundX
from typing import List, Optional, Dict, Any

async def search_documents_in_Groundx(
    groundx_api_key: str,
    document_ids: List[str],
    query: str,
    n: Optional[int] = None,
    next_token: Optional[str] = None,
    verbosity: Optional[int] = None,
    filter: Optional[Dict[str, Any]] = None,
    relevanced: Optional[float] = None
) -> dict:
    """
    Search documents on GroundX for the most relevant information to a given query by documentId(s).
    
    See: https://docs.eyelevel.ai/reference/api-reference/search/documents

    Args:
        groundx_api_key (str): The API key for GroundX.
        document_ids (List[str]): An array of unique documentIds to be searched.
        query (str): The search query to be used to find relevant documentation.
        n (int, optional): The maximum number of returned search results. Accepts 1-100 with a default of 20.
        next_token (str, optional): A token for pagination. If the number of search results for a given query is larger than n, the response will include a "nextToken" value. That token can be included in this field to retrieve the next batch of n search results.
        verbosity (int, optional): The amount of data returned with each search result. 0 == no search results, only the recommended context. 1 == search results but no searchData. 2 == search results and searchData.
        filter (dict, optional): A dictionary of key-value pairs that can be used to pre-filter documents prior to a search.
        relevanced (float, optional): The minimum search relevance score required to include the result. Defaults to 10.0.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        params = {"document_ids": document_ids, "query": query}
        if n is not None:
            params["n"] = n
        if next_token is not None:
            params["next_token"] = next_token
        if verbosity is not None:
            params["verbosity"] = verbosity
        if filter is not None:
            params["filter"] = filter
        if relevanced is not None:
            params["relevanced"] = relevanced
        response = await client.search.documents(**params)
        return response
    except Exception as e:
        return {"error": f"Failed to search documents: {str(e)}"}
