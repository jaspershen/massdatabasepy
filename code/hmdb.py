import requests

class HMDBDownloader:
    BASE_URL = "https://hmdb.ca/unearth/q"

    @staticmethod
    def download_metabolite(metabolite_id: str) -> str:
        """Downloads HMDB metabolite data given a metabolite ID."""
        url = f"{HMDBDownloader.BASE_URL}/{metabolite_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            raise ValueError(f"Failed to fetch data for metabolite ID {metabolite_id}")

    @staticmethod
    def save_metabolite_data(metabolite_id: str, file_path: str):
        """Downloads and saves HMDB metabolite data to a file."""
        data = HMDBDownloader.download_metabolite(metabolite_id)
        with open(file_path, "w") as f:
            f.write(data)
