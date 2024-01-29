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

class PaymentPage(BasePage):
    def create_widgets(self):
        label_title = CTkLabel(self, text="Payment Page", font=("ar", 15, "bold"))
        label_title.pack(pady=20)

        # Entry fields for payment information
        self.card_number_var = tk.StringVar()
        self.expiry_date_var = tk.StringVar()
        self.cvv_var = tk.StringVar()

        card_number_label = CTkLabel(self, text="Card Number:")
        card_number_label.pack(pady=5)
        card_number_entry = CTkEntry(self, textvariable=self.card_number_var)
        card_number_entry.pack(pady=5)

        expiry_date_label = CTkLabel(self, text="Expiry Date (MM/YY):")
        expiry_date_label.pack(pady=5)
        expiry_date_entry = CTkEntry(self, textvariable=self.expiry_date_var)
        expiry_date_entry.pack(pady=5)

        cvv_label = CTkLabel(self, text="CVV:")
        cvv_label.pack(pady=5)
        cvv_entry = CTkEntry(self, textvariable=self.cvv_var, show="*")
        cvv_entry.pack(pady=5)

        pay_button = CTkButton(self, text="Pay", command=self.process_payment)
        pay_button.pack(pady=10)

        back_to_home_button = CTkButton(self, text="Back to Home", command=self.page_controller.show_home_page)
        back_to_home_button.pack(pady=10)

    def process_payment(self):
        # Get payment information
        card_number = self.card_number_var.get()
        expiry_date = self.expiry_date_var.get()
        cvv = self.cvv_var.get()

        # Validate payment information (you can add more validation as needed)
        if card_number and expiry_date and cvv:
            # Process the payment (this is just an example, you may need to customize this part)
            payment_info = {
                "card_number": card_number,
                "expiry_date": expiry_date,
                "cvv": cvv
            }

            # Save the payment information or perform other actions
            # For now, let's print the information
            print("Payment processed successfully!")
            print("Payment Information:", payment_info)

            # Show a messagebox with payment details
            messagebox.showinfo("Payment Successful", "Payment processed successfully!")

            # You can add more logic here, such as updating a database or UI elements

            # Navigate back to the home page
            self.page_controller.show_home_page()
        else:
            messagebox.showerror("Invalid Payment Information", "Please fill in all payment fields.")
