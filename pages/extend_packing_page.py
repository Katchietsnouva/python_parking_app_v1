import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from customtkinter import CTkEntry, CTkButton, CTkLabel, CTkCheckBox
import datetime

# from controllers.page_controller import PageController
# from controllers.user_controller import UserController
from pages.base_page import BasePage
# from pages.login_page import LoginPage
# from pages.registration_page import RegisterPage
# from pages.home_page import HomePage
# from pages.booking_page import BookingPage
# from extend_packing_page import ExtendParkingPage
# from payment_page import PaymentPage
# from profit_loss_page import ProfitLossPage

class ExtendParkingPage(BasePage):
    def create_widgets(self):
        label_title = CTkLabel(self, text="Extend Parking Time", font=("ar", 15, "bold"))
        label_title.pack(pady=20)

        # Entry field for extending duration
        self.extend_duration_var = tk.StringVar()
        extend_duration_label = CTkLabel(self, text="Extend Duration (hours):")
        extend_duration_label.pack(pady=5)
        extend_duration_entry = CTkEntry(self, textvariable=self.extend_duration_var)
        extend_duration_entry.pack(pady=5)

        extend_button = CTkButton(self, text="Extend Parking", command=self.extend_parking)
        extend_button.pack(pady=10)

        pay_button = CTkButton(self, text="Proceed to Payment", command=self.page_controller.show_payment_page)
        pay_button.pack(pady=10)

        back_to_home_button = CTkButton(self, text="Back to Home", command=self.page_controller.show_home_page)
        back_to_home_button.pack(pady=10)


    def extend_parking(self):
        extend_duration = self.extend_duration_var.get()

        # Validate if a valid duration is entered (you can add more validation as needed)
        if extend_duration.isdigit() and int(extend_duration) > 0:
            # Process the parking extension (this is just an example, you may need to customize this part)
            extension_info = {
                "user": "CurrentUser",  # Replace with actual user information
                "extended_duration": int(extend_duration),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            # Save the extension information or perform other actions
            # For now, let's print the information
            print("Parking extended successfully!")
            print("Extension Information:", extension_info)

            # Show a messagebox with the extension details
            messagebox.showinfo("Extension Successful", f"Parking extended for {extend_duration} hours!")

            # You can add more logic here, such as updating a database or UI elements

            # Navigate back to the home page
            self.page_controller.show_home_page()
        else:
            messagebox.showerror("Invalid Duration", "Please enter a valid positive number for extension duration.")

