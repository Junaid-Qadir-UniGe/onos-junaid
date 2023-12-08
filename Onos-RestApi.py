#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth

# ONOS Controller API base URL
onos_base_url = "http://192.168.254.38:8181/onos"

# Endpoint URL for devices
devices_endpoint = "/v1/devices"

# ONOS Controller credentials
username = "onos"
password = "rocks"

# Function to get ONOS Devices
def get_devices():
    url = onos_base_url + devices_endpoint
    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    devices_data = get_devices()

    if devices_data is not None:
        print("Devices Data:")
        print(devices_data)
