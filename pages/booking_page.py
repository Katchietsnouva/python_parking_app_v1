import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from customtkinter import CTkEntry, CTkButton, CTkLabel, CTkCheckBox
from datetime import datetime
from tkcalendar import *

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

class BookingPage(BasePage):
    def create_widgets(self):
        # label_title = CTkLabel(self, text="Booking Page", font=("ar", 15, "bold"))
        # label_title.pack(pady=20)

        # Entry fields for booking information
        self.duration_var = tk.StringVar()

        # duration_label = CTkLabel(self, text="Parking Duration (hours):")
        # duration_label.pack(pady=5)
        # duration_entry = CTkEntry(self, textvariable=self.duration_var)
        # duration_entry.pack(pady=5)

        # book_button = CTkButton(self, text="Book Parking", command=self.book_parking)
        # book_button.pack(pady=10)

        home_button = CTkButton(self, text="Home Page", command=self.page_controller.show_home_page)
        home_button.pack(pady=10)

        
        # clock_frame = ctk.CTk()
        # self.title("Date Picker Car Park Slot Booking")
        # self.geometry("1000x600")
        # self.master.geometry("1000x600")
        # clock_frame.configure(bg="#cd950c")

        hour_string = ctk.StringVar()
        min_string = ctk.StringVar()
        sec_string = ctk.StringVar()
        hour_string_2 = ctk.StringVar()
        min_string_2 = ctk.StringVar()
        sec_string_2 = ctk.StringVar()
        hour_string_3 = ctk.StringVar()
        min_string_3 = ctk.StringVar()
        sec_string_3 = ctk.StringVar()
        last_value_sec = ""
        last_value = ""
        font_prefab = ('Times', 24)


        formatted_date_1 = None
        formatted_date_2 = None

        
        self.master.geometry("1000x800")
        # def set_geometry_a(self):
        #     self.master.geometry("1000x600")

        def display_arrival_time_msg():
            global formatted_date_1
            selected_date = cal.get_date()
            current_datetime = datetime.now()
            formatted_date_1 = datetime.strptime(selected_date, "%m/%d/%y").strftime("%d/%m/%Y")
            selected_datetime = datetime.strptime(formatted_date_1, "%d/%m/%Y")
            # Get selected time
            hr_d_2 = hr_box_2.get()
            min_d_2 = min_box_2.get()
            sec_d_2 = sec_box_2.get()

            # Call the validation function
            if not validate_selected_date(formatted_date_1, selected_datetime, hr_d_2, min_d_2, current_datetime):
                return False
            
            t_a = f"Arrival date: {formatted_date_1}      Time IN: {hr_d_2}:{min_d_2}:{sec_d_2} hrs."
            book_msg_display_arrival.configure(text=t_a)
            print(t_a)

            
        def display_departure_time_msg():
            global formatted_date_2
            selected_date = cal.get_date()
            current_datetime = datetime.now()
            formatted_date_2 = datetime.strptime(selected_date, "%m/%d/%y").strftime("%d/%m/%Y")
            selected_datetime = datetime.strptime(formatted_date_2, "%d/%m/%Y")
            # Get selected time
            hr_d_3 = hr_box_3.get()
            min_d_3 = min_box_3.get()
            sec_d_3 = sec_box_3.get()

            if not validate_selected_date(formatted_date_2, selected_datetime, hr_d_3, min_d_3, current_datetime):
                return False
            calculate_duration()
            
            t_d = f"Departure date: {formatted_date_2}        Time OUT: {hr_d_3}:{min_d_3}:{sec_d_3} hrs."
            book_msg_display_departure.configure(text=t_d)
            print(t_d)

            


        # def calculate_duration():
        #     selected_date = cal.get_date()
        #     arrival_time = datetime.strptime(f"{selected_date} {hr_box_2.get()}:{min_box_2.get()}:{sec_box_2.get()}", "%m/%d/%y %H:%M:%S")
        #     departure_time = datetime.strptime(f"{selected_date} {hr_box_3.get()}:{min_box_3.get()}:{sec_box_3.get()}", "%m/%d/%y %H:%M:%S")

        #     duration = departure_time - arrival_time

        #     if duration.total_seconds() < 0:
        #         tk.messagebox.showerror("Invalid Duration", "Departure time cannot be earlier than arrival time.")
        #         return False  # Indicate invalid duration

        #     minutes = duration.total_seconds() / 60
        #     parking_duration.configure(text=f"You will park for {int(minutes)} minutes")
        #     return True  # Indicate valid duration



        def calculate_duration():
            global formatted_date_1, formatted_date_2
            # If departure date is different, adjust accordingly
            # if formatted_date_2 != formatted_date_1:  # Assuming formatted_date_2 holds the departure date
            #     departure_time = datetime.strptime(f"{formatted_date_2} {hr_box_3.get()}:{min_box_3.get()}:{sec_box_3.get()}", "%d/%m/%Y %H:%M:%S")
            #     arrival_time = datetime.strptime(f"{formatted_date_1} {hr_box_2.get()}:{min_box_2.get()}:{sec_box_2.get()}", "%d/%m/%Y %H:%M:%S")
            departure_time = datetime.strptime(f"{formatted_date_2} {hr_box_3.get()}:{min_box_3.get()}:{sec_box_3.get()}", "%d/%m/%Y %H:%M:%S")
            arrival_time = datetime.strptime(f"{formatted_date_1} {hr_box_2.get()}:{min_box_2.get()}:{sec_box_2.get()}", "%d/%m/%Y %H:%M:%S")

            # Calculate duration, handling potential negative values due to day differences
            duration = departure_time - arrival_time
            if duration.days < 0:
                tk.messagebox.showerror("Invalid Duration", "Departure date cannot be earlier than arrival date.")
                return False

            total_minutes = duration.days * 24 * 60 + duration.seconds // 60
            
            days = duration.days    
            hours, remainder = divmod(duration.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            detailed_duration_text = f" {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds"
            combined_text = f"You will park for {total_minutes} minutes equivalent to:\n{detailed_duration_text}"

            parking_duration_label.configure(text="")
            # parking_duration_label.insert=("0.0,","You will park for 0 min")
            
            parking_duration.configure(state='normal')  # Allow modifications
            parking_duration.delete(1.0, 'end')          # Clear existing content
            parking_duration.insert("0.0", combined_text)  # Insert the new content
            # parking_duration.insert("0.0", combined_text)  # Insert the new content

            parking_duration.configure(state='disabled') 
            
            print(combined_text)
            return True


        def validate_selected_date(formatted_date, selected_datetime, hour_value_ver, minute_value_ver, current_datetime):
            # Extract day, month, and year separately
            selected_day = selected_datetime.day
            selected_month = selected_datetime.month
            selected_year = selected_datetime.year

            current_day = current_datetime.day
            current_month = current_datetime.month
            current_year = current_datetime.year

            # Compare only day, month, and year to see if the date is same day
            if (selected_year, selected_month, selected_day) == (current_year, current_month, current_day):
                print("processing the accepted current date time ")
                if int(hour_value_ver) == current_datetime.hour:
                    if int(minute_value_ver) > current_datetime.minute:
                        print("processing the accepted current date time HOUR")
                    else:
                        tk.messagebox.showerror("Check Time Error(Minute)!", "Select a minute value greater than current minute value.\nYou can not book a time in the past.")
                        print("Check Time Error(Minute)!", "Select a minute value greater than current minute value.\nYou can not book a time in the past.")
                        return False    
                elif int(hour_value_ver) > current_datetime.hour:
                    print("processing the accepted current date time HOUR 2")
                else:
                    tk.messagebox.showerror("Check Time Error(Hour)!", "Select an hour value equal or greater than current hour value.\nYou can not book a time in the past.")
                    print("Check Time Error(Hour)!", "Select an hour value equal or greater than current hour value.\nYou can not book a time in the past.")
                    return False
            # now compare the date if the are on different days
            # elif formatted_date > datetime.now().strftime("%d/%m/%y"):
            elif selected_datetime > current_datetime:
                print("the greatter date selected date was accepted") 
            else:
                tk.messagebox.showerror("Check Date Error", "Select a date greater than current date.\nYou cannot book a date in the past.")
                print("Check Date Error", "Select a date greater than current date.\nYou can not book a date in the past.")
                return False
            return True






        current_raw_time_validity = datetime.now().strftime("%d:%m:%y")
        print(str(current_raw_time_validity) + " (this is current system date in day/month/year)")

        current_time_validity = datetime.now().strftime("%H:%M:%S")
        print(current_time_validity + " (this is current time value used to update real time UI clock at time of initial code call)")
        def update_current_time():
            current_time = datetime.now().strftime("%H:%M:%S")
            hour_value = current_time.split(":")[0]
            min_value = current_time.split(":")[1]
            sec_value = current_time.split(":")[2]

            # Update the Spinbox values
            hr_box.delete(0, "end")
            hr_box.insert(0, hour_value)
            
            min_box.delete(0, "end")
            min_box.insert(0, min_value)
            
            sec_box.delete(0, "end")
            sec_box.insert(0, sec_value)
            

            # clock_frame.after(1000, update_current_time)
            self.after(1000, update_current_time)

        # frames_container =  ctk.CTkFrame(clock_frame)
        frames_container =  ctk.CTkFrame(self)
        upper_frame = ctk.CTkFrame(frames_container)
        middle_frame = ctk.CTkFrame(frames_container)
        middle_frame_left = ctk.CTkFrame(middle_frame)
        middle_frame_middle = ctk.CTkFrame(middle_frame)
        middle_frame_right = ctk.CTkFrame(middle_frame)
        lower_frame = ctk.CTkFrame(frames_container)
        lower_frame_btn_frame = ctk.CTkFrame(lower_frame)
        lower_frame_label_frame = ctk.CTkFrame(lower_frame)

        initial_date = datetime.now()
        # print(initial_date)
        cal = Calendar(
            upper_frame,
            selectmode="day",
            day=initial_date.day,
            month=initial_date.month,
            year=initial_date.year,
            font=font_prefab
        )

        cal.pack(fill=tk.BOTH, expand=True)


        # For displaying current time in real time update
        hr_box = tk.Spinbox(
            middle_frame_left,
            from_=0,
            to=23,
            wrap=True,
            textvariable=hour_string,
            font=font_prefab,
            width=6,
            justify=tk.CENTER
        )

        min_box = tk.Spinbox(
            middle_frame_left,
            from_=0,
            to=59,
            wrap=True,
            textvariable=min_string,
            width=6,
            # state="readonly",
            font=font_prefab,
            justify=tk.CENTER
        )

        sec_box = tk.Spinbox(
            middle_frame_left,
            from_=0,
            to=59,
            wrap=True,
            textvariable=sec_string,
            width=6,
            font=font_prefab,
            justify=tk.CENTER
        )

        diag_msg1a = ctk.CTkLabel(
            middle_frame_left,
            text="Real Time Update",
            font=('HP Simplified', 14)
        )
        diag_msg1b = ctk.CTkLabel(
            middle_frame_left,
            text="Hour  Minute  Seconds",
            font=('HP Simplified', 14)
        )
        diag_msg1a.pack(side=tk.TOP,padx=10, pady=5)
        diag_msg1b.pack(side=tk.TOP,padx=10, pady=5)

        hr_box.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=20)
        min_box.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=20)
        sec_box.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=20)

        update_current_time()  # Call the function to update time continuously







        # For specifying the arrival time at the booking slot
        hr_box_2 = tk.Spinbox(
            middle_frame_middle,
            from_=0,
            to=23,
            wrap=True,
            textvariable=hour_string_2,
            font=font_prefab,
            width=6,
            justify=tk.CENTER
        )

        min_box_2 = tk.Spinbox(
            middle_frame_middle,
            from_=0,
            to=59,
            wrap=True,
            textvariable=min_string_2,
            width=6,
            # state="readonly",
            font=font_prefab,
            justify=tk.CENTER
        )

        sec_box_2 = tk.Spinbox(
            middle_frame_middle,
            from_=0,
            to=59,
            wrap=True,
            textvariable=sec_string_2,
            width=6,
            font=font_prefab,
            justify=tk.CENTER
        )

        diag_msg_2a = ctk.CTkLabel(
            middle_frame_middle,
            text="Select Parking Arrival Time",
            font=('HP Simplified', 14)
        )

        diag_msg_2b = ctk.CTkLabel(
            middle_frame_middle,
            text="Hour      Minute",
            font=('HP Simplified', 14)
        )
        diag_msg_2a.pack(side=tk.TOP,padx=10, pady=5)
        diag_msg_2b.pack(side=tk.TOP,padx=10, pady=5)

        hr_box_2.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=20)
        min_box_2.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=20)
        sec_box_2.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=20)



        # For specifying the departure time from the booking slot
        hr_box_3 = tk.Spinbox(
            middle_frame_right,
            from_=0,
            to=23,
            wrap=True,
            textvariable=hour_string_3,
            font=font_prefab,
            width=6,
            justify=tk.CENTER
        )

        min_box_3 = tk.Spinbox(
            middle_frame_right,
            from_=0,
            to=59,
            wrap=True,
            textvariable=min_string_3,
            width=6,
            # state="readonly",
            font=font_prefab,
            justify=tk.CENTER
        )

        sec_box_3 = tk.Spinbox(
            middle_frame_right,
            from_=0,
            to=59,
            wrap=True,
            textvariable=sec_string_3,
            width=6,
            font=font_prefab,
            justify=tk.CENTER
        )

        diag_msg_3a = ctk.CTkLabel(
            middle_frame_right,
            text="Select Parking Departure Time",
            font=('HP Simplified', 14)
        )

        diag_msg_3b = ctk.CTkLabel(
            middle_frame_right,
            text="Hour      Minute",
            font=('HP Simplified', 14)
        )
        diag_msg_3a.pack(side=tk.TOP,padx=10, pady=5)
        diag_msg_3b.pack(side=tk.TOP,padx=10, pady=5)

        hr_box_3.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=20)
        min_box_3.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=20)
        sec_box_3.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=20)




        arrivalBtn = ctk.CTkButton(
            lower_frame_btn_frame,
            text="Book Arrival Time",
            command=display_arrival_time_msg
        )
        arrivalBtn.pack(side= tk.LEFT, padx=20, pady=10)

        departureBtn = ctk.CTkButton(
            lower_frame_btn_frame,
            text="Book Departure Time",
            command=display_departure_time_msg
        )
        departureBtn.pack(side= tk.RIGHT, padx=20, pady=10)

        book_msg_display_arrival = ctk.CTkLabel(
            lower_frame_label_frame,
            text="Pick Arrival Time"
        )
        book_msg_display_arrival.pack(side= tk.LEFT, padx=20, pady=10)

        book_msg_display_departure= ctk.CTkLabel(
            lower_frame_label_frame,
            text="Pick Departure Time"
        )
        book_msg_display_departure.pack(side= tk.RIGHT, padx=20, pady=10)

        parking_duration_label = ctk.CTkLabel(
            lower_frame_label_frame,
            text="You will park for 0 min"
        )
        parking_duration_label.pack(padx=20, pady=10)

        parking_duration = ctk.CTkTextbox(
            lower_frame_btn_frame,
            wrap="word",  # Wrap text at word boundaries
            height=50,     # Set the desired height (number of lines)
            width=600     # Set the desired width (number of characters)
            
        )
        parking_duration.pack(padx=20, pady=20)


        # upper_frame.pack(padx=20, pady=20)
        upper_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)
        middle_frame_left.pack(side=tk.LEFT, expand=True, padx=10, pady=10)
        middle_frame_middle.pack(side=tk.LEFT, expand=True, padx=10, pady=10)
        middle_frame_right.pack(expand=True, padx=10, pady=10)  
        middle_frame.pack(expand=True, padx=10, pady=5)
        lower_frame_btn_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)
        lower_frame_label_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)
        lower_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)
        frames_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)


        




        # clock_frame.mainloop()