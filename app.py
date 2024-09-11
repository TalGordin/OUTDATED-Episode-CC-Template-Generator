import tkinter
from tkinter import *
from tkinter import ttk
import random
import time
import assets

def defineAppColors():
    random.seed(time.time())
    global appColor
    global titleImg
    global buttonColor
    global buttonBorderWidth
    global buttonStyle
    global entryColor

    buttonBorderWidth = 1
    buttonStyle = 'solid'

    appColor = random.choice(["#ffbdc7", "#C0ECFC", "#FFFF99"])
    root.config(bg=appColor)
    if appColor == "#ffbdc7":
        titleImg = PhotoImage(file='logo.pink.png')
        buttonColor = "#ff9cab"
        entryColor = '#ffcfd6'
    elif appColor == "#C0ECFC":
        titleImg = PhotoImage(file='logo.blue.png')
        buttonColor = "#88d6f2"
        entryColor = '#cff2ff'
    else:
        titleImg = PhotoImage(file='logo.yellow.png')
        buttonColor = "#ffff7d"
        entryColor = '#fcfcc0'

    global title
    title = Label(root, image=titleImg, bg=appColor, bd=0, highlightthickness=0, padx=0, pady=0)
    title.pack(fill='both', expand=True)

    global scrollbar_style
    scrollbar_style = ttk.Style()
    scrollbar_style.configure("My.Vertical.TScrollbar", troughcolor=buttonColor, background=entryColor)

class Dropdown(ttk.Combobox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class Checkbox(tkinter.Checkbutton):
    def __init__(self, master, text, id, initial_value=False, **kwargs):
        self.var = tkinter.BooleanVar(value=initial_value)
        super().__init__(master, text=text, variable=self.var, **kwargs)
        self.id = id
        self.var.trace_add("write", self.toggle)

    def get_value(self):
        return self.var.get()

    def set_value(self, value):
        self.var.set(value)

    def toggle(self, *args):
        self.set_value(self.get_value())
        # print("checkbox is now" , self.get_value())

def styleButton(button, size = 'normal'):
    button.config(font=('Calibri', 15, "normal"),
                  borderwidth=buttonBorderWidth,
                  relief=buttonStyle,
                  activebackground = buttonColor,
                  bg = appColor,
                  height=0, width=25
                  )
    if size == 'small':
        button.config(width = 0)
def styleEntry(entry, size=15):
    entry.config(font=('Calibri', size, "normal"),
                 bg = entryColor)
def styleDropdown(d, size=14):
    style=ttk.Style()
    style.theme_use('clam')
    style.configure('TCombobox', fieldbackground=entryColor, selectforeground=entryColor)
    d.config(font=('Calibri', size, "normal"))
def styleCheckbox(cb):
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TCombobox', fieldbackground=entryColor, selectforeground=entryColor)
    cb.config(font=('Calibri', 14, "normal"), bg=appColor, activebackground=appColor)
def styleLabel(label, size=15):
    label.config(font=('Calibri', size, "normal"),
                  bg = appColor,
                  wraplength = 700
                  )

def startGUI():
    global root
    root = Tk()
    root.title("Character Customization Template Creator")
    x = root.winfo_screenwidth() // 4
    y = int(root.winfo_screenheight() * 0.1)
    root.geometry('700x550+' + str(x) + '+' + str(y))
    root.attributes('-alpha', 1)
    root.resizable(False, False)
    defineAppColors()

    tkinter_mainMenu()
    root.mainloop()

def tkinter_clearScreen():
    for widget in root.winfo_children():
        if widget != title:
            widget.destroy()

def tkinter_mainMenu():
    tkinter_clearScreen()

    mainFrame = Frame(root)
    mainFrame.configure(bg=appColor)
    mainLabel = Label(mainFrame, text='Choose an action:')
    styleLabel(mainLabel)

    b1 = Button(mainFrame, text='Manage Templates',
                command = tkinter_templatesMenu)
    b2 = Button(mainFrame, text='Manage Assets',
                command = tkinter_assetsMenu)
    b3 = Button(mainFrame, text='Help',
                command = tkinter_helpMenu)
    b0 = Button(mainFrame, text='Save & Exit',
                command = lambda: root.destroy())

    styleButton(b1)
    styleButton(b2)
    styleButton(b3)
    styleButton(b0)

    mainLabel.pack(pady=2)
    b1.pack(pady=2)
    b2.pack(pady=2)
    b3.pack(pady=2)
    b0.pack(pady=2)
    mainFrame.pack(fill="both", expand=True)

def tkinter_templatesMenu():
    tkinter_clearScreen()

    templatesFrame = Frame(root)
    templatesFrame.configure(bg=appColor)
    templatesLabel = Label(templatesFrame, text='Choose an action:')
    styleLabel(templatesLabel)

    b4 = Button(templatesFrame, text='Create a new template', command = tkinter_addNewTemplate)
    b5 = Button(templatesFrame, text='Edit an existing template', command=tkinter_editTemplate)
    b6 = Button(templatesFrame, text='Delete all existing templates')
    b7 = Button(templatesFrame, text='Back to main menu',
                command = tkinter_mainMenu)

    styleButton(b4)
    styleButton(b5)
    styleButton(b6)
    styleButton(b7)

    templatesLabel.pack(pady=2)
    b4.pack(pady=2)
    b5.pack(pady=2)
    b6.pack(pady=2)
    b7.pack(pady=2)
    templatesFrame.pack(fill="both", expand=True)
def tkinter_assetsMenu():
    tkinter_clearScreen()

    assetsFrame = Frame(root)
    assetsFrame.configure(bg=appColor)
    assetsLabel = Label(assetsFrame, text='Choose an action:')
    styleLabel(assetsLabel)

    b8 = Button(assetsFrame, text='Add a new asset',
                command = tkinter_addNewAsset)
    b9 = Button(assetsFrame, text='View all assets',
                command = tkinter_viewAllAssets)
    b12 = Button(assetsFrame, text='Edit an asset',
                 command=tkinter_editAsset)
    b10 = Button(assetsFrame, text='Delete an asset',
                 command=tkinter_deleteAsset)
    b11 = Button(assetsFrame, text='Back to main menu',
                 command = tkinter_mainMenu)

    styleButton(b8)
    styleButton(b9)
    styleButton(b10)
    styleButton(b11)
    styleButton(b12)

    assetsLabel.pack(pady=2)
    b8.pack(pady=2)
    b12.pack(pady=2)
    b10.pack(pady=2)
    b9.pack(pady=2)
    b11.pack(pady=2)
    assetsFrame.pack(fill="both", expand=True)

def tkinter_helpMenu():
    tkinter_clearScreen()

    helpFrame = Frame(root)
    helpFrame.configure(bg=appColor)
    l1 = Label(helpFrame, text='Click "manage templates" to add new CC templates or make changes to existing ones.')
    l2 = Label(helpFrame, text='''Click "manage assets" to add or remove assets from the program's database''')
    b12 = Button(helpFrame, text='Got it!',
                 command = tkinter_mainMenu)

    styleLabel(l1)
    styleLabel(l2)
    styleButton(b12, 'small')

    l1.pack(pady=5)
    l2.pack(pady=5)
    b12.pack(pady=5)
    helpFrame.pack(fill="both", expand=True)

def tkinter_addNewTemplate():
    tkinter_clearScreen()

    def addNewTemplate_continue():
        error = Label(frame, fg='red')
        styleLabel(error)

        temp_name = e1.get()
        MC_name = e2.get()
        gender = c1.get()

        if temp_name == '':
            error.config(text="Template name can't be empty!")
            error.grid(row=2, column=0)
        elif MC_name == '':
            error.config(text="MC script name can't be empty!")
            error.grid(row=2, column=0)
        elif not assets.isOriginalTemplate(temp_name):
            error.config(text="A template with this name already exists!")
            error.grid(row=2, column=0)
        elif gender == '':
            error.config(text="Please specify MC's gender!")
            error.grid(row=2, column=0)
        else:
            assets.CreateNewTemplate(temp_name, MC_name, gender)
            open_popup("Successfully created template!")
            tkinter_templatesMenu()



    frame = Frame(root)
    frame.configure(bg=appColor)
    frame.pack(fill="both", expand=True)

    grid = Frame(frame)
    grid.grid(row = 0, column = 0, padx=240)
    grid.configure(bg = appColor)
    grid0 = Frame(frame)
    grid0.grid(row=1, column=0, pady = 10)
    grid0.configure(bg=appColor)

    l1 = Label(grid, text='Add a new template:')
    l2 = Label(grid, text='Template name')
    e1 = Entry(grid)
    l3 = Label(grid, text='MC script name')
    e2 = Entry(grid)
    l4 = Label(grid, text="MC's gender")
    c1 = ttk.Combobox(grid, values = ["Female", "Male"], state='readonly')
    c1.set('')
    b1 = Button(grid0, text='Cancel', command=tkinter_templatesMenu)
    b2 = Button(grid0, text='Done', command=addNewTemplate_continue)

    styleLabel(l1)
    styleLabel(l2)
    styleLabel(l3)
    styleLabel(l4)
    styleEntry(e1)
    styleEntry(e2)
    styleDropdown(c1)
    styleButton(b1, 'small')
    styleButton(b2, 'small')

    l1.grid(row=0, column=1, pady=(0,10))
    l2.grid(row=1, column=1)
    e1.grid(row=2, column=1)
    l3.grid(row=3, column=1)
    e2.grid(row=4, column=1)
    l4.grid(row=5, column=1)
    c1.grid(row=6, column=1)
    b1.grid(row=7, column=0, padx = 5, pady=10)
    b2.grid(row=7, column=1, padx = 5, pady=10)

def tkinter_editTemplate():
    tkinter_clearScreen()

    def showTemplateMenu(template):
        temp_info = assets.getTemplate(template)
        mc_info = assets.getCharacter(temp_info[2])

        tkinter_clearScreen()

        frame = Frame(root)
        frame.configure(bg=appColor)
        frame.pack(fill="both", expand=True)

        frame1 = Frame(frame)
        frame1.configure(bg=appColor)
        frame1.pack(fill="both", expand=True)

        frame2 = Frame(frame)
        frame2.configure(bg=appColor)
        frame2.pack(fill="both", expand=True)

        title_text = temp_info[1] + " (MC: " + mc_info[1] + ")"
        title = Label(frame1, text=title_text)
        styleLabel(title, 17)
        title.pack()

        manage_cat = Button(frame2, text="Manage Categories",
                            command=lambda: templateCategories(temp_info, mc_info, frame2))
        styleButton(manage_cat)
        manage_cat.pack(pady=2)

        manage_sub = Button(frame2, text='Manage Subcategories',
                            command=lambda: templateSubcategories(temp_info, mc_info, frame2))
        styleButton(manage_sub)
        manage_sub.pack(pady=2)

        manage_ast = Button(frame2, text="Manage Assets",
                            command=lambda: templateAssets(temp_info, mc_info, frame2))
        styleButton(manage_ast)
        manage_ast.pack(pady=2)

        manage_fam = Button(frame2, text='Manage Relatives',
                            command=lambda: templateRelatives(temp_info, mc_info, frame2))
        styleButton(manage_fam)
        manage_fam.pack(pady=2)

        back2 = Button(frame2, text='Go Back', command=tkinter_editTemplate)
        styleButton(back2, "small")
        back2.pack(pady=2)

    def chosenTemplate(event):
        showTemplateMenu(choose_temp.get())


    def templateCategories(temp_info, mc_info, frame):
        pass
    def templateSubcategories(temp_info, mc_info, frame):
        pass
    def templateAssets(temp_info, mc_info, frame):
        pass
    def templateRelatives(temp_info, mc_info, frame):

        def addNewRelative():
            for widget in frame.winfo_children():
                widget.destroy()

            l4 = Label(frame, text="New relative's script name:")
            name = Entry(frame)
            l5 = Label(frame, text="Gender:")
            gender = Dropdown(frame, values=['Male', 'Female'], state='readonly')
            back3 = Button(frame, text="Go back", command=lambda: showTemplateMenu(temp_info[1]))

            styleLabel(l4)
            styleEntry(name)
            styleLabel(l5)
            styleDropdown(gender)
            styleButton(back3, "small")
            l4.pack()
            name.pack()
            l5.pack()
            gender.pack()
            back3.pack()

        def editRelative():
            name = choose_char.get()
            relative = assets.getCharacterByName(name)
            print("id = ", relative[0])

        for widget in frame.winfo_children():
            widget.destroy()

        relative = Frame(frame)
        relative.configure(bg=appColor)
        relative.pack(fill="both", expand=True)

        relatives_info = assets.getRelatives(temp_info[0], temp_info[2])
        relatives = []
        for char in relatives_info:
            relatives.append(char[1])

        l2=Label(relative, text="Choose a relative:")
        styleLabel(l2)
        l2.pack()
        choose_char = Dropdown(relative, values=relatives, state='readonly')
        styleDropdown(choose_char)
        choose_char.pack()
        l3 = Label(relative, text="or")
        styleLabel(l3)
        l3.pack()
        new_char = Button(relative, text="Create a new relative", command=addNewRelative)
        styleButton(new_char)
        new_char.pack(pady=5)
        back2 = Button(relative, text="Go Back", command=lambda: showTemplateMenu(temp_info[1]))
        styleButton(back2, 'small')
        back2.pack(pady=8)

        choose_char.bind('<<ComboboxSelected>>', editRelative)


    frame = Frame(root)
    frame.configure(bg=appColor)
    frame.pack(fill="both", expand=True)

    l1 = Label(frame, text="Select a template to edit:")
    styleLabel(l1)
    l1.pack()

    templates_list = assets.getTemplateNames()
    choose_temp = Dropdown(frame, state='readonly', values=templates_list)
    styleDropdown(choose_temp)
    choose_temp.pack()

    back1 = Button(frame, text="Go Back", command=tkinter_templatesMenu)
    styleButton(back1, "small")
    back1.pack(pady=20)

    choose_temp.bind("<<ComboboxSelected>>", chosenTemplate)

def tkinter_addNewAsset():
    tkinter_clearScreen()

    def showSubcategories(event):
        l8.grid_forget()
        for widget in grid2.winfo_children():
            widget.destroy()

        bodyColor_light = Checkbox(grid2, text='Light', id=1)
        bodyColor_medium = Checkbox(grid2, text='Medium', id=2)
        bodyColor_dark = Checkbox(grid2, text='Dark', id=3)
        bodyColor_ash = Checkbox(grid2, text='Ash', id=4)
        bodyColor_copper = Checkbox(grid2, text='Copper', id=5)
        bodyColor_gold = Checkbox(grid2, text='Gold', id=6)
        bodyColor_neutral = Checkbox(grid2, text='Neutral', id=7)
        bodyColor_rose = Checkbox(grid2, text='Rose', id=8)

        hair_short = Checkbox(grid2, text='Short', id=9)
        hair_medium = Checkbox(grid2, text='Medium', id=10)
        hair_long = Checkbox(grid2, text='Long', id=11)
        hair_updo = Checkbox(grid2, text='Updo', id=12)
        hair_straight = Checkbox(grid2, text='Straight', id=13)
        hair_wavy = Checkbox(grid2, text='Wavy', id=14)
        hair_curly = Checkbox(grid2, text='Curly', id=15)
        hair_coily = Checkbox(grid2, text='Coily', id=16)

        hairColor_natural = Checkbox(grid2, text='Natural', id=17)
        hairColor_dyed = Checkbox(grid2, text='Dyed', id=18)
        hairColor_blacks = Checkbox(grid2, text='Blacks', id=19)
        hairColor_browns = Checkbox(grid2, text='Browns', id=20)
        hairColor_blonds = Checkbox(grid2, text='Blonds', id=21)
        hairColor_reds = Checkbox(grid2, text='Reds', id=22)
        hairColor_pinks = Checkbox(grid2, text='Pinks', id=23)
        hairColor_purples = Checkbox(grid2, text='Purples', id=24)
        hairColor_blues = Checkbox(grid2, text='Blues', id=25)
        hairColor_greens = Checkbox(grid2, text='Greens/Yellows', id=26)
        hairColor_whites = Checkbox(grid2, text='Whites/Grays', id=27)

        face_smooth = Checkbox(grid2, text='Smooth', id=28)
        face_hairy = Checkbox(grid2, text='Hairy', id=29)
        face_mature = Checkbox(grid2, text='Mature', id=30)

        eyes_double = Checkbox(grid2, text='Double Eyelid', id=31)
        eyes_mono = Checkbox(grid2, text='Monolid', id=32)

        eyesColor_natural = Checkbox(grid2, text='Natural', id=33)
        eyesColor_fantasy = Checkbox(grid2, text='Fantasy', id=34)
        eyesColor_brown = Checkbox(grid2, text='Brown', id=35)
        eyesColor_blue = Checkbox(grid2, text='Blue', id=36)
        eyesColor_green = Checkbox(grid2, text='Green/Gray', id=37)

        eyebrowsColor_natural = Checkbox(grid2, text='Natural', id=38)
        eyebrowsColor_dyed = Checkbox(grid2, text='Dyed', id=39)
        eyebrowsColor_blacks = Checkbox(grid2, text='Blacks', id=40)
        eyebrowsColor_browns = Checkbox(grid2, text='Browns', id=41)
        eyebrowsColor_blonds = Checkbox(grid2, text='Blonds', id=42)
        eyebrowsColor_reds = Checkbox(grid2, text='Reds', id=43)
        eyebrowsColor_misc = Checkbox(grid2, text='Misc.', id=44)

        mouth_thin = Checkbox(grid2, text='Thin', id=45)
        mouth_full = Checkbox(grid2, text='Full', id=46)
        mouth_human = Checkbox(grid2, text='Human', id=47)
        mouth_vampire = Checkbox(grid2, text='Vampire', id=48)

        mouthColor_natural = Checkbox(grid2, text='Natural', id=49)
        mouthColor_gloss = Checkbox(grid2, text='Gloss', id=50)
        mouthColor_matte = Checkbox(grid2, text='Matte', id=51)
        mouthColor_nudes = Checkbox(grid2, text='Nudes', id=52)
        mouthColor_browns = Checkbox(grid2, text='Browns', id=53)
        mouthColor_reds = Checkbox(grid2, text='Reds', id=54)
        mouthColor_pinks = Checkbox(grid2, text='Pinks', id=55)
        mouthColor_purples = Checkbox(grid2, text='Purples', id=56)
        mouthColor_misc = Checkbox(grid2, text='Misc.', id=57)

        chosenCategory = c2.get()
        if chosenCategory == 'bodyColor':
            styleCheckbox(bodyColor_light)
            styleCheckbox(bodyColor_medium)
            styleCheckbox(bodyColor_dark)
            styleCheckbox(bodyColor_ash)
            styleCheckbox(bodyColor_copper)
            styleCheckbox(bodyColor_gold)
            styleCheckbox(bodyColor_neutral)
            styleCheckbox(bodyColor_rose)

            l8.grid(row=6, column=1)
            bodyColor_light.grid(row=1, column=0, sticky='w')
            bodyColor_medium.grid(row=1, column=1, sticky='w')
            bodyColor_dark.grid(row=1, column=3, sticky='w')
            bodyColor_ash.grid(row=1, column=4, sticky='w')
            bodyColor_copper.grid(row=2, column=0, sticky='w')
            bodyColor_gold.grid(row=2, column=1, sticky='w')
            bodyColor_neutral.grid(row=2, column=3, sticky='w')
            bodyColor_rose.grid(row=2, column=4, sticky='w')
        elif chosenCategory == 'hair':
            styleCheckbox(hair_short)
            styleCheckbox(hair_medium)
            styleCheckbox(hair_long)
            styleCheckbox(hair_updo)
            styleCheckbox(hair_straight)
            styleCheckbox(hair_wavy)
            styleCheckbox(hair_curly)
            styleCheckbox(hair_coily)

            l8.grid(row=6, column=1)
            hair_short.grid(row=1, column=0, sticky='w')
            hair_medium.grid(row=1, column=1, sticky='w')
            hair_long.grid(row=1, column=3, sticky='w')
            hair_updo.grid(row=1, column=4, sticky='w')
            hair_straight.grid(row=2, column=0, sticky='w')
            hair_wavy.grid(row=2, column=1, sticky='w')
            hair_curly.grid(row=2, column=3, sticky='w')
            hair_coily.grid(row=2, column=4, sticky='w')

        elif chosenCategory == 'hairColor':
            styleCheckbox(hairColor_natural)
            styleCheckbox(hairColor_dyed)
            styleCheckbox(hairColor_blacks)
            styleCheckbox(hairColor_browns)
            styleCheckbox(hairColor_blonds)
            styleCheckbox(hairColor_reds)
            styleCheckbox(hairColor_pinks)
            styleCheckbox(hairColor_purples)
            styleCheckbox(hairColor_blues)
            styleCheckbox(hairColor_greens)
            styleCheckbox(hairColor_whites)

            l8.grid(row=6, column=1)
            hairColor_natural.grid(row=1, column=0, sticky='w')
            hairColor_dyed.grid(row=1, column=1, sticky='w')
            hairColor_blacks.grid(row=1, column=3, sticky='w')
            hairColor_browns.grid(row=1, column=4, sticky='w')
            hairColor_blonds.grid(row=2, column=0, sticky='w')
            hairColor_reds.grid(row=2, column=1, sticky='w')
            hairColor_pinks.grid(row=2, column=3, sticky='w')
            hairColor_purples.grid(row=2, column=4, sticky='w')
            hairColor_blues.grid(row=3, column=0, sticky='w')
            hairColor_greens.grid(row=3, column=1, sticky='w')
            hairColor_whites.grid(row=3, column=3, sticky='w')
        elif chosenCategory == 'face':
            styleCheckbox(face_smooth)
            styleCheckbox(face_hairy)
            styleCheckbox(face_mature)

            l8.grid(row=6, column=1)
            face_smooth.grid(row=1, column=0, sticky='w')
            face_hairy.grid(row=1, column=1, sticky='w')
            face_mature.grid(row=1, column=2, sticky='w')
        elif chosenCategory == 'eyes':
            styleCheckbox(eyes_double)
            styleCheckbox(eyes_mono)

            l8.grid(row=6, column=1)
            eyes_double.grid(row=1, column=0, sticky='w')
            eyes_mono.grid(row=1, column=1, sticky='w')
        elif chosenCategory == 'eyesColor':
            styleCheckbox(eyesColor_natural)
            styleCheckbox(eyesColor_fantasy)
            styleCheckbox(eyesColor_brown)
            styleCheckbox(eyesColor_blue)
            styleCheckbox(eyesColor_green)

            l8.grid(row=6, column=1)
            eyesColor_natural.grid(row=1, column=0, sticky='w')
            eyesColor_fantasy.grid(row=1, column=1, sticky='w')
            eyesColor_brown.grid(row=1, column=3, sticky='w')
            eyesColor_blue.grid(row=1, column=4, sticky='w')
            eyesColor_green.grid(row=2, column=0, sticky='w')
        elif chosenCategory == 'eyebrowsColor':
            styleCheckbox(eyebrowsColor_natural)
            styleCheckbox(eyebrowsColor_dyed)
            styleCheckbox(eyebrowsColor_blacks)
            styleCheckbox(eyebrowsColor_browns)
            styleCheckbox(eyebrowsColor_blonds)
            styleCheckbox(eyebrowsColor_reds)
            styleCheckbox(eyebrowsColor_misc)

            l8.grid(row=6, column=1)
            eyebrowsColor_natural.grid(row=1, column=0, sticky='w')
            eyebrowsColor_dyed.grid(row=1, column=1, sticky='w')
            eyebrowsColor_blacks.grid(row=1, column=3, sticky='w')
            eyebrowsColor_browns.grid(row=1, column=4, sticky='w')
            eyebrowsColor_blonds.grid(row=2, column=0, sticky='w')
            eyebrowsColor_reds.grid(row=2, column=1, sticky='w')
            eyebrowsColor_misc.grid(row=2, column=3, sticky='w')
        elif chosenCategory == 'mouth':
            styleCheckbox(mouth_thin)
            styleCheckbox(mouth_full)
            styleCheckbox(mouth_human)
            styleCheckbox(mouth_vampire)

            l8.grid(row=6, column=1)
            mouth_thin.grid(row=1, column=0)
            mouth_full.grid(row=1, column=1)
            mouth_human.grid(row=1, column=3)
            mouth_vampire.grid(row=1, column=4)
        elif chosenCategory == 'mouthColor':
            styleCheckbox(mouthColor_natural)
            styleCheckbox(mouthColor_gloss)
            styleCheckbox(mouthColor_matte)
            styleCheckbox(mouthColor_nudes)
            styleCheckbox(mouthColor_browns)
            styleCheckbox(mouthColor_reds)
            styleCheckbox(mouthColor_pinks)
            styleCheckbox(mouthColor_purples)
            styleCheckbox(mouthColor_misc)

            l8.grid(row=6, column=1)
            mouthColor_natural.grid(row=1, column=0, sticky='w')
            mouthColor_gloss.grid(row=1, column=1, sticky='w')
            mouthColor_matte.grid(row=1, column=3, sticky='w')
            mouthColor_nudes.grid(row=1, column=4, sticky='w')
            mouthColor_browns.grid(row=2, column=0, sticky='w')
            mouthColor_reds.grid(row=2, column=1, sticky='w')
            mouthColor_pinks.grid(row=2, column=3, sticky='w')
            mouthColor_purples.grid(row=2, column=4, sticky='w')
            mouthColor_misc.grid(row=3, column=0, sticky='w')

    global addNewAssetFrame
    addNewAssetFrame = Frame(root)
    addNewAssetFrame.configure(bg = appColor)

    grid1 = Frame(addNewAssetFrame)
    grid1.grid(row = 0, column = 0, padx=65)
    grid1.configure(bg = appColor)
    global grid2
    grid2 = Frame(addNewAssetFrame)
    grid2.grid(row = 1, column = 0, padx=65)
    grid2.configure(bg=appColor)
    grid3 = Frame(addNewAssetFrame)
    grid3.grid(row = 2, column = 0, padx=65)
    grid3.configure(bg=appColor)

    l3 = Label(grid1, text='Add a new asset:')
    l4 = Label(grid1, text='Script Name')
    l5 = Label(grid1, text='Display Name')
    e1 = Entry(grid1)
    e2 = Entry(grid1)
    l6 = Label(grid1, text='Gender')
    c1 = Dropdown(grid1, values = ["Female", "Male", "Both"], state="readonly")
    c1.set('')
    l7 = Label(grid1, text='Category')
    global l8
    l8 = Label(grid1, text='Subcategories:')
    categories = assets.getCategories()
    global c2
    c2 = Dropdown(grid1, values = categories, state="readonly")
    c2.set('')
    c2.bind('<<ComboboxSelected>>', showSubcategories)

    styleLabel(l3)
    styleLabel(l4)
    styleLabel(l5)
    styleEntry(e1)
    styleEntry(e2)
    styleLabel(l6)
    styleLabel(l7)
    styleDropdown(c1)
    styleDropdown(c2)
    styleLabel(l8)

    l3.grid(row = 0, column = 1)
    l4.grid(row = 2, column = 0)
    l5.grid(row = 2, column = 2)
    e1.grid(row = 3, column = 0)
    e2.grid(row = 3, column = 2)
    l6.grid(row=4, column=0)
    l7.grid(row=4, column=2)
    c1.grid(row = 5, column = 0)
    c2.grid(row = 5, column = 2)

    b12=Button(grid3, text='Discard', command= tkinter_assetsMenu)
    b13 = Button(grid3, text='Save', command=lambda: tkinter_addNewAsset_confirm(e1, e2, c1, c2, categories))

    styleButton(b12, 'small')
    styleButton(b13, 'small')

    b12.grid(row=0, column=0, padx = 10, pady=5)
    b13.grid(row=0, column=1, padx = 10, pady=5)
    addNewAssetFrame.pack(fill="both", expand=True)

    def tkinter_addNewAsset_confirm(e1, e2, c1, c2, categories):
        errorFrame = Frame(addNewAssetFrame)
        errorFrame.grid(row=5, column=0)
        errorLabel = Label(errorFrame)
        styleLabel(errorLabel)
        errorLabel.config(fg='#FF0000')

        if e1.get() == '':
            errorLabel.config(text="Script Name can't be empty!")
            errorLabel.grid(row=0, column=0)
        elif e2.get() == '':
            errorLabel.config(text="Display Name can't be empty!")
            errorLabel.grid(row=0, column=0)
        elif c1.get() != 'Female' and c1.get() != 'Male' and c1.get() != 'Both':
            errorLabel.config(text="Gender can't be empty!")
            errorLabel.grid(row=0, column=0)
        elif c2.get() not in categories:
            errorLabel.config(text="Category can't be empty!")
            errorLabel.grid(row=0, column=0)
        elif not assets.isOriginalAsset(e1.get(), c2.get(), c1.get()):
            errorLabel.config(text="An asset with this script name already exists for this category and gender!")
            errorLabel.grid(row=0, column=0)
        else:
            errorLabel.destroy()

            script_name = e1.get()
            display_name = e2.get()
            genders = c1.get()
            cat = c2.get()

            subcategories = []
            for widget in grid2.winfo_children():
                if widget.winfo_viewable() and widget.get_value():
                    subcategories.append(widget.id)

            assets.addAsset(script_name, display_name, genders, cat, subcategories)
            open_popup("Asset successfully created.")
            tkinter_assetsMenu()
def tkinter_viewAllAssets():
    def on_mousewheel(event):
         # Get the direction of the mouse wheel (up or down)
        if event.delta > 0:
            canvas.yview_scroll(-1, "units")
        else:
            canvas.yview_scroll(1, "units")

    allAssets = assets.getAllAssets()

    tkinter_clearScreen()

    #Create a main frame
    main_frame = Frame(root)
    main_frame.configure(bg=appColor)
    main_frame.pack(fill=BOTH, expand = True)
    #Create a canvas
    canvas = Canvas(main_frame, bg=appColor, borderwidth=0, highlightthickness=0, height=150)
    #Add a scrollbar on main frame
    scroll=ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview, style="My.Vertical.TScrollbar")
    #Config canvas
    canvas.configure(yscrollcommand=scroll.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind("<MouseWheel>", on_mousewheel)
    #Create inner frame
    text = Frame(canvas, bg=appColor)
    #Add inner frame to canvas
    canvas.create_window((350,0), window=text, anchor='center', width=700)
    #insert text
    for key, value in allAssets.items():
        title=Label(text, text=key + ":")
        styleLabel(title)
        title.config(font=('Calibri', 15, "bold"))
        title.pack()

        value_str = "\n".join(value) + '\n'
        values = Label(text, text=value_str)
        styleLabel(values)
        values.config(font=('Calibri', 14, "normal"))
        values.pack(fill='both', expand=True)

    back = Button(main_frame, text="Done", command=tkinter_assetsMenu)
    styleButton(back, "small")
    back.pack(side=BOTTOM, pady=10)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scroll.pack(side=RIGHT, fill=Y)
    canvas.update_idletasks()
    canvas.yview_moveto(0)
def tkinter_deleteAsset():
    tkinter_clearScreen()

    frame = Frame(root)
    frame.configure(bg=appColor)
    frame.pack(fill="both", expand=True)

    warning = Label(frame, text="Warning: Deleting assets will affect all templates in the system and cannot be undone."
                                "\nConsider disabling them in your template instead.", fg='#FF0000')
    styleLabel(warning, 14)
    warning.pack(pady=10)

    notice = Label(frame, text="Notice: Only assets you've added to the system can be deleted and will be displayed.")
    styleLabel(notice, 14)
    notice.pack(pady=(0, 30))

    grid=Frame(frame)
    grid.configure(bg=appColor)
    grid.pack()

    l1=Label(grid, text="In category:")
    styleLabel(l1)
    l1.grid(row=0, column=0, padx=20)
    cats = ["Body Type (Female)", "Body Type (Male)", "Skin Tone", "Hairstyle (Female)", "Hairstyle (Male)",
                  "Hair color", "Face Shapes (Female)", "Face Shapes (Male)", "Nose (Female)", "Nose (Male)",
                  "Eye Shapes (Female)", "Eye Shapes (Male)", "Eye Colors", "Eyebrows (Female)", "Eyebrows (Male)",
                  "Eyebrow Colors", "Lip Shapes (Female)", "Lip Shapes (Male)", "Lip Colors"]
    cat_dropdown=Dropdown(grid, values=cats, state="readonly")
    styleDropdown(cat_dropdown)
    cat_dropdown.grid(row=1, column=0, padx=20)
    l2=Label(grid, text='Asset:')
    styleLabel(l2)
    l2.grid(row=0, column=1, padx=20)
    asset=Dropdown(grid, values=[], state="readonly")
    styleDropdown(asset)
    asset.grid(row=1, column=1, padx=20)

    cat_dropdown.bind("<<ComboboxSelected>>", lambda event: updateAssetsByGender(cat_dropdown, asset))

    grid2 = Frame(frame)
    grid2.configure(bg=appColor)
    grid2.pack()

    cancel=Button(grid2, text="Cancel", command=tkinter_assetsMenu)
    styleButton(cancel, "small")
    cancel.grid(row=2, column=0, pady=30, padx=10)

    delete = Button(grid2, text="Delete", fg='#FF0000',
                    command=lambda: tkinter_deleteAsset_confirm(cat_dropdown, asset, frame))
    styleButton(delete, "small")
    delete.grid(row=2, column=1, pady=30, padx=10)

    def tkinter_deleteAsset_confirm(cat_dropdown, asset, frame):
        category = cat_dropdown.get()
        print(category)
        asset_name = asset.get()

        data = assets.GetCatGenderFromStr(category)
        if data[0] == 0 :
            error = Label(frame, text="Category can't be empty!", fg='red')
            styleLabel(error)
            error.pack()
        elif asset_name == "":
            error = Label(frame, text="Asset name can't be empty!", fg='red')
            styleLabel(error)
            error.pack()
        else:
            assets.deleteAsset(data, asset_name)
            open_popup("Asset successfully deleted.")
            tkinter_assetsMenu()
def updateAssetsByGender(cat_dropdown, asset_dropdown, getOnlyDeletables = True):
    selected_cat = cat_dropdown.get()
    # print("Selected:", selected_cat)
    data = assets.GetCatGenderFromStr(selected_cat)
    res_list = assets.getAssetsByGender(data, getOnlyDeletables)

    asset_dropdown["values"] = res_list
    asset_dropdown.set("")
def tkinter_editAsset():
    tkinter_clearScreen()

    frame = Frame(root)
    frame.configure(bg=appColor)
    frame.pack(fill="both", expand=True)

    grid=Frame(frame)
    grid.configure(bg=appColor)
    grid.pack()

    l1=Label(grid, text="In category:")
    styleLabel(l1)
    l1.grid(row=0, column=0, padx=20)
    cats = ["Body Type (Female)", "Body Type (Male)", "Skin Tone", "Hairstyle (Female)", "Hairstyle (Male)",
                  "Hair color", "Face Shapes (Female)", "Face Shapes (Male)", "Nose (Female)", "Nose (Male)",
                  "Eye Shapes (Female)", "Eye Shapes (Male)", "Eye Colors", "Eyebrows (Female)", "Eyebrows (Male)",
                  "Eyebrow Colors", "Lip Shapes (Female)", "Lip Shapes (Male)", "Lip Colors"]
    cat_dropdown=Dropdown(grid, values=cats, state="readonly")
    styleDropdown(cat_dropdown)
    cat_dropdown.grid(row=1, column=0, padx=20)
    l2=Label(grid, text='Asset:')
    styleLabel(l2)
    l2.grid(row=0, column=1, padx=20)
    asset=Dropdown(grid, values=[], state="readonly")
    styleDropdown(asset)
    asset.grid(row=1, column=1, padx=20)

    grid2 = Frame(frame)
    grid2.configure(bg=appColor)
    grid2.pack()
    grid3 = Frame(frame)
    grid3.configure(bg=appColor)
    grid3.pack()
    grid4 = Frame(frame)
    grid4.configure(bg=appColor)
    grid4.pack()

    cat_dropdown.bind("<<ComboboxSelected>>", lambda event: categoryChosen(cat_dropdown, asset))
    asset.bind("<<ComboboxSelected>>", lambda event: showProperties(cat_dropdown, asset, grid2, grid3))

    def categoryChosen(cat_dropdown, asset):
        for widget in grid3.winfo_children():
            widget.destroy()
        updateAssetsByGender(cat_dropdown, asset, False)


    cancel=Button(grid4, text="Cancel", command=tkinter_assetsMenu)
    styleButton(cancel, "small")
    cancel.grid(row=2, column=0, pady=30, padx=10)

    delete = Button(grid4, text="Save changes",
                    command=lambda: tkinter_editAsset_confirm(cat_dropdown, asset, grid2, grid3))
    styleButton(delete, "small")
    delete.grid(row=2, column=1, pady=30, padx=10)

    def showProperties(cat_dropdown, asset_dropdown, grid1, grid2):
        clearFrame(grid2)

        selected_cat = cat_dropdown.get()
        name = asset_dropdown.get()
        # print("Selected:", selected_cat)
        data = assets.GetCatGenderFromStr(selected_cat)
        asset = assets.getAssetData(data, name)

        '''
        [0] - id
        [1] - script_name
        [2] - display_name
        [3] - category_id
        [4] - isFemale
        [5] - isMale
        [6] - canDelete
        '''
        display_name_title = Label(grid1, text="Display Name:")
        styleLabel(display_name_title)
        display_name_title.grid(row=0, column=0, pady=(20, 0))
        display_name = Entry(grid1)
        styleEntry(display_name)
        display_name.insert(0, asset[2])
        display_name.grid(row=1, column=0, padx=20)

        subcats = assets.getSubcats(asset[3])
        active_subs = assets.getActiveSubcats(asset[0])

        row = 0
        col = 0
        for subcat in subcats:
            cb = Checkbox(grid2, text=subcat[1], id=subcat[0])
            styleCheckbox(cb)
            cb.grid(row=row, column=col)
            for subs in active_subs:
                if subcat[0] == subs[1]:
                    cb.select()

            col = (col + 1) % 4
            if col == 0:
                row += 1
    def tkinter_editAsset_confirm(cat_dropdown, asset_dropdown, grid1, grid2):
        selected_cat = cat_dropdown.get()
        name = asset_dropdown.get()
        data = assets.GetCatGenderFromStr(selected_cat)
        asset = assets.getAssetData(data, name)

        error = Label(grid2, fg='red')
        styleLabel(error)

        for widget in grid1.winfo_children():
            if isinstance(widget, Entry):
                display_name = widget.get()
                # print(display_name)

        if name == '':
            error.config(text="Please choose an asset to edit!")
            error.pack()
        elif display_name =='':
            error.config(text="Display name can't be empty!")
            error.pack()
        else:
            assets.updateAssetDisplayName(asset[0], display_name)

            subcats = []
            for widget in grid2.winfo_children():
                if isinstance(widget, Checkbox):
                    if widget.get_value():
                        subcats.append(widget.id)

            assets.updateSubcategories(asset[0], subcats)
            open_popup("Successfully saved changes.")
            tkinter_assetsMenu()


def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def open_popup(message):
    # Create a new popup window
    popup = Toplevel(root)

    window_width = root.winfo_width()
    window_height = root.winfo_height()
    popup_width = 300  # Adjust this as needed
    popup_height = 150  # Adjust this as needed

    x_position = root.winfo_x() + (window_width - popup_width) // 2
    y_position = root.winfo_y() + (window_height - popup_height) // 2

    popup.geometry(f"{popup_width}x{popup_height}+{x_position}+{y_position}")
    popup.title("Character Customization Template Creator")

    frame = Frame(popup, bg=appColor)
    frame.pack(fill="both", expand=True)

    # Add content to the popup window
    label = Label(frame, text=message)
    styleLabel(label)
    label.pack(padx=20, pady=20)

    button = Button(frame, text="OK", padx=20, command= popup.destroy)
    styleButton(button, "small")
    button.pack(pady=15)

    # Block interaction with the main window
    root.wait_window(popup)