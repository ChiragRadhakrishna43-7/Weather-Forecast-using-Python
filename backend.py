# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 18:09:58 2023

@author: Krishna
"""
import requests

API_KEY = "a0dc6fea6ebe7ee1326dfc09c463ac7d"

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"   
    response = requests.get(url)  
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    
    return filtered_data