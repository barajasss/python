import os
from tkinter import *
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox

root = Tk()
root.geometry('500x400+400+200')


PROGRAM_NAME = "Text Editor"
file_name = None

root.title(PROGRAM_NAME)

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
edit_menu = Menu(menu_bar, tearoff=0)
view_menu = Menu(menu_bar, tearoff=0)
themes_menu = Menu(view_menu, tearoff=0)
about_menu = Menu(menu_bar, tearoff=0)



themes = {
	'Standard': 'white.black',
	'Auqamarine': 'teal.white',
	'Bold Beige': 'black.yellow',
	'Cobalt Blue': 'blue.white'
}





#####################################

# Function definitions

#####################################


def cut():
	content_text.event_generate("<<Cut>>")
def copy():
	content_text.event_generate("<<Copy>>")
def paste():
	content_text.event_generate("<<Paste>>")
def undo(event=None):
	content_text.event_generate("<<Undo>>")
	return 'break'
def redo(event=None):
	content_text.event_generate("<<Redo>>")
	return 'break'
def select_all(event=None):
	content_text.tag_add('sel', 1.0, END)
	return 'break'
def find_text(event=None):
	search_toplevel = Toplevel(root)
	search_toplevel.title("Find Text")
	search_toplevel.transient(root)
	search_toplevel.resizable(False, False)
	Label(search_toplevel, text="Find All:").grid(row=0, column=0, sticky='e')
	search_entry_widget = Entry(search_toplevel, width=25)
	search_entry_widget.grid(row=0, column=1, sticky='we')
	search_entry_widget.focus_set()
	ignore_case_value = IntVar()
	Checkbutton(search_toplevel, text='Ignore Case', variable=ignore_case_value).grid(row=1, column=1, sticky='e', padx=2, pady=2)
	Button(search_toplevel, text="Find All", underline=0, command=lambda: search_output(search_entry_widget.get(), ignore_case_value.get(), content_text, search_toplevel, search_entry_widget)).grid(row=0, column=2, sticky='e' + 'w', padx=2, pady=2)

	def close_search_window():
		content_text.tag_remove('match', '1.0', END)
		search_toplevel.destroy()
		return "break"
	search_toplevel.protocol('WM_DELETE_WINDOW', close_search_window)

def search_output(needle, if_ignore_case, content_text, search_toplevel, search_box):
		content_text.tag_remove('match', '1.0', END)
		matches_found = 0
		if needle:
			start_pos = '1.0'
			while True:
				start_pos = content_text.search(needle, start_pos, END, nocase=if_ignore_case)
				if not start_pos:
					break;
				end_pos = '{}+{}c'.format(start_pos, len(needle))
				content_text.tag_add('match', start_pos, end_pos)
				matches_found += 1
				start_pos = end_pos
			content_text.tag_config('match', foreground='red', background='yellow')
		search_box.focus_set()
		search_toplevel.title('{} matches found'.format(matches_found))

def open_file(event=None):
	input_file_name = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
	if input_file_name:
		global file_name
		file_name = input_file_name
		root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
		content_text.delete(1.0, END)
		with open(file_name) as _file:
			content_text.insert('1.0', _file.read())

def save(event=None):
	global file_name
	if not file_name:
		save_as()
	else:
		write_to_file(file_name)
	return "break"

def save_as(event=None):
	input_file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Types", "*.*"), ("Text Documents", "*.txt")])
	if input_file_name:
		global file_name
		file_name = input_file_name
		write_to_file(file_name)
		root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
	return "break"	


def write_to_file(file_name):
	content = content_text.get("1.0", END)
	try:
		with open(file_name, 'w') as _file:
			_file.write(content)
	except IOError:
		pass

def new_file(event=None):
	global file_name
	file_name = ""
	root.title("Untitled - {}".format(PROGRAM_NAME))
	content_text.delete('1.0', END)

def display_about_messagebox(event=None):
	messagebox.showinfo(title="Text Editor App", message="Made by Baraja Swargiary")

def display_help_messagebox(event=None):
	messagebox.showinfo(title="Help", message="Read some books on tkinter GUI programming to get help")

def display_exit_messagebox(event=None):
	if messagebox.askokcancel(message="Do you really want to quit?"):
		root.destroy()

def on_content_changed(event=None):
	update_line_numbers()
	update_cursor()

def get_line_numbers():
	line_numbers = ""
	if show_line_number.get():
		row, col = content_text.index('end').split('.')
		for i in range(1, int(row)):
			line_numbers += str(i) + '\n'
	return line_numbers


def update_line_numbers():
	line_numbers = get_line_numbers()
	line_number_bar.config(state='normal')
	line_number_bar.delete('1.0', END)
	line_number_bar.insert('1.0', line_numbers)
	line_number_bar.config(state='disabled')

def update_cursor():
	if show_cursor_info.get():
		current_position = content_text.index(INSERT).split('.')
		row, col = int(current_position[0]), int(current_position[1])+1
		cursor_info_bar.pack(side='right', expand=NO, fill=None, anchor='se')
		cursor_info_bar.config(text='Line: {0} | Column: {1}'.format(str(row), str(col)))
	else:
		cursor_info_bar.pack_forget()

def change_theme():
	bg, fg = themes[theme_option.get()].split(".")
	content_text.config(background=bg, foreground=fg)

def show_popup_menu(event):
	popup_menu.tk_popup(event.x_root, event.y_root)


menu_bar.add_cascade(label='File', menu=file_menu)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
menu_bar.add_cascade(label='View', menu=view_menu)
menu_bar.add_cascade(label='About', menu=about_menu)

file_menu.add_command(label='New', accelerator='Ctrl+N', compound='left', command=new_file)
file_menu.add_command(label='Open', accelerator='Ctrl+O', compound='left', command=open_file)
file_menu.add_command(label='Save', accelerator='Ctrl+S', compound='left', command=save)
file_menu.add_command(label='Save as', accelerator='Shift+Ctrl+S', compound='left', command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Exit', accelerator='Alt+F4', command=display_exit_messagebox)

edit_menu.add_command(label='Undo', accelerator='Ctrl+Z', command=undo)
edit_menu.add_command(label='Redo', accelerator='Ctrl+Y', command=redo)
edit_menu.add_command(label='Cut', accelerator='Ctrl+X', command=cut)
edit_menu.add_command(label='Copy', accelerator='Ctrl+C', command=copy)
edit_menu.add_command(label='Paste', accelerator='Ctrl+V', command=paste)
edit_menu.add_separator()
edit_menu.add_command(label='Find', accelerator='Ctrl+f', command=find_text)
edit_menu.add_separator()
edit_menu.add_command(label='Select All', accelerator='Ctrl+A', underline=7, command=select_all)


show_line_number = IntVar()
show_cursor_info = IntVar()
theme_option = StringVar()
theme_option.set('Standard')

view_menu.add_checkbutton(label='Show Line Number', variable=show_line_number, command=update_line_numbers)
view_menu.add_checkbutton(label='Show Cursor Location at Botton', variable=show_cursor_info, command=update_cursor)
view_menu.add_checkbutton(label='Highlight Current Line')

view_menu.add_cascade(label='Themes', menu=themes_menu)
themes_menu.add_radiobutton(label='Standard', variable=theme_option, value='Standard', command=change_theme)
themes_menu.add_radiobutton(label='Aquamarine', variable=theme_option, value='Aquamarine', command=change_theme)
themes_menu.add_radiobutton(label='Bold Beige', variable=theme_option, value='Bold Beige', command=change_theme)
themes_menu.add_radiobutton(label='Cobalt Blue', variable=theme_option, value='Cobalt Blue', command=change_theme)

about_menu.add_command(label='About', command=display_about_messagebox)
about_menu.add_command(label='Help', command=display_help_messagebox)


shortcut_bar = Frame(root, height=25, background="light sea green")
shortcut_bar.pack(expand='no', fill='x')

line_number_bar = Text(root, width=4, padx=3, takefocus=0, border=0, background='khaki', state='disabled', wrap='none')
line_number_bar.pack(side='left', fill='y')


content_text = Text(root, wrap="word", undo=1)



scroll_bar = Scrollbar(content_text, cursor='arrow')
scroll_bar.pack(side='right', fill='y')

cursor_info_bar = Label(content_text, text='Line: 1 | Column: 1', background='gray', fg='white')
cursor_info_bar.pack(side='right', expand=NO, fill=None, anchor='se')

content_text.pack(expand='yes', fill='both')

content_text.config(yscrollcommand=scroll_bar.set)
content_text.bind('<Control-z>', undo)
content_text.bind('<Control-Z>', undo)
content_text.bind('<Control-y>', redo)
content_text.bind('<Control-Y>', redo)
content_text.bind('<Control-a>', select_all)
content_text.bind('<Control-A>', select_all)
content_text.bind('<Control-F>', find_text)
content_text.bind('<Control-o>', open_file)
content_text.bind("<Control-n>", new_file)
content_text.bind('<Control-s>', save)
content_text.bind('<KeyPress-F1>', display_help_messagebox)
content_text.bind('<Any-KeyPress>', on_content_changed)
content_text.bind('<Button-3>', show_popup_menu)

scroll_bar.config(command=content_text.yview)



popup_menu = Menu(content_text, tearoff=0)
for i in ('cut', 'copy', 'paste', 'undo', 'redo'):
	cmd = eval(i)
	popup_menu.add_command(label=i, compound='left', command=cmd)
popup_menu.add_separator()
popup_menu.add_command(label='Select All', underline=7, command=select_all)



root.config(menu=menu_bar)


root.protocol('WM_DELETE_WINDOW', display_exit_messagebox)

root.mainloop()



