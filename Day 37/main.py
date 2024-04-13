import requests
USER_NAME = "csk"
USER_TOKEN = "chennaisuperkings"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": USER_TOKEN ,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response)

headers = {
    "X-USER-TOKEN" : USER_TOKEN
}
graph_params = {
    "id": "graph1",
    "name": "jogging",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}
graph_endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs"

# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(graph_response)

# Create a Pixel. Store new data
pixel_data = {
    "date": "20220507",
    "quantity": "3.5"
}
pixel_endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs/graph1"
# pixel_response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# print(pixel_response)

# Update a Pixel. Modify the data
update_pixel_data = {
    "quantity": "6.5"
}
update_pixel_endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs/graph1/20220507"
# update_pixel_response = requests.put(url=update_pixel_endpoint, json=update_pixel_data, headers=headers)
# print(update_pixel_response)

# Delete a Pixel. Delete the data

delete_pixel_endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs/graph1/20220507"
delete_pixel_response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(delete_pixel_response)