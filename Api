import requests
import json

# Function to send a GET request
def send_get_request(url, headers=None):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()  
    else:
        print(f"GET request failed with status code: {response.status_code}")
        return None

# Function to send a POST request
def send_post_request(url, data, headers=None):
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if  response.status_code == 201:
        return response.json()  
    else:
        print(f"POST request failed with status code: {response.status_code}")
        try:
            return response.json()
        except json.JSONDecodeError:
            return None

# Function to send a PUT request
def send_put_request(url, data, headers=None):
    response = requests.put(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:  
        return response.json()  
    elif response.status_code == 204: 
        return {"message": "Update successful, no content returned"}
    else:
        print(f"PUT request failed with status code: {response.status_code}")
        try:
            return response.json()
        except json.JSONDecodeError:
            return None

# Example usage of the functions
if __name__ == "__main__":
    # Define your endpoints
    post_url = "https://restful-booker.herokuapp.com/booking"
    get_url = "https://restful-booker.herokuapp.com/booking"
    put_url = "https://restful-booker.herokuapp.com/booking/{booking_id}"  

    # Define headers and data for POST request
    post_headers = {
        "Content-Type": "application/json"
    }

    post_data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2020-01-01",
            "checkout": "2023-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    
    # Define headers and data for PUT request
    put_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="  
}

    put_data = {
        "firstname": "Segun",
        "lastname": "Omiyedun",  
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
        "checkin": "2024-01-01",
        "checkout": "2024-01-02"
    },
        "additionalneeds": "SegunApirequest"  
}

    # Step 1: Create a booking (POST request)
    post_response = send_post_request(post_url, post_data, post_headers)
    if post_response:
        print("POST request successful:")
        print(json.dumps(post_response, indent=4))
        booking_id = post_response.get('bookingid')
    else:
        print("Failed to create booking.")
        exit()

    # Step 2: Get the booking details using the booking ID (GET request)
    get_response = send_get_request(f"{get_url}/{booking_id}")
    if get_response:
        print("GET request successful:")
        print(json.dumps(get_response, indent=4))
    else:
        print("Failed to get booking details.")
        exit()

    # Step 3: Update the booking (PUT request)
    put_response = send_put_request(f"{put_url.format(booking_id=booking_id)}", put_data, put_headers)
    if put_response:
        print("PUT request successful:")
        print(json.dumps(put_response, indent=4))
    else:
        print("Failed to update booking.")
