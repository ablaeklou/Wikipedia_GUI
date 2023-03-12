from tkinter import Tk, Frame, Label, Toplevel, Entry, Button, Text, Scrollbar, END, INSERT
from tkinter.messagebox import showerror
from wikipedia import summary



# create function which will show summary
def get_summary():
	
	
	try:
		
		
		answer.delete(1.0, END)
		
	
		answer.insert(INSERT, summary(keyword_entry.get()))
		
	
	except Exception as error:
		
	
		showerror("Error", error)


# create a GUI window
root = Tk()

# set title of window
root.title("Wikipedia GUI")

root.iconbitmap('Wikipedia2.ico')

# set geometry of geometry
root.geometry("770x650")

# set window's width and height to
# false => window will not be resizable
root.resizable(False, False)

# set background colour of window
root.configure(bg="silver")

# create a label for entry and button
mylabel = Label(root, text = 'Welcome to my Wikipedia GUI APP ', font=("cambria", 22, "bold",), fg="Green" ).pack()


# create a frame for entry and button
top_button = Button(root, bg="silver")
top_button.pack(side="top", fill="x", padx=50, pady=10)


# create a label for showing the search button

Label(top_button, text='Search here:',font=("cambria", 10, "italic",), fg="Magenta"  ).pack(side="left")

# create a label for search results

Label(root, 
	text='Search results:',
	pady=1,
	font=("Cambria",17)).pack()

# create a frame for text area where summary will be displayed
bottom_button = Button(root, bg="silver")
bottom_button.pack(side="top", fill="x", padx=10, pady=10)

#def clear
def clear():
       answer.delete(0.0,"end")



# create a entry box where user can enter a keyword
keyword_entry = Entry(top_button, font=("Cambria", 20, "bold"), width=25, bd=4)
keyword_entry.pack(side="left", ipady=6)

# create a search button
search_button = Button(top_button, text="SEARCH", font=(
	"Cambria", 18, "bold"), width=15, bd=4, command=get_summary)
search_button.pack(side="right")

# create a clear button

clear_button = Button(bottom_button, text="Clear", font=("Cambria", 18, "bold"),fg="Blue",  width=15, bd=4, command=clear)
clear_button.pack(side="bottom")

    

# create a exit button

exit_button = Button(bottom_button, text="EXIT", font=("Cambria", 18, "bold"),fg="red",  width=15, bd=4, command=root.destroy)
exit_button.pack(side="bottom")

# create a scroll bar for text area
scroll = Scrollbar(bottom_button)

# create a text area where summary will be displayed
answer = Text(bottom_button, font=("Cambria", 18), fg="Black",
			width=55, height=20, bd=5, yscrollcommand=scroll.set)
answer.pack(side="left", fill="y")
scroll.pack(side="left", fill="y")

# start the GUI
root.mainloop()
