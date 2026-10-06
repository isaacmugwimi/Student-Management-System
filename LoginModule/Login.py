import customtkinter as ctk
from PIL import Image
from tkinter import messagebox


def start_login():

    # ---------------------------------
    # APPEARANCE
    # ---------------------------------

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    # ---------------------------------
    # MAIN WINDOW
    # ---------------------------------

    login_window = ctk.CTk()

    login_window.title("Modern Login System")
    login_window.geometry("600x650")
    login_window.resizable(False, False)

    # ---------------------------------
    # LOAD ICONS
    # ---------------------------------
    header_icon = ctk.CTkImage(
        light_image=Image.open("assets/user-lock-solid.png"),
        dark_image=Image.open("assets/user-lock-solid.png"),
        size=(100, 100),
    )

    user_icon = ctk.CTkImage(
        light_image=Image.open("assets/user-blue.png"),
        dark_image=Image.open("assets/user-blue.png"),
        size=(22, 22),
    )

    lock_icon = ctk.CTkImage(
        light_image=Image.open("assets/user-lock.png"),
        dark_image=Image.open("assets/user-lock.png"),
        size=(22, 22),
    )

    eye_icon = ctk.CTkImage(
        light_image=Image.open("assets/eye-solid.png"),
        dark_image=Image.open("assets/eye-solid.png"),
        size=(22, 22),
    )

    eye_icon_slash = ctk.CTkImage(
        light_image=Image.open("assets/eye-slash-regular.png"),
        dark_image=Image.open("assets/eye-slash-regular.png"),
        size=(20, 20),
    )
    login_icon = ctk.CTkImage(
        light_image=Image.open("assets/arrow-right-to-bracket-solid.png"),
        dark_image=Image.open("assets/arrow-right-to-bracket-solid.png"),
        size=(22, 22),
    )

    clear_icon = ctk.CTkImage(
        light_image=Image.open("assets/rotate-right-solid.png"),
        dark_image=Image.open("assets/rotate-right-solid.png"),
        size=(22, 22),
    )
    exit_icon = ctk.CTkImage(
        light_image=Image.open("assets/arrow-right-from-bracket-solid.png"),
        dark_image=Image.open("assets/arrow-right-from-bracket-solid.png"),
        size=(22, 22),
    )

    # ---------------------------------
    # VARIABLES
    # ---------------------------------

    password_visible = False

    # ---------------------------------
    # FUNCTIONS
    # ---------------------------------

    def login():

        username = username_entry.get()
        password = password_entry.get()

        if username == "":
            messagebox.showwarning("Warning", "Please enter your username.")
            return

        if password == "":
            messagebox.showwarning("Warning", "Please enter your password.")
            return

        if username == "admin" and password == "1234":

            messagebox.showinfo("Login Successful", "Welcome to the system!")

        else:

            messagebox.showerror("Login Failed", "Invalid username or password.")

    def clear_fields():

        username_entry.delete(0, "end")
        password_entry.delete(0, "end")

        username_entry.focus()

    def toggle_password():

        nonlocal password_visible

        if password_visible:

            password_entry.configure(show="*")
            eye_button.configure(image=eye_icon)

            password_visible = False

        else:

            password_entry.configure(show="")
            eye_button.configure(image=eye_icon_slash)

            password_visible = True

    def exit_application():

        result = messagebox.askyesno("Exit", "Are you sure you want to exit?")

        if result:
            login_window.destroy()

    # =================================
    # HEADER FRAME
    # =================================

    header_frame = ctk.CTkFrame(login_window, corner_radius=0, fg_color="#1976D2")

    # FRAME INSIDE MAIN WINDOW
    header_frame.pack(fill="x")

    

    # ---------------------------------
    # HEADER ICON
    # ---------------------------------
    header_icon_label = ctk.CTkLabel(
        header_frame,
        text="",
        image=header_icon,
        compound="left",
        font=("Arial", 15, "bold"),
    )
    # header_icon_label.pack(pady=(10, 0), padx=20, anchor="w")
    header_icon_label.pack()

    # ---------------------------------
    # HEADER TITLE
    # ---------------------------------

    title_label = ctk.CTkLabel(
        header_frame,
        text="LOGIN SYSTEM",
        text_color="white",
        font=("Arial", 28, "bold"),
    )

    title_label.pack(pady=(30, 10))

    # ---------------------------------
    # HEADER SUBTITLE
    # ---------------------------------

    subtitle_label = ctk.CTkLabel(
        header_frame,
        text="Welcome! Please login to continue",
        text_color="white",
        font=("Arial", 14),
    )

    subtitle_label.pack(pady=(0, 30))

    # =================================
    # LOGIN FRAME
    # =================================

    login_frame = ctk.CTkFrame(login_window, width=550, height=400)

    # FRAME INSIDE MAIN WINDOW
    login_frame.pack(padx=40, pady=35)

    # Keep the frame at exactly
    # 750 x 400
    login_frame.pack_propagate(False)

    # =================================
    # USERNAME LABEL
    # =================================

    username_label = ctk.CTkLabel(
        login_frame,
        text="Username",
        image=user_icon,
        compound="left",
        font=("Arial", 15, "bold"),
    )

    username_label.place(x=40, y=30)

    # =================================
    # USERNAME ENTRY
    # =================================

    username_entry = ctk.CTkEntry(
        login_frame, placeholder_text="Enter your username", height=40, width=360
    )

    username_entry.place(x=40, y=65)

    # =================================
    # PASSWORD LABEL
    # =================================

    password_label = ctk.CTkLabel(
        login_frame,
        text="Password",
        image=lock_icon,
        compound="left",
        font=("Arial", 15, "bold"),
    )

    password_label.place(x=40, y=125)

    # =================================
    # PASSWORD ENTRY
    # =================================

    password_entry = ctk.CTkEntry(
        login_frame,
        placeholder_text="Enter your password",
        show="*",
        height=40,
        width=310,
    )

    password_entry.place(x=40, y=160)

    # =================================
    # EYE BUTTON
    # =================================

    eye_button = ctk.CTkButton(
        login_frame,
        text="",
        image=eye_icon,
        width=40,
        height=40,
        fg_color="transparent",
        hover_color="#dddddd",
        command=toggle_password,
    )

    eye_button.place(x=355, y=160)

    # =================================
    # LOGIN BUTTON
    # =================================

    login_button = ctk.CTkButton(
        login_frame,
        text="LOGIN",
        image=login_icon,
        width=360,
        height=45,
        font=("Arial", 15, "bold"),
        command=login,
    )

    login_button.place(x=40, y=230)

    # =================================
    # CLEAR BUTTON
    # =================================

    clear_button = ctk.CTkButton(
        login_frame,
        text="CLEAR",
        width=170,
        height=40,
        image=clear_icon,
        fg_color="gray",
        hover_color="#555555",
        command=clear_fields,
    )

    clear_button.place(x=40, y=295)

    # =================================
    # EXIT BUTTON
    # =================================

    exit_button = ctk.CTkButton(
        login_frame,
        text="EXIT",
        width=170,
        image=exit_icon,
        height=40,
        fg_color="#d32f2f",
        hover_color="#b71c1c",
        command=exit_application,
    )

    exit_button.place(x=230, y=295)

    # =================================
    # FOCUS USERNAME
    # =================================

    username_entry.focus()

    # =================================
    # START APPLICATION
    # =================================

    login_window.mainloop()
