import Tkinter as tk
import tkFont as tkf
import tkSimpleDialog
from tkFileDialog import askopenfilename
import tkFileDialog
import autocomplete as auto
import cohort

# create a class to build and manage the display
class DisplayApp:

    def __init__(self, width, height):

        # ===============create a tk object, which is the root window======================
        self.root = tk.Tk()

        # ====================width and height of the window=============================
        self.initDx = width
        self.initDy = height
        # =======================set up the geometry for the window=======================
        self.root.geometry( "%dx%d+50+30" % (self.initDx, self.initDy) )

        #=========================== set the title of the window============================
        self.root.title("Cohortylizer")

        #==========================set the maximum size of the window for resizing====================
        self.root.maxsize( 190, 500 )

        #===========GUI items==================================
        self.autocomplete=None
        self.listbox2=None
        self.textBox2=None
        self.provenanceList = []
        self.filename = ""
        self.coho = cohort.cohort()
        self.selectedList = []
        self.tempSelected = []
        # =========================setup the menus=================
#         self.importCSV()
        #========================global variable that remembers the selected values of listboxes==================

        # ==============================build the controls========================
        self.buildControls()

        # ==========================build the Canvas========================

        # =============================bring the window to the front=====================
        self.root.lift()

        # - ============================do idle events here to get actual canvas size====================
        self.root.update_idletasks()

        # ==================now we can ask the size of the canvas==================

        # ========================set up the key bindings====================
        self.setBindings()
        
        #=======================list of booleans for drawing rectangle======================
        
        #====================View object=========================================

    


    


    # build a frame and put controls in it
    def buildControls(self):

		### Control ###
		# ======================make a control frame on the right======================
		rightcntlframe = tk.Frame(self.root,bg='grey' )
		rightcntlframe.pack(side=tk.RIGHT, padx=2, pady=2, fill=tk.Y)

		
		open=tk.Button(rightcntlframe,text="Open File",command=self.importCSV)
		open.pack()

		#=================use a label to set the size of the right panel========================
		self.autocomplete = auto.AutocompleteEntry(self.provenanceList,rightcntlframe)
		self.listbox2=tk.Listbox(rightcntlframe,selectmode=tk.SINGLE, exportselection=0,width=15,height=5)
		

		self.textBox1=tk.Entry(rightcntlframe)
		self.textBox2=tk.Entry(rightcntlframe)


# ==================Name Entry=================
# 		label4 = tk.Label( rightcntlframe, text="Provenance Name", width=20,bg='grey',relief=tk.GROOVE )
# 		label4.pack( side=tk.TOP, pady=10 )
# 		self.textBox1.pack()
# ==============================================

# 		list=['BIN','HEX','DEC']
# 		for thing in list:
# 			self.listbox1.insert(tk.END,thing)
# 			self.listbox2.insert(tk.END,thing)
		label2 = tk.Label( rightcntlframe, text="Autocomplete Options", width=20,bg='grey',relief=tk.GROOVE )
		label2.pack( side=tk.TOP, pady=10 )
		self.autocomplete.pack()
		
		add=tk.Button(rightcntlframe,text="Add",command=self.add)
		add.pack()
		
		label3 = tk.Label( rightcntlframe, text="Current Cohort", width=20,bg='grey',relief=tk.GROOVE )
		label3.pack( side=tk.TOP, pady=10 )
		
		self.listbox2.pack()
		
		
		remove=tk.Button(rightcntlframe,text="Remove",command=self.remove)
		remove.pack()
		
		
		label5 = tk.Label( rightcntlframe, text="Cohort Name", width=20,bg='grey',relief=tk.GROOVE )
		label5.pack( side=tk.TOP, pady=10 )
		
		self.textBox2.pack()
		generate=tk.Button(rightcntlframe,text="Press to Generate",command=self.generate)
		generate.pack()
		


		#==================changes the color of the points========================
# 		button3 = tk.Button( rightcntlframe, text="Dialog Box",command=self.dialogBox)
# 		button3.pack(side=tk.TOP)


    #sets the key bindings
    def setBindings(self):

        # =================bind command sequences to the root window===============
        self.root.bind( '<Command-q>', self.handleQuit )
        
    #applies quit to the canvas
    def handleQuit(self, event=None):
        print 'Terminating'
        self.root.destroy()
        
    
#     Opens the file, at this time is specific to the
    def importCSV( self, event = None ):
        print 'opening file'

        # preventative bug measure
        try:
            filename = askopenfilename(parent = self.root, title='Choose a data file', initialdir='.')
            self.coho.data_init( filename )
            self.autocomplete.lista = self.coho.provenance_list

        except IOError:
            return

        self.filename = filename
        
#     adds to the cohort listbox
    def add(self):
    	self.tempSelected = []
    	temp = self.autocomplete.get()
    	if (temp in self.selectedList) == False:
    		self.selectedList.append(temp)
    		self.tempSelected.append(temp)
    		self.manageListBox()
    	print self.selectedList
        
#     Ensures the cohort representation is current
    def manageListBox(self):
    	for thing in self.tempSelected:
    		self.listbox2.insert(tk.END,thing)
	
# 	removes elements from the cohort list box
    def remove(self):
		if len(self.selectedList) > 0:
			temp = self.listbox2.curselection()
			idx = int(temp[0])
			self.selectedList.pop(idx)
			self.listbox2.delete(idx)
	
# 	Generates the new file
    def generate(self):
    	temp = self.textBox2.get()
    	if(len(temp)>0):
    		self.coho.cohort_name = temp
    		self.coho.provenance_list = self.selectedList
    		self.coho.identify_cohorts()
    
		
    
    	
 
        

   

    
        
        
     
    #main method
    def main(self):
        print 'Entering main loop'
        self.root.mainloop()

if __name__ == "__main__":
    dapp = DisplayApp(500, 500)
    dapp.main()
    


