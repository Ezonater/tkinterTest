import tkinter as tk

current_playlist = None
current_thumbnail = None
current_title = None

main_menu = tk.Tk()
main_menu.title("This is the info screen")


def playlist_update(sv):
    global current_playlist
    current_playlist = sv
    check_start_button()


def title_update(sv):
    global current_title
    current_title = sv
    check_start_button()


def check_start_button():
    if (playlist_entry.get() != "") & (title_entry.get() != ""):
        if playlist_entry.get()[:38] == "https://www.youtube.com/playlist?list=":
            start_button.config(state=tk.NORMAL)
            start_label.config(text="Title: " + title_entry.get() + "\nPlaylist: " + playlist_entry.get())
            start_label.pack()
        else:
            start_label.forget()
            start_button.config(state=tk.DISABLED)
            start_label.config(text="Title: " + title_entry.get() + "\nPlaylist: That is not a valid YouTube playlist link.")
    else:
        start_label.forget()
        start_button.config(state=tk.DISABLED)



info_label = tk.Label(main_menu, text="Please note that this program is still in development.")
main_label = tk.Label(main_menu, text="Compilation Generator", font=30, pady=20)
playlist_entry_label = tk.Label(main_menu, text="Enter your playlist here:")
playlist_text_variable = tk.StringVar()
playlist_text_variable.trace("w",
                             lambda name, index, mode, playlist_text_variable=playlist_text_variable,: playlist_update(
                                 playlist_text_variable))
playlist_entry = tk.Entry(main_menu, textvariable=playlist_text_variable)
title_entry_label = tk.Label(main_menu, text="Enter your title here:")
title_text_variable = tk.StringVar()
title_text_variable.trace("w", lambda name, index, mode, title_text_variable=title_text_variable,: title_update(
    title_text_variable))
title_entry = tk.Entry(main_menu, textvariable=title_text_variable)

start_label = tk.Label(main_menu, text="Title: " + str(current_title) + "\nPlaylist: " + str(current_playlist), pady=30)
start_button = tk.Button(main_menu, text="Start!", state=tk.DISABLED)
error_text_variable = tk.StringVar()
error_label = tk.Label(main_menu, textvariable=error_text_variable)


def next_screen():
    main_menu.title("This is the main menu")
    main_menu.geometry("400x400")
    begin_button.forget()
    info_label.forget()
    main_label.pack()
    title_entry_label.pack()
    title_entry.pack()
    playlist_entry_label.pack()
    playlist_entry.pack()
    start_button.pack()


begin_button = tk.Button(main_menu, text="Begin", command=next_screen)
info_label.pack()
begin_button.pack()
main_menu.mainloop()
