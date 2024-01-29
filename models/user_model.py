import datetime
import tkinter as tk
import customtkinter as ctk
from customtkinter import CTkEntry, CTkButton, CTkLabel, CTkCheckBox
from tkinter import messagebox

    
# models/user_model.py
class UserModel:
    def __init__(self, username, password, name, phone, car_plate, email):
        self.username = username
        self.password = password
        self.name = name
        self.phone = phone
        self.car_plate = car_plate
        self.email = email