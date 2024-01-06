import requests

def request_kegg_compound(compound_id):
    """
    Retrieve information about a compound from the KEGG database.

    This function takes a KEGG compound ID and returns a list of strings,
    each string containing a line of information about the compound from the KEGG database.

    Args:
    compound_id (str): The KEGG compound ID.

    Returns:
    list of str: Information about the compound.

    Example:
    >>> request_kegg_compound("C00002")
    ['ENTRY       C00002            Compound', 'NAME        ATP;', ...]

    Note:
    This function requires an internet connection to access the KEGG API.
    """

    url = f"http://rest.kegg.jp/get/{compound_id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.strip().split('\n')
        else:
            return f"Failed to retrieve data. Status code: {response.status_code}"
    except Exception as e:
        return str(e)

# # Example usage
# print(request_kegg_compound("C00002"))
