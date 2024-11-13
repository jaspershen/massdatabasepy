import requests

class KEGGDownloader:
    BASE_URL = "https://rest.kegg.jp/get"

    @staticmethod
    def download_pathway(pathway_id: str) -> str:
        """Downloads KEGG pathway data given a pathway ID."""
        url = f"{KEGGDownloader.BASE_URL}/{pathway_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            raise ValueError(f"Failed to fetch data for pathway ID {pathway_id}")

    @staticmethod
    def save_pathway_data(pathway_id: str, file_path: str):
        """Downloads and saves KEGG pathway data to a file."""
        data = KEGGDownloader.download_pathway(pathway_id)
        with open(file_path, "w") as f:
            f.write(data)
