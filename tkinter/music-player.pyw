import pygame
import os
from tkinter import *
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox

class MusicPlayer():
	def __init__(self, title):
		pygame.init()
		self.root = Tk()
		self.root.title(title)
		self.root.geometry('500x250+400+200')

		self.frame1 = Frame(self.root)
		self.frame2 = Frame(self.root)
		self.frame3 = Frame(self.root)
		self.frame4 = Frame(self.root)

		self.filename = StringVar()
		self.status = StringVar()
		self.volume = IntVar()
		self.volume.set(25)
		self.status.set('No file loaded')
		self.paused = False
		self.file_loaded = False

		self.gui_init()
		self.root.protocol('WM_DELETE_WINDOW', self.exit_window)
		self.root.bind('<Control-o>', self.load_music_file)
		self.root.bind('<Alt-F4>', self.exit_window)
		self.root.bind(pygame.mixer.music.get_endevent(), self.exit_window)
		self.root.mainloop()


	def gui_init(self):
		self.init_menu_bar()
		self.init_main_components()
	
	def init_menu_bar(self):
		self.menu_bar = Menu(self.root)
		self.file_menu = Menu(self.menu_bar, tearoff=0)
		self.about_menu = Menu(self.menu_bar, tearoff=0)

		self.menu_bar.add_cascade(label='File', menu=self.file_menu)
		self.menu_bar.add_cascade(label='About', menu=self.about_menu)
		self.file_menu.add_command(label='Open', accelerator='Ctrl + o', command=self.open_file)
		self.file_menu.add_command(label='Exit', accelerator='Alt + F4', command=self.exit_window)
		self.about_menu.add_command(label='Credits', command=self.open_credits)
		self.about_menu.add_command(label='Help', command=self.open_help)
		self.root.config(menu=self.menu_bar)

	def init_main_components(self):
		Label(self.frame1, text='File name:').pack(side='left', padx=10, expand='no', fill='x', anchor='nw')
		Label(self.frame1, textvariable=self.filename, background='khaki', width=30).pack(side='left', expand='no', fill='x', anchor='nw')
		
		Button(self.frame2, width=10, text='Open File', command=self.load_music_file).pack(side='left', expand=True, fill='x', padx=10)
		Button(self.frame2, width=10, text='Play', command=self.play_music_file).pack(side='left', expand=True, fill='x', padx=10)
		Button(self.frame2, width=10, text='Pause', command=self.pause_music_file).pack(side='left', expand=True, fill='x', padx=10)
		Button(self.frame2, width=10, text='Stop', command=self.stop_music_file).pack(side='left', expand=True, fill='x', padx=10)

		Label(self.frame3, text='Volume: ').pack(side='left', anchor='s', fill='x', expand=True)
		self.volume_scale = Scale(self.frame3, from_=0, to=50, orient='horizontal', variable=self.volume, command=self.change_volume)
		self.volume_scale.pack(side='top', expand=True, fill='x')

		Label(self.frame4, text='Status:').pack(side='left', expand=True, pady=10)
		Label(self.frame4, textvariable=self.status, background='khaki').pack(side='left', pady=10, expand=True)


		self.frame1.pack(pady=20, padx=10)
		self.frame2.pack(pady=10, padx=10)
		self.frame3.pack(pady=10, padx=10)
		self.frame4.pack(pady=10, padx=10)

	def load_music_file(self, event=None):
		self.tempname = filedialog.askopenfilename()
		pygame.mixer.music.load(self.tempname)
		self.filename.set(os.path.basename(self.tempname))
		self.status.set("File ready to play")
		self.file_loaded = True
		pygame.mixer.music.set_endevent(1)
		self.volume.set(25)
		pygame.mixer.music.set_volume(self.volume.get()/50)

	def play_music_file(self):
		if self.has_file_loaded():
			if self.paused:
				pygame.mixer.music.unpause()
			elif self.status.get() != "Playing":
				pygame.mixer.music.play()
				
			self.status.set("Playing")

	def pause_music_file(self):
		if self.has_file_loaded():
			pygame.mixer.music.pause()
			self.paused = True
			self.status.set("Paused")

	def stop_music_file(self):
		if self.has_file_loaded():
			pygame.mixer.music.stop()
			self.paused = False
			self.status.set("Stopped")

	def open_file(self, event=None):
		self.load_music_file()

	def exit_window(self, event=None):
		self.tempname = messagebox.askokcancel(title='Exit Window', message='Exit Music Player?')
		if self.tempname == True:
			self.root.destroy()

	def open_credits(self, event=None):
		messagebox.showinfo(title='Credits', message='Made by Baraja')

	def open_help(self, event=None):
		messagebox.showinfo(title='Help', message='Open/Load a music file first before performing any action.\nThen use play/pause/stop buttons to control the music.\nIt is easy.')

	def has_file_loaded(self):
		if self.file_loaded:
			return True
		else:
			messagebox.showerror(title='File not found', message='Please load a music file before performing any action')
			return False

	def change_volume(self, event=None):
		pygame.mixer.music.set_volume(self.volume.get()/50)


music_player = MusicPlayer('Music Player')
