import requests

class Post:
    def __init__(self) -> None:
        self.get_all_data()

    def get_all_data(self):
        response = requests.get(url='https://api.npoint.io/ed99320662742443cc5b')
        response.raise_for_status()
        data = response.json()
        return data

    def single_post(self, id):
        # print(f"id: {id}")
        data = self.get_all_data()
        single_blog = []
        single_blog = [item for item in data if item["id"] == id]
        # for item in data:
        #     print(f"item: {item['id']}")
        #     if item['id'] == id:
        #         print(item)
        #         single_blog.append(item)
        return single_blog[0]
