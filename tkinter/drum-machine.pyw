from tkinter import *
PROGRAM_NAME = 'Drum Machine'

#CONSTANTS

MAX_NUMBER_OF_PATTERNS = 10
MAX_NUMBER_OF_DRUM_SAMPLES = 5
MAX_BPU = 10
MAX_UNITS = 200
MAX_BEATS_PER_MINUTE = 500
INITIAL_NUMBER_OF_UNITS = 4
INITIAL_BPU = 4
INITIAL_BEATS_PER_MINUTE = 240

class DrumMachine:

	def __init__(self, root):
		self.root = root
		self.root.title(PROGRAM_NAME)
		self.root.geometry('800x400+300+150')
		#tkinter variables to keep track of the values
		self.current_pattern = IntVar()
		self.number_of_units = IntVar()
		self.bpu = IntVar()
		self.to_loop = BooleanVar()
		self.beats_per_minute = IntVar()
		self.current_pattern_text = StringVar()

		#Frames
		self.top_frame = None
		self.left_frame = None
		self.right_frame = None
		self.bottom_frame = None

		self.init_gui()
		#file menu and about
		self.menu_bar = Menu(self.root)
		self.file_menu = Menu(self.menu_bar, tearoff=False)
		self.about_menu = Menu(self.menu_bar, tearoff=False)

		self.menu_bar.add_cascade(label='File', menu=self.file_menu)
		self.menu_bar.add_cascade(label='About', menu = self.about_menu)

		self.file_menu.add_command(label='New')
		self.file_menu.add_command(label='Open')
		self.file_menu.add_command(label='Save')
		self.file_menu.add_command(label='Save as')

		self.about_menu.add_command(label='Credits')
		self.about_menu.add_command(label='Help')

		self.root.config(menu=self.menu_bar)

	def init_all_patterns(self):
		self.all_patterns = [
			{
				'list_of_drum_files': [None]*MAX_NUMBER_OF_DRUM_SAMPLES,
				'number_of_units': INITIAL_NUMBER_OF_UNITS,
				'bpu': INITIAL_BPU,
				'is_button_clicked_list': self.init_is_button_clicked_list(
					MAX_NUMBER_OF_DRUM_SAMPLES, 
					INITIAL_NUMBER_OF_UNITS * INITIAL_BPU	
				)
			} for i in range(MAX_NUMBER_OF_PATTERNS)
		]

	def init_is_button_clicked_list(self, num_of_rows, num_of_columns):
		return [[False]*num_of_columns for x in range(num_of_rows)]

	def init_gui(self):
		self.create_top_bar()
		self.create_play_bar()
		self.create_left_drum_loader()
		self.create_right_button_matrix()

	def create_top_bar(self):
		self.top_frame = Frame(self.root)
		self.current_pattern_text.set('Pattern '+ str(self.current_pattern.get()))
		Label(self.top_frame, text='Pattern Number:').pack(side='left', anchor='nw', expand=True)
		Spinbox(self.top_frame, width=5, from_=1, to=MAX_NUMBER_OF_PATTERNS, textvariable = self.current_pattern, command=self.on_bpu_changed).pack(side='left', anchor='w', expand=True)
		Entry(self.top_frame, textvariable=self.current_pattern_text).pack(side='left', expand=True)
		Label(self.top_frame, text='Number of Units:').pack(side='left', expand=True)
		Spinbox(self.top_frame, width=5, from_=1, to=MAX_UNITS, textvariable= self.number_of_units).pack(side='left', expand=True)
		Label(self.top_frame, text='BPUs').pack(side='left', expand=True)
		Spinbox(self.top_frame, from_=1, to=MAX_BPU, textvariable=self.bpu).pack(side='left', expand=True)

		self.top_frame.pack(side='top', fill='x', padx=20, pady=10)

	def create_left_drum_loader(self):
		self.left_frame = Frame(self.root)
		Entry(self.left_frame).pack(fill = 'x', expand=True)
		Entry(self.left_frame).pack(fill = 'x', expand=True)
		Entry(self.left_frame).pack(fill = 'x', expand=True)
		Entry(self.left_frame).pack(fill = 'x', expand=True)
		Entry(self.left_frame).pack(fill = 'x', expand=True)
		self.left_frame.pack(side='left', fill='y', expand=None, anchor='w', padx=20)

	def create_right_button_matrix(self):
		pass

	def create_play_bar(self):
		self.bottom_frame = Frame(self.root)
		Button(self.bottom_frame, width=15, text='Play').pack(side='left', expand=True)
		Button(self.bottom_frame, width=15, text='Stop').pack(side='left', expand=True)
		Checkbutton(self.bottom_frame, text='Loop').pack(side='left', expand=True)
		Label(self.bottom_frame, text='Beats Per Minute:').pack(side='left', expand=True)
		Spinbox(self.bottom_frame, from_=1, to=MAX_BEATS_PER_MINUTE, textvariable = self.beats_per_minute).pack(side='left', expand=True)
		self.bottom_frame.pack(side=BOTTOM, anchor='s', fill='x', pady=10)


	def on_bpu_changed(self):
		pass








if __name__ == '__main__':
	root = Tk()
	DrumMachine(root)
	root.mainloop()