#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on October 04, 2022, at 15:05
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'mfe_flanker_v1'  # from the Builder filename that created this script
expInfo = {
    'id': '',
    'cb': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['id'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\NDClab\\Desktop\\Experiments\\memory_for_error_flanker\\mfe_short_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color='0.5000, 0.5000, 0.5000', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "JS_code" ---

# --- Initialize components for Routine "setup" ---
# Run 'Begin Experiment' code from setup_code
import serial #used for sending eeg triggers
import time #indirerctly used for sending eeg triggers (how long to wait before clearing port)


win.mouseVisible = False #hide mouse cursor
port = serial.Serial('COM3') #open specified port (COM3) for sending eeg triggers to           
PulseWidth = 0.002 #how long to wait before clearing port after sending trigger (2 ms is sufficient at 1000 hz sampling rate)

port.write([0x00]) #clear serial port
time.sleep(PulseWidth) #wait PulseWidth amount of time before doing anything else

# Run 'Begin Experiment' code from code_6
# Initialize and assign the variables that will be used in the instructions of the surprise task.
if expInfo['cb'] == 'A':
    Left_first_inst = 'New'
    Right_first_inst = 'Old'
    Left_sec_inst = 'Approving'
    Right_sec_inst = 'Disapproving'
elif expInfo['cb'] == 'B':
    Left_first_inst = 'Old'
    Right_first_inst = 'New'
    Left_sec_inst = 'Approving'
    Right_sec_inst = 'Disapproving'
elif expInfo['cb'] == 'C':
    Left_first_inst = 'Old'
    Right_first_inst = 'New'
    Left_sec_inst = 'Disapproving'
    Right_sec_inst = 'Approving'
elif expInfo['cb'] == 'D':
    Left_first_inst = 'New'
    Right_first_inst = 'Old'
    Left_sec_inst = 'Disapproving'
    Right_sec_inst = 'Approving'
elif expInfo['cb'] == 'E':
    Left_first_inst = 'New'
    Right_first_inst = 'Old'
    Left_sec_inst = 'Disapproving'
    Right_sec_inst = 'Approving'
elif expInfo['cb'] == 'F':
    Left_first_inst = 'New'
    Right_first_inst = 'Old'
    Left_sec_inst = 'Approving'
    Right_sec_inst = 'Disapproving'
elif expInfo['cb'] == 'G':
    Left_first_inst = 'Old'
    Right_first_inst = 'New'
    Left_sec_inst = 'Approving'
    Right_sec_inst = 'Disapproving'
elif expInfo['cb'] == 'H':
    Left_first_inst = 'Old'
    Right_first_inst = 'New'
    Left_sec_inst = 'Disapproving'
    Right_sec_inst = 'Approving'



# --- Initialize components for Routine "welcome" ---
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='Arrow Game\n\nWelcome to the arrow game. In this game, arrows will be quickly flashed on the screen. Your goal is to respond to the direction of the MIDDLE arrow, and to respond as quickly as you can without making mistakes. \n\nIf the MIDDLE arrow is pointing to the right, use your right hand to press the right button. If the MIDDLE arrow is pointing to the left, use your left hand to press the left button. \n\nPress the right button to continue\n',
    font='Arial',
    units='height', pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
welcome_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "instructRight" ---
instructRight_text = visual.TextStim(win=win, name='instructRight_text',
    text='Below, the MIDDLE arrow is pointing to the right, so you would respond by pressing the right button with your right hand.\n\nPress the right button to continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructRight_centerImg = visual.ImageStim(
    win=win,
    name='instructRight_centerImg', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(0, -.3), size=(.035, .035),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
instructRight_rightImg1 = visual.ImageStim(
    win=win,
    name='instructRight_rightImg1', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(0.0385, -.3), size=(.035, .035),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
instructRight_leftImg1 = visual.ImageStim(
    win=win,
    name='instructRight_leftImg1', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(-0.0385, -.3), size=(.035, .035),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
insructRight_keyResp = keyboard.Keyboard()
instructRight_rightImg2 = visual.ImageStim(
    win=win,
    name='instructRight_rightImg2', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(0.077, -.3), size=(.035, .035),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
instructRight_leftImg2 = visual.ImageStim(
    win=win,
    name='instructRight_leftImg2', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(-0.077, -.3), size=(.035, .035),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "instructLeft" ---
instructLeft_text = visual.TextStim(win=win, name='instructLeft_text',
    text='Below, the MIDDLE arrow is pointing to the left, so you would respond by pressing the left button with your left hand.\n\nPress the left button to continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructLeft_centerImg = visual.ImageStim(
    win=win,
    name='instructLeft_centerImg', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(0, -.3), size=(.035, .035),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
instructLeft_rightImg1 = visual.ImageStim(
    win=win,
    name='instructLeft_rightImg1', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(0.0385, -.3), size=(.035, .035),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
instructLeft_leftImg1 = visual.ImageStim(
    win=win,
    name='instructLeft_leftImg1', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(-0.0385, -.3), size=(.035, .035),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
instructLeft_keyResp = keyboard.Keyboard()
instructLeft_leftImg2 = visual.ImageStim(
    win=win,
    name='instructLeft_leftImg2', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(-0.077, -.3), size=(.035, .035),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
instructLeft_rightImg2 = visual.ImageStim(
    win=win,
    name='instructLeft_rightImg2', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(0.077, -.3), size=(.035, .035),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "instructInconRight" ---
instructInconRight_text = visual.TextStim(win=win, name='instructInconRight_text',
    text='Sometimes the MIDDLE arrow will point in a different direction from the other arrows. However, your goal is to always respond based on the direction of the MIDDLE arrow.\n\nBelow, the MIDDLE arrow is pointing to the right, so you would respond by pressing the right button with your right hand.\n\nPress the right button to continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructIncon_centerImg = visual.ImageStim(
    win=win,
    name='instructIncon_centerImg', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(0, -.3), size=(.035, .035),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
instructIncon_rightImg1 = visual.ImageStim(
    win=win,
    name='instructIncon_rightImg1', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(0.0385, -.3), size=(.035, .035),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
instructIncon_leftImg1 = visual.ImageStim(
    win=win,
    name='instructIncon_leftImg1', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(-0.0385, -.3), size=(.035, .035),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
insructInconRight_keyResp = keyboard.Keyboard()
instructIncon_leftImg2 = visual.ImageStim(
    win=win,
    name='instructIncon_leftImg2', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(-0.077, -.3), size=(.035, .035),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
instructIncon_rightImg2 = visual.ImageStim(
    win=win,
    name='instructIncon_rightImg2', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(0.077, -.3), size=(.035, .035),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "instructInconLeft" ---
instructInconLeft_text = visual.TextStim(win=win, name='instructInconLeft_text',
    text='Below, the MIDDLE arrow is pointing to the left, so you would respond by pressing the left button with your left hand.\n\nPress the left button to continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructInconLeft_centerImg = visual.ImageStim(
    win=win,
    name='instructInconLeft_centerImg', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(0, -.3), size=(.035, .035),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
instructInconLeft_rightImg1 = visual.ImageStim(
    win=win,
    name='instructInconLeft_rightImg1', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(0.0385, -.3), size=(.035, .035),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
instructInconLeft_leftImg1 = visual.ImageStim(
    win=win,
    name='instructInconLeft_leftImg1', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(-0.0385, -.3), size=(.035, .035),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
instructInconLeft_keyResp = keyboard.Keyboard()
instructInconLeft_rightImg2 = visual.ImageStim(
    win=win,
    name='instructInconLeft_rightImg2', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(0.077, -.3), size=(.035, .035),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
instructInconLeft_leftImg2 = visual.ImageStim(
    win=win,
    name='instructInconLeft_leftImg2', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(-0.077, -.3), size=(.035, .035),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "prac_blockReminders" ---
# Run 'Begin Experiment' code from prac_initAcc_code
#initialize the following variables at the start of experiment
trialNum = 0
accuracy = 0
numCorr = 0
blockAcc = 0
prac_blockText = visual.TextStim(win=win, name='prac_blockText',
    text='Practice',
    font='Arial',
    pos=(0, .3), height=0.06, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
prac_reminder_text = visual.TextStim(win=win, name='prac_reminder_text',
    text='You will now practice responding to the arrows. Remember to always respond to the direction of the MIDDLE arrow.\n\nRespond as quickly as you can without making mistakes.\n\nTo get ready, rest your right and left thumbs on the right and left buttons, then press the right button when you are ready to begin.\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
prac_reminder_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "initFixation" ---
initFixation_img = visual.ImageStim(
    win=win,
    name='initFixation_img', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, -.015), size=(0.26, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# --- Initialize components for Routine "prac_stimRoutine" ---
# Run 'Begin Experiment' code from prac_isi_code
#initialize the thisISI variable
thisISI = 0
bigFace = visual.ImageStim(
    win=win,
    name='bigFace', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.0), size=(0.4267, .3),
    color=[1,1,1], colorSpace='rgb', opacity=0.85,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
cover_background_2 = visual.ImageStim(
    win=win,
    name='cover_background_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -.015), size=(0.26, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
prac_centerImg = visual.ImageStim(
    win=win,
    name='prac_centerImg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
prac_rightImg1 = visual.ImageStim(
    win=win,
    name='prac_rightImg1', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
prac_rightImg2 = visual.ImageStim(
    win=win,
    name='prac_rightImg2', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)
prac_leftImg1 = visual.ImageStim(
    win=win,
    name='prac_leftImg1', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-7.0)
prac_leftImg2 = visual.ImageStim(
    win=win,
    name='prac_leftImg2', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-8.0)
prac_fixImg = visual.ImageStim(
    win=win,
    name='prac_fixImg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, -.015), size=(0.26, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-9.0)
prac_stim_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "prac_blockFeed" ---
prac_blockFeed_text = visual.TextStim(win=win, name='prac_blockFeed_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
prac_pressContinue = visual.TextStim(win=win, name='prac_pressContinue',
    text='Press the right key',
    font='Arial',
    pos=(0, -.3), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
prac_blockFeed_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "ringBell" ---
ringBell_text = visual.TextStim(win=win, name='ringBell_text',
    text='Ring the bell to let the experimenter know that you finished the practice.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
bellKey = keyboard.Keyboard()

# --- Initialize components for Routine "task_blockReminders" ---
# Run 'Begin Experiment' code from task_blockReminder_code
#initialize the following variables at the start of experiment
blockCounter = 0

#note that we do not need to initialize the accuracy and numCorr vars here
#because they were already initialilzed in the code snippet of the practice loop
task_blockText = visual.TextStim(win=win, name='task_blockText',
    text='',
    font='Arial',
    pos=(0, .3), height=0.06, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
task_blockReminders_text = visual.TextStim(win=win, name='task_blockReminders_text',
    text='Remember to always respond to the direction of the MIDDLE arrow.\n\nRespond as quickly as you can without making mistakes.\n\nTo get ready, rest your right and left thumbs on the right and left buttons, then press the right button when you are ready to begin.\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
task_blockReminders_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "initFixation" ---
initFixation_img = visual.ImageStim(
    win=win,
    name='initFixation_img', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, -.015), size=(0.26, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# --- Initialize components for Routine "task_stimRoutine" ---
# Run 'Begin Experiment' code from task_isi_code
#no need to initialize thisISI, as already done in practice code snippit
bigFace_2 = visual.ImageStim(
    win=win,
    name='bigFace_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.0), size=(0.4267, .3),
    color=[1,1,1], colorSpace='rgb', opacity=0.85,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
cover_background = visual.ImageStim(
    win=win,
    name='cover_background', 
    image='img/cover_background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -.015), size=(0.26, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
task_centerImg = visual.ImageStim(
    win=win,
    name='task_centerImg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
task_rightImg1 = visual.ImageStim(
    win=win,
    name='task_rightImg1', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
task_rightImg2 = visual.ImageStim(
    win=win,
    name='task_rightImg2', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)
task_leftImg1 = visual.ImageStim(
    win=win,
    name='task_leftImg1', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-7.0)
task_leftImg2 = visual.ImageStim(
    win=win,
    name='task_leftImg2', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-8.0)
task_fixImg = visual.ImageStim(
    win=win,
    name='task_fixImg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, -.015), size=(0.26, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-9.0)
task1_stim_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "task_blockFeed" ---
task_blockFeed_text = visual.TextStim(win=win, name='task_blockFeed_text',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.12, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
task_blockFeed_text2 = visual.TextStim(win=win, name='task_blockFeed_text2',
    text='',
    font='Arial',
    pos=(0, -0.3), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
task_blockFeed_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "ringBell2" ---
ringBell_text_2 = visual.TextStim(win=win, name='ringBell_text_2',
    text='Please ring the bell to let the experimenter know you finished the game.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
bellKey_2 = keyboard.Keyboard()

# --- Initialize components for Routine "errorNumbers" ---
errorNum_text = visual.TextStim(win=win, name='errorNum_text',
    text='Excluding the practice, how many errors do you think you made during the arrow game? \n\nPlease provide a number as your best estimate.\n\n\nExperimenter enters the answer for participant. \n\n',
    font='Open Sans',
    pos=(0, 0.12), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
textbox_errorNum = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, -0.3),     letterHeight=0.05,
     size=(0.2, 0.2), borderWidth=2.0,
     color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='bottom-center',
     fillColor=[1.0000, 1.0000, 1.0000], borderColor=[-1.0000, -1.0000, -1.0000],
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox_errorNum',
     autoLog=True,
)
errorN_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "errorPercentage" ---
errorPercent_text = visual.TextStim(win=win, name='errorPercent_text',
    text='Excluding the practice, what percentage of your responses do you think were errors during the arrow game? \n\nPlease provide a single number as your best estimate.\n\n\nExperimenter enters the answer for participant. \n\n',
    font='Open Sans',
    pos=(0, 0.12), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
textbox_errorPercent = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, -0.3),     letterHeight=0.05,
     size=(0.2, 0.2), borderWidth=2.0,
     color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='bottom-center',
     fillColor=[1.0000, 1.0000, 1.0000], borderColor=[-1.0000, -1.0000, -1.0000],
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox_errorPercent',
     autoLog=True,
)
errorN_key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "botherRate" ---
botherRate_text = visual.TextStim(win=win, name='botherRate_text',
    text='How much did it bother you when you made an error during the arrow game? \n\nYour answer should be on a scale from 0 (not at all) to 10 (very much). \n\n\nExperimenter enters the answer for participant. \n\n\n',
    font='Open Sans',
    pos=(0, 0.12), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
textbox_botherRate = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, -0.3),     letterHeight=0.05,
     size=(0.2, 0.2), borderWidth=2.0,
     color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='bottom-center',
     fillColor=[1.0000, 1.0000, 1.0000], borderColor=[-1.0000, -1.0000, -1.0000],
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox_botherRate',
     autoLog=True,
)
botherRate_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "ringBell3" ---
ringBell_text_3 = visual.TextStim(win=win, name='ringBell_text_3',
    text='Ring the bell to let the experimenter know when you complete answering the surveys.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
bellKey_3 = keyboard.Keyboard()

# --- Initialize components for Routine "surpriseInstruct" ---
instruct_surprise1 = visual.TextStim(win=win, name='instruct_surprise1',
    text='You will now begin a task in which you will be asked one question.\n\nAnswers of this question are presented on a slider and you will need to use the mouse to select one of them as your response. \n \n\nTo learn about this task and the question, press the right button to continue. \n',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instruct_surp1_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "surpIns2" ---
instruct_surprise1_5 = visual.TextStim(win=win, name='instruct_surprise1_5',
    text='The question asks whether the face displayed on screen looks OLD (you saw it in the previous game) or NEW (you didn’t see it in the previous game).\nYou have six options: “definitely OLD,” “probably OLD,” “maybe OLD,” “maybe NEW,” “probably NEW,”  or “definitely NEW.”\n\nRandomly choose a response from the slider below to continue and learn about these answers.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
prac_firstSlider_2 = visual.Slider(win=win, name='prac_firstSlider_2',
    startValue=None, size=(0.85, 0.022), pos=(0, -0.35), units=None,
    labels=["Definitely", "Probably", "Maybe", "Maybe", "Probably", "Definitely"], ticks=[1, 2, 3, 4, 5, 6], granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.022,
    flip=False, ori=0.0, depth=-1, readOnly=False)
text_7 = visual.TextStim(win=win, name='text_7',
    text='',
    font='Open Sans',
    pos=(-0.6, -0.35), height=0.045, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='',
    font='Open Sans',
    pos=(0.6, -0.35), height=0.045, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "surpIns2_2" ---
instruct_surprise1_7 = visual.TextStim(win=win, name='instruct_surprise1_7',
    text='For example, if you are 100% confident that you saw the face in the previous game, choose “definitely OLD.”\n\nIf you are less confident, but think you probably saw the face in the previous game, choose “probably OLD.”\n\nIf you really aren’t sure, but think it’s a little more likely that you saw the face in the previous game, choose “maybe OLD.”\n\nIf you really aren’t sure, but think it’s a little more likely that you didn’t see the face in the previous game, choose “maybe NEW.”\n\nIf you aren’t certain, but think you probably haven’t seen the face before, choose “probably NEW.”\n\nIf you are 100% confident that you haven’t seen the face before, choose “definitely NEW.”\n\nRandomly choose a response from the slider below to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
prac_firstSlider_3 = visual.Slider(win=win, name='prac_firstSlider_3',
    startValue=None, size=(0.85, 0.022), pos=(0, -0.35), units=None,
    labels=["Definitely", "Probably", "Maybe", "Maybe", "Probably", "Definitely"], ticks=[1, 2, 3, 4, 5, 6], granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.022,
    flip=False, ori=0.0, depth=-1, readOnly=False)
text_9 = visual.TextStim(win=win, name='text_9',
    text='',
    font='Open Sans',
    pos=(-0.6, -0.35), height=0.045, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_10 = visual.TextStim(win=win, name='text_10',
    text='',
    font='Open Sans',
    pos=(0.6, -0.35), height=0.045, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "surp_taskReminders" ---
# Run 'Begin Experiment' code from task_blockReminder_code_2
#initialize the following variables at the start of experiment
blockCounterZ1 = 0


task_blockText_2 = visual.TextStim(win=win, name='task_blockText_2',
    text='',
    font='Arial',
    pos=(0, .3), height=0.06, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
task_blockReminders_text_2 = visual.TextStim(win=win, name='task_blockReminders_text_2',
    text='Press the right button when you are ready to begin.\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
task_blockReminders_keyResp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "firstStim_A1" ---
first_surpStimuliA1 = visual.ImageStim(
    win=win,
    name='first_surpStimuliA1', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4551466688, 0.32),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fStimA1 = visual.TextStim(win=win, name='fStimA1',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
firstStim_sliderA1 = visual.Slider(win=win, name='firstStim_sliderA1',
    startValue=None, size=(0.85, 0.022), pos=(0, 0.22), units=None,
    labels=["Definitely", "Probably", "Maybe", "Maybe", "Probably", "Definitely"], ticks=[1, 2, 3, 4, 5, 6], granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.022,
    flip=False, ori=0.0, depth=-3, readOnly=False)
first_mouseA1 = event.Mouse(win=win)
x, y = [None, None]
first_mouseA1.mouseClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(-0.6, 0.22), height=0.045, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Open Sans',
    pos=(0.6, 0.22), height=0.045, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# --- Initialize components for Routine "fixation2" ---
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "ringBell4" ---
ringBell_text_4 = visual.TextStim(win=win, name='ringBell_text_4',
    text='Ring the bell to let the experimenter know you completed the game.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
bellKey_4 = keyboard.Keyboard()

# --- Initialize components for Routine "finishMessage" ---
finishMessage_text = visual.TextStim(win=win, name='finishMessage_text',
    text='Thank you for your participation!',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "JS_code" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
JS_codeComponents = []
for thisComponent in JS_codeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "JS_code" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in JS_codeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "JS_code" ---
for thisComponent in JS_codeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "JS_code" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "setup" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "setup" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "setup" ---
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
welcome_keyResp.keys = []
welcome_keyResp.rt = []
_welcome_keyResp_allKeys = []
# keep track of which components have finished
welcomeComponents = [welcome_text, welcome_keyResp]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_text* updates
    if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.tStart = t  # local t and not account for scr refresh
        welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
        welcome_text.setAutoDraw(True)
    
    # *welcome_keyResp* updates
    waitOnFlip = False
    if welcome_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_keyResp.frameNStart = frameN  # exact frame index
        welcome_keyResp.tStart = t  # local t and not account for scr refresh
        welcome_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_keyResp, 'tStartRefresh')  # time at next scr refresh
        welcome_keyResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_keyResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcome_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcome_keyResp.status == STARTED and not waitOnFlip:
        theseKeys = welcome_keyResp.getKeys(keyList=['8'], waitRelease=False)
        _welcome_keyResp_allKeys.extend(theseKeys)
        if len(_welcome_keyResp_allKeys):
            welcome_keyResp.keys = _welcome_keyResp_allKeys[-1].name  # just the last key pressed
            welcome_keyResp.rt = _welcome_keyResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "welcome" ---
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructRight" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
insructRight_keyResp.keys = []
insructRight_keyResp.rt = []
_insructRight_keyResp_allKeys = []
# keep track of which components have finished
instructRightComponents = [instructRight_text, instructRight_centerImg, instructRight_rightImg1, instructRight_leftImg1, insructRight_keyResp, instructRight_rightImg2, instructRight_leftImg2]
for thisComponent in instructRightComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructRight" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructRight_text* updates
    if instructRight_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_text.frameNStart = frameN  # exact frame index
        instructRight_text.tStart = t  # local t and not account for scr refresh
        instructRight_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_text, 'tStartRefresh')  # time at next scr refresh
        instructRight_text.setAutoDraw(True)
    
    # *instructRight_centerImg* updates
    if instructRight_centerImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_centerImg.frameNStart = frameN  # exact frame index
        instructRight_centerImg.tStart = t  # local t and not account for scr refresh
        instructRight_centerImg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_centerImg, 'tStartRefresh')  # time at next scr refresh
        instructRight_centerImg.setAutoDraw(True)
    
    # *instructRight_rightImg1* updates
    if instructRight_rightImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_rightImg1.frameNStart = frameN  # exact frame index
        instructRight_rightImg1.tStart = t  # local t and not account for scr refresh
        instructRight_rightImg1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_rightImg1, 'tStartRefresh')  # time at next scr refresh
        instructRight_rightImg1.setAutoDraw(True)
    
    # *instructRight_leftImg1* updates
    if instructRight_leftImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_leftImg1.frameNStart = frameN  # exact frame index
        instructRight_leftImg1.tStart = t  # local t and not account for scr refresh
        instructRight_leftImg1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_leftImg1, 'tStartRefresh')  # time at next scr refresh
        instructRight_leftImg1.setAutoDraw(True)
    
    # *insructRight_keyResp* updates
    waitOnFlip = False
    if insructRight_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        insructRight_keyResp.frameNStart = frameN  # exact frame index
        insructRight_keyResp.tStart = t  # local t and not account for scr refresh
        insructRight_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insructRight_keyResp, 'tStartRefresh')  # time at next scr refresh
        insructRight_keyResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(insructRight_keyResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(insructRight_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if insructRight_keyResp.status == STARTED and not waitOnFlip:
        theseKeys = insructRight_keyResp.getKeys(keyList=['8'], waitRelease=False)
        _insructRight_keyResp_allKeys.extend(theseKeys)
        if len(_insructRight_keyResp_allKeys):
            insructRight_keyResp.keys = _insructRight_keyResp_allKeys[-1].name  # just the last key pressed
            insructRight_keyResp.rt = _insructRight_keyResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instructRight_rightImg2* updates
    if instructRight_rightImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_rightImg2.frameNStart = frameN  # exact frame index
        instructRight_rightImg2.tStart = t  # local t and not account for scr refresh
        instructRight_rightImg2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_rightImg2, 'tStartRefresh')  # time at next scr refresh
        instructRight_rightImg2.setAutoDraw(True)
    
    # *instructRight_leftImg2* updates
    if instructRight_leftImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_leftImg2.frameNStart = frameN  # exact frame index
        instructRight_leftImg2.tStart = t  # local t and not account for scr refresh
        instructRight_leftImg2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_leftImg2, 'tStartRefresh')  # time at next scr refresh
        instructRight_leftImg2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructRightComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructRight" ---
for thisComponent in instructRightComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructRight" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructLeft" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instructLeft_keyResp.keys = []
instructLeft_keyResp.rt = []
_instructLeft_keyResp_allKeys = []
# keep track of which components have finished
instructLeftComponents = [instructLeft_text, instructLeft_centerImg, instructLeft_rightImg1, instructLeft_leftImg1, instructLeft_keyResp, instructLeft_leftImg2, instructLeft_rightImg2]
for thisComponent in instructLeftComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructLeft" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructLeft_text* updates
    if instructLeft_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_text.frameNStart = frameN  # exact frame index
        instructLeft_text.tStart = t  # local t and not account for scr refresh
        instructLeft_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_text, 'tStartRefresh')  # time at next scr refresh
        instructLeft_text.setAutoDraw(True)
    
    # *instructLeft_centerImg* updates
    if instructLeft_centerImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_centerImg.frameNStart = frameN  # exact frame index
        instructLeft_centerImg.tStart = t  # local t and not account for scr refresh
        instructLeft_centerImg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_centerImg, 'tStartRefresh')  # time at next scr refresh
        instructLeft_centerImg.setAutoDraw(True)
    
    # *instructLeft_rightImg1* updates
    if instructLeft_rightImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_rightImg1.frameNStart = frameN  # exact frame index
        instructLeft_rightImg1.tStart = t  # local t and not account for scr refresh
        instructLeft_rightImg1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_rightImg1, 'tStartRefresh')  # time at next scr refresh
        instructLeft_rightImg1.setAutoDraw(True)
    
    # *instructLeft_leftImg1* updates
    if instructLeft_leftImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_leftImg1.frameNStart = frameN  # exact frame index
        instructLeft_leftImg1.tStart = t  # local t and not account for scr refresh
        instructLeft_leftImg1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_leftImg1, 'tStartRefresh')  # time at next scr refresh
        instructLeft_leftImg1.setAutoDraw(True)
    
    # *instructLeft_keyResp* updates
    waitOnFlip = False
    if instructLeft_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_keyResp.frameNStart = frameN  # exact frame index
        instructLeft_keyResp.tStart = t  # local t and not account for scr refresh
        instructLeft_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_keyResp, 'tStartRefresh')  # time at next scr refresh
        instructLeft_keyResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructLeft_keyResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructLeft_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructLeft_keyResp.status == STARTED and not waitOnFlip:
        theseKeys = instructLeft_keyResp.getKeys(keyList=['1'], waitRelease=False)
        _instructLeft_keyResp_allKeys.extend(theseKeys)
        if len(_instructLeft_keyResp_allKeys):
            instructLeft_keyResp.keys = _instructLeft_keyResp_allKeys[-1].name  # just the last key pressed
            instructLeft_keyResp.rt = _instructLeft_keyResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instructLeft_leftImg2* updates
    if instructLeft_leftImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_leftImg2.frameNStart = frameN  # exact frame index
        instructLeft_leftImg2.tStart = t  # local t and not account for scr refresh
        instructLeft_leftImg2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_leftImg2, 'tStartRefresh')  # time at next scr refresh
        instructLeft_leftImg2.setAutoDraw(True)
    
    # *instructLeft_rightImg2* updates
    if instructLeft_rightImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_rightImg2.frameNStart = frameN  # exact frame index
        instructLeft_rightImg2.tStart = t  # local t and not account for scr refresh
        instructLeft_rightImg2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_rightImg2, 'tStartRefresh')  # time at next scr refresh
        instructLeft_rightImg2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructLeftComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructLeft" ---
for thisComponent in instructLeftComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructLeft" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructInconRight" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
insructInconRight_keyResp.keys = []
insructInconRight_keyResp.rt = []
_insructInconRight_keyResp_allKeys = []
# keep track of which components have finished
instructInconRightComponents = [instructInconRight_text, instructIncon_centerImg, instructIncon_rightImg1, instructIncon_leftImg1, insructInconRight_keyResp, instructIncon_leftImg2, instructIncon_rightImg2]
for thisComponent in instructInconRightComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructInconRight" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructInconRight_text* updates
    if instructInconRight_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconRight_text.frameNStart = frameN  # exact frame index
        instructInconRight_text.tStart = t  # local t and not account for scr refresh
        instructInconRight_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconRight_text, 'tStartRefresh')  # time at next scr refresh
        instructInconRight_text.setAutoDraw(True)
    
    # *instructIncon_centerImg* updates
    if instructIncon_centerImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructIncon_centerImg.frameNStart = frameN  # exact frame index
        instructIncon_centerImg.tStart = t  # local t and not account for scr refresh
        instructIncon_centerImg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructIncon_centerImg, 'tStartRefresh')  # time at next scr refresh
        instructIncon_centerImg.setAutoDraw(True)
    
    # *instructIncon_rightImg1* updates
    if instructIncon_rightImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructIncon_rightImg1.frameNStart = frameN  # exact frame index
        instructIncon_rightImg1.tStart = t  # local t and not account for scr refresh
        instructIncon_rightImg1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructIncon_rightImg1, 'tStartRefresh')  # time at next scr refresh
        instructIncon_rightImg1.setAutoDraw(True)
    
    # *instructIncon_leftImg1* updates
    if instructIncon_leftImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructIncon_leftImg1.frameNStart = frameN  # exact frame index
        instructIncon_leftImg1.tStart = t  # local t and not account for scr refresh
        instructIncon_leftImg1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructIncon_leftImg1, 'tStartRefresh')  # time at next scr refresh
        instructIncon_leftImg1.setAutoDraw(True)
    
    # *insructInconRight_keyResp* updates
    waitOnFlip = False
    if insructInconRight_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        insructInconRight_keyResp.frameNStart = frameN  # exact frame index
        insructInconRight_keyResp.tStart = t  # local t and not account for scr refresh
        insructInconRight_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insructInconRight_keyResp, 'tStartRefresh')  # time at next scr refresh
        insructInconRight_keyResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(insructInconRight_keyResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(insructInconRight_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if insructInconRight_keyResp.status == STARTED and not waitOnFlip:
        theseKeys = insructInconRight_keyResp.getKeys(keyList=['8'], waitRelease=False)
        _insructInconRight_keyResp_allKeys.extend(theseKeys)
        if len(_insructInconRight_keyResp_allKeys):
            insructInconRight_keyResp.keys = _insructInconRight_keyResp_allKeys[-1].name  # just the last key pressed
            insructInconRight_keyResp.rt = _insructInconRight_keyResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instructIncon_leftImg2* updates
    if instructIncon_leftImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructIncon_leftImg2.frameNStart = frameN  # exact frame index
        instructIncon_leftImg2.tStart = t  # local t and not account for scr refresh
        instructIncon_leftImg2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructIncon_leftImg2, 'tStartRefresh')  # time at next scr refresh
        instructIncon_leftImg2.setAutoDraw(True)
    
    # *instructIncon_rightImg2* updates
    if instructIncon_rightImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructIncon_rightImg2.frameNStart = frameN  # exact frame index
        instructIncon_rightImg2.tStart = t  # local t and not account for scr refresh
        instructIncon_rightImg2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructIncon_rightImg2, 'tStartRefresh')  # time at next scr refresh
        instructIncon_rightImg2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructInconRightComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructInconRight" ---
for thisComponent in instructInconRightComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructInconRight" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructInconLeft" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instructInconLeft_keyResp.keys = []
instructInconLeft_keyResp.rt = []
_instructInconLeft_keyResp_allKeys = []
# keep track of which components have finished
instructInconLeftComponents = [instructInconLeft_text, instructInconLeft_centerImg, instructInconLeft_rightImg1, instructInconLeft_leftImg1, instructInconLeft_keyResp, instructInconLeft_rightImg2, instructInconLeft_leftImg2]
for thisComponent in instructInconLeftComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructInconLeft" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructInconLeft_text* updates
    if instructInconLeft_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_text.frameNStart = frameN  # exact frame index
        instructInconLeft_text.tStart = t  # local t and not account for scr refresh
        instructInconLeft_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_text, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_text.setAutoDraw(True)
    
    # *instructInconLeft_centerImg* updates
    if instructInconLeft_centerImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_centerImg.frameNStart = frameN  # exact frame index
        instructInconLeft_centerImg.tStart = t  # local t and not account for scr refresh
        instructInconLeft_centerImg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_centerImg, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_centerImg.setAutoDraw(True)
    
    # *instructInconLeft_rightImg1* updates
    if instructInconLeft_rightImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_rightImg1.frameNStart = frameN  # exact frame index
        instructInconLeft_rightImg1.tStart = t  # local t and not account for scr refresh
        instructInconLeft_rightImg1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_rightImg1, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_rightImg1.setAutoDraw(True)
    
    # *instructInconLeft_leftImg1* updates
    if instructInconLeft_leftImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_leftImg1.frameNStart = frameN  # exact frame index
        instructInconLeft_leftImg1.tStart = t  # local t and not account for scr refresh
        instructInconLeft_leftImg1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_leftImg1, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_leftImg1.setAutoDraw(True)
    
    # *instructInconLeft_keyResp* updates
    waitOnFlip = False
    if instructInconLeft_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_keyResp.frameNStart = frameN  # exact frame index
        instructInconLeft_keyResp.tStart = t  # local t and not account for scr refresh
        instructInconLeft_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_keyResp, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_keyResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructInconLeft_keyResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructInconLeft_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructInconLeft_keyResp.status == STARTED and not waitOnFlip:
        theseKeys = instructInconLeft_keyResp.getKeys(keyList=['1'], waitRelease=False)
        _instructInconLeft_keyResp_allKeys.extend(theseKeys)
        if len(_instructInconLeft_keyResp_allKeys):
            instructInconLeft_keyResp.keys = _instructInconLeft_keyResp_allKeys[-1].name  # just the last key pressed
            instructInconLeft_keyResp.rt = _instructInconLeft_keyResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instructInconLeft_rightImg2* updates
    if instructInconLeft_rightImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_rightImg2.frameNStart = frameN  # exact frame index
        instructInconLeft_rightImg2.tStart = t  # local t and not account for scr refresh
        instructInconLeft_rightImg2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_rightImg2, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_rightImg2.setAutoDraw(True)
    
    # *instructInconLeft_leftImg2* updates
    if instructInconLeft_leftImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_leftImg2.frameNStart = frameN  # exact frame index
        instructInconLeft_leftImg2.tStart = t  # local t and not account for scr refresh
        instructInconLeft_leftImg2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_leftImg2, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_leftImg2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructInconLeftComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructInconLeft" ---
for thisComponent in instructInconLeftComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructInconLeft" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac_block_loop = data.TrialHandler(nReps=0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blockSelect_practice.csv'),
    seed=None, name='prac_block_loop')
thisExp.addLoop(prac_block_loop)  # add the loop to the experiment
thisPrac_block_loop = prac_block_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_block_loop.rgb)
if thisPrac_block_loop != None:
    for paramName in thisPrac_block_loop:
        exec('{} = thisPrac_block_loop[paramName]'.format(paramName))

for thisPrac_block_loop in prac_block_loop:
    currentLoop = prac_block_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_block_loop.rgb)
    if thisPrac_block_loop != None:
        for paramName in thisPrac_block_loop:
            exec('{} = thisPrac_block_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "prac_blockReminders" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    prac_reminder_keyResp.keys = []
    prac_reminder_keyResp.rt = []
    _prac_reminder_keyResp_allKeys = []
    # keep track of which components have finished
    prac_blockRemindersComponents = [prac_blockText, prac_reminder_text, prac_reminder_keyResp]
    for thisComponent in prac_blockRemindersComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_blockReminders" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_blockText* updates
        if prac_blockText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_blockText.frameNStart = frameN  # exact frame index
            prac_blockText.tStart = t  # local t and not account for scr refresh
            prac_blockText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_blockText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_blockText.started')
            prac_blockText.setAutoDraw(True)
        
        # *prac_reminder_text* updates
        if prac_reminder_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_reminder_text.frameNStart = frameN  # exact frame index
            prac_reminder_text.tStart = t  # local t and not account for scr refresh
            prac_reminder_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_reminder_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_reminder_text.started')
            prac_reminder_text.setAutoDraw(True)
        
        # *prac_reminder_keyResp* updates
        waitOnFlip = False
        if prac_reminder_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_reminder_keyResp.frameNStart = frameN  # exact frame index
            prac_reminder_keyResp.tStart = t  # local t and not account for scr refresh
            prac_reminder_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_reminder_keyResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_reminder_keyResp.started')
            prac_reminder_keyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prac_reminder_keyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prac_reminder_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prac_reminder_keyResp.status == STARTED and not waitOnFlip:
            theseKeys = prac_reminder_keyResp.getKeys(keyList=['8'], waitRelease=False)
            _prac_reminder_keyResp_allKeys.extend(theseKeys)
            if len(_prac_reminder_keyResp_allKeys):
                prac_reminder_keyResp.keys = _prac_reminder_keyResp_allKeys[-1].name  # just the last key pressed
                prac_reminder_keyResp.rt = _prac_reminder_keyResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_blockRemindersComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_blockReminders" ---
    for thisComponent in prac_blockRemindersComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if prac_reminder_keyResp.keys in ['', [], None]:  # No response was made
        prac_reminder_keyResp.keys = None
    prac_block_loop.addData('prac_reminder_keyResp.keys',prac_reminder_keyResp.keys)
    if prac_reminder_keyResp.keys != None:  # we had a response
        prac_block_loop.addData('prac_reminder_keyResp.rt', prac_reminder_keyResp.rt)
    # the Routine "prac_blockReminders" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "initFixation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    initFixation_img.setImage('img/transp_fixation.png')
    # keep track of which components have finished
    initFixationComponents = [initFixation_img]
    for thisComponent in initFixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "initFixation" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *initFixation_img* updates
        if initFixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            initFixation_img.frameNStart = frameN  # exact frame index
            initFixation_img.tStart = t  # local t and not account for scr refresh
            initFixation_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(initFixation_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'initFixation_img.started')
            initFixation_img.setAutoDraw(True)
        if initFixation_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > initFixation_img.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                initFixation_img.tStop = t  # not accounting for scr refresh
                initFixation_img.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'initFixation_img.stopped')
                initFixation_img.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in initFixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "initFixation" ---
    for thisComponent in initFixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # set up handler to look after randomisation of conditions etc
    prac_trial_loop = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(whichBlock),
        seed=None, name='prac_trial_loop')
    thisExp.addLoop(prac_trial_loop)  # add the loop to the experiment
    thisPrac_trial_loop = prac_trial_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_trial_loop.rgb)
    if thisPrac_trial_loop != None:
        for paramName in thisPrac_trial_loop:
            exec('{} = thisPrac_trial_loop[paramName]'.format(paramName))
    
    for thisPrac_trial_loop in prac_trial_loop:
        currentLoop = prac_trial_loop
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_trial_loop.rgb)
        if thisPrac_trial_loop != None:
            for paramName in thisPrac_trial_loop:
                exec('{} = thisPrac_trial_loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "prac_stimRoutine" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from prac_isi_code
        # pick the ISI for the next routine
        # this code component is set to 'both' because we need to remove the 'np'
        # at the start of np.linspace (this is a python library JS won't know what to call. 
        
        # make range from a to b in n stepsizes
        ISIRange = np.linspace(3500, 4000, 500)
        
        # picking from a shuffled array is easier for random selection in JS
        shuffle(ISIRange)
        thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
        
        # save this ISI to our output file
        prac_trial_loop.addData('ISI', thisISI)
        
        
        # show in console for debugging
        #print('thisISI: ', thisISI)
        bigFace.setImage(straightFace)
        # Run 'Begin Routine' code from bigFace_trig_code
        #set stimTriggerSent to false at the start of the trial. this way
        #when the stimulus is shown, we can change it to True. This variable
        #is used to ensure we only throw the stimulus EEG trigger once.
        stimTriggerSentZ1 = False
        cover_background_2.setImage('img/cover_background.png')
        prac_centerImg.setPos(locationC)
        prac_centerImg.setSize(imageSize)
        prac_centerImg.setImage(middleStim)
        prac_rightImg1.setPos(locationR)
        prac_rightImg1.setSize(imageSize)
        prac_rightImg1.setImage(rightStim)
        prac_rightImg2.setPos([0.077,0])
        prac_rightImg2.setSize(imageSize)
        prac_rightImg2.setImage(rightStim)
        prac_leftImg1.setPos(locationL)
        prac_leftImg1.setSize(imageSize)
        prac_leftImg1.setImage(leftStim)
        prac_leftImg2.setPos([-0.077,0])
        prac_leftImg2.setSize(imageSize)
        prac_leftImg2.setImage(leftStim)
        prac_fixImg.setImage('img/transp_fixation.png')
        # Run 'Begin Routine' code from prac_stimTrigger_code
        #set stimTriggerSent to false at the start of the trial. this way
        #when the stimulus is shown, we can change it to True. This variable
        #is used to ensure we only throw the stimulus EEG trigger once.
        stimTriggerSent = False
        # Run 'Begin Routine' code from distractor_trig_code
        #set stimTriggerSent to false at the start of the trial. this way
        #when the stimulus is shown, we can change it to True. This variable
        #is used to ensure we only throw the stimulus EEG trigger once.
        stimTriggerSentZ2 = False
        prac_stim_keyResp.keys = []
        prac_stim_keyResp.rt = []
        _prac_stim_keyResp_allKeys = []
        # Run 'Begin Routine' code from prac_respTrigger_code
        #clear out the keys_counbted variable at the start of the trial
        #this variable will hold the keys that have had eeg triggers thrown
        #already within a given trial.
        keys_counted = []
        # keep track of which components have finished
        prac_stimRoutineComponents = [bigFace, cover_background_2, prac_centerImg, prac_rightImg1, prac_rightImg2, prac_leftImg1, prac_leftImg2, prac_fixImg, prac_stim_keyResp]
        for thisComponent in prac_stimRoutineComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "prac_stimRoutine" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *bigFace* updates
            if bigFace.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bigFace.frameNStart = frameN  # exact frame index
                bigFace.tStart = t  # local t and not account for scr refresh
                bigFace.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bigFace, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bigFace.started')
                bigFace.setAutoDraw(True)
            if bigFace.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > bigFace.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    bigFace.tStop = t  # not accounting for scr refresh
                    bigFace.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'bigFace.stopped')
                    bigFace.setAutoDraw(False)
            # Run 'Each Frame' code from bigFace_trig_code
            #the first if statement below ensures that the subsequent if statements (and throwing of triggers)
            #only occurs once per trial. That is, only when the stimulus is presented (.status = STARTED) and
            #stimTriggerSent is still False. Once a trigger is sent, we change stimTriggerSent to True so that 
            #the stimulus eeg trigger will not be sent again for this trial
            if bigFace.status == STARTED and not stimTriggerSentZ1:
                    stimTriggerSentZ1 = True #switch stimTriggerSent to True so that the stimulus eeg trigger will not be sent again this trial
                    port.write([0x03]) #hexcode = 3; eeg trigger sent
                    time.sleep(PulseWidth) #how long to wait before clearing trigger port
                    port.write([0x00]) #clear trigger port by sending hexcode = 0
            
            
            # *cover_background_2* updates
            if cover_background_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cover_background_2.frameNStart = frameN  # exact frame index
                cover_background_2.tStart = t  # local t and not account for scr refresh
                cover_background_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cover_background_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cover_background_2.started')
                cover_background_2.setAutoDraw(True)
            if cover_background_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cover_background_2.tStartRefresh + 0.35-frameTolerance:
                    # keep track of stop time/frame for later
                    cover_background_2.tStop = t  # not accounting for scr refresh
                    cover_background_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cover_background_2.stopped')
                    cover_background_2.setAutoDraw(False)
            
            # *prac_centerImg* updates
            if prac_centerImg.status == NOT_STARTED and tThisFlip >= 0.15-frameTolerance:
                # keep track of start time/frame for later
                prac_centerImg.frameNStart = frameN  # exact frame index
                prac_centerImg.tStart = t  # local t and not account for scr refresh
                prac_centerImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_centerImg, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_centerImg.started')
                prac_centerImg.setAutoDraw(True)
            if prac_centerImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_centerImg.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_centerImg.tStop = t  # not accounting for scr refresh
                    prac_centerImg.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prac_centerImg.stopped')
                    prac_centerImg.setAutoDraw(False)
            
            # *prac_rightImg1* updates
            if prac_rightImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_rightImg1.frameNStart = frameN  # exact frame index
                prac_rightImg1.tStart = t  # local t and not account for scr refresh
                prac_rightImg1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_rightImg1, 'tStartRefresh')  # time at next scr refresh
                prac_rightImg1.setAutoDraw(True)
            if prac_rightImg1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_rightImg1.tStartRefresh + .350-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_rightImg1.tStop = t  # not accounting for scr refresh
                    prac_rightImg1.frameNStop = frameN  # exact frame index
                    prac_rightImg1.setAutoDraw(False)
            
            # *prac_rightImg2* updates
            if prac_rightImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_rightImg2.frameNStart = frameN  # exact frame index
                prac_rightImg2.tStart = t  # local t and not account for scr refresh
                prac_rightImg2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_rightImg2, 'tStartRefresh')  # time at next scr refresh
                prac_rightImg2.setAutoDraw(True)
            if prac_rightImg2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_rightImg2.tStartRefresh + .350-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_rightImg2.tStop = t  # not accounting for scr refresh
                    prac_rightImg2.frameNStop = frameN  # exact frame index
                    prac_rightImg2.setAutoDraw(False)
            
            # *prac_leftImg1* updates
            if prac_leftImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_leftImg1.frameNStart = frameN  # exact frame index
                prac_leftImg1.tStart = t  # local t and not account for scr refresh
                prac_leftImg1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_leftImg1, 'tStartRefresh')  # time at next scr refresh
                prac_leftImg1.setAutoDraw(True)
            if prac_leftImg1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_leftImg1.tStartRefresh + .350-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_leftImg1.tStop = t  # not accounting for scr refresh
                    prac_leftImg1.frameNStop = frameN  # exact frame index
                    prac_leftImg1.setAutoDraw(False)
            
            # *prac_leftImg2* updates
            if prac_leftImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_leftImg2.frameNStart = frameN  # exact frame index
                prac_leftImg2.tStart = t  # local t and not account for scr refresh
                prac_leftImg2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_leftImg2, 'tStartRefresh')  # time at next scr refresh
                prac_leftImg2.setAutoDraw(True)
            if prac_leftImg2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_leftImg2.tStartRefresh + .350-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_leftImg2.tStop = t  # not accounting for scr refresh
                    prac_leftImg2.frameNStop = frameN  # exact frame index
                    prac_leftImg2.setAutoDraw(False)
            
            # *prac_fixImg* updates
            if prac_fixImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_fixImg.frameNStart = frameN  # exact frame index
                prac_fixImg.tStart = t  # local t and not account for scr refresh
                prac_fixImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_fixImg, 'tStartRefresh')  # time at next scr refresh
                prac_fixImg.setAutoDraw(True)
            if prac_fixImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_fixImg.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_fixImg.tStop = t  # not accounting for scr refresh
                    prac_fixImg.frameNStop = frameN  # exact frame index
                    prac_fixImg.setAutoDraw(False)
            # Run 'Each Frame' code from prac_stimTrigger_code
            #the first if statement below ensures that the subsequent if statements (and throwing of triggers)
            #only occurs once per trial. That is, only when the stimulus is presented (.status = STARTED) and
            #stimTriggerSent is still False. Once a trigger is sent, we change stimTriggerSent to True so that 
            #the stimulus eeg trigger will not be sent again for this trial
            if prac_centerImg.status == STARTED and not stimTriggerSent:
                if stimNum == 5: #code denoting which stimulus array was sent (from excel file)
                    stimTriggerSent = True #switch stimTriggerSent to True so that the stimulus eeg trigger will not be sent again this trial
                    port.write([0x0D]) #hexcode = 13; eeg trigger sent
                    time.sleep(PulseWidth) #how long to wait before clearing trigger port
                    port.write([0x00]) #clear trigger port by sending hexcode = 0
                elif stimNum == 6:
                    stimTriggerSent = True
                    port.write([0x0E]) # S14
                    time.sleep(PulseWidth)
                    port.write([0x00])
                elif stimNum == 7:
                    stimTriggerSent = True
                    port.write([0x0F]) # S15
                    time.sleep(PulseWidth)
                    port.write([0x00])
                elif stimNum == 8:
                    stimTriggerSent = True
                    port.write([0x10]) # S16
                    time.sleep(PulseWidth)
                    port.write([0x00])
            # Run 'Each Frame' code from distractor_trig_code
            #the first if statement below ensures that the subsequent if statements (and throwing of triggers)
            #only occurs once per trial. That is, only when the stimulus is presented (.status = STARTED) and
            #stimTriggerSent is still False. Once a trigger is sent, we change stimTriggerSent to True so that 
            #the stimulus eeg trigger will not be sent again for this trial
            if prac_leftImg1.status == STARTED and not stimTriggerSentZ2:
                if stimNum == 5: #code denoting which stimulus array was sent (from excel file)
                    stimTriggerSentZ2 = True #switch stimTriggerSent to True so that the stimulus eeg trigger will not be sent again this trial
                    port.write([0x0F]) #hexcode = 15; eeg trigger sent
                    time.sleep(PulseWidth) #how long to wait before clearing trigger port
                    port.write([0x00]) #clear trigger port by sending hexcode = 0
                elif stimNum == 6:
                    stimTriggerSentZ2 = True
                    port.write([0x10]) #16
                    time.sleep(PulseWidth)
                    port.write([0x00])
                elif stimNum == 7:
                    stimTriggerSentZ2 = True
                    port.write([0x11]) #17
                    time.sleep(PulseWidth)
                    port.write([0x00])
                elif stimNum == 8:
                    stimTriggerSentZ2 = True
                    port.write([0x12]) #18
                    time.sleep(PulseWidth)
                    port.write([0x00])
            
            # *prac_stim_keyResp* updates
            waitOnFlip = False
            if prac_stim_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_stim_keyResp.frameNStart = frameN  # exact frame index
                prac_stim_keyResp.tStart = t  # local t and not account for scr refresh
                prac_stim_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_stim_keyResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_stim_keyResp.started')
                prac_stim_keyResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(prac_stim_keyResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(prac_stim_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if prac_stim_keyResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_stim_keyResp.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_stim_keyResp.tStop = t  # not accounting for scr refresh
                    prac_stim_keyResp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prac_stim_keyResp.stopped')
                    prac_stim_keyResp.status = FINISHED
            if prac_stim_keyResp.status == STARTED and not waitOnFlip:
                theseKeys = prac_stim_keyResp.getKeys(keyList=['1','8'], waitRelease=False)
                _prac_stim_keyResp_allKeys.extend(theseKeys)
                if len(_prac_stim_keyResp_allKeys):
                    prac_stim_keyResp.keys = [key.name for key in _prac_stim_keyResp_allKeys]  # storing all keys
                    prac_stim_keyResp.rt = [key.rt for key in _prac_stim_keyResp_allKeys]
            # Run 'Each Frame' code from prac_respTrigger_code
            if prac_stim_keyResp.keys and len(prac_stim_keyResp.keys) > len(keys_counted):# A key response has been made but we haven't yet "counted" it
                keys_counted.append(prac_stim_keyResp.keys[-1]) #add this response to list of keys pressed this trial
                if len(prac_stim_keyResp.keys) < 2: #if this is  the first response
                    if prac_stim_keyResp.keys[-1] == '1':
                        if target == 'left': #correct response
                            port.write([0x0B]) # 11
                            time.sleep(PulseWidth)
                            port.write([0x00])
                        elif target == 'right': #error response
                            port.write([0x0C])# 12
                            time.sleep(PulseWidth)
                            port.write([0x00])
                    elif prac_stim_keyResp.keys[-1] == '8':
                        if target == 'right': #correct response
                            port.write([0x0B]) # 11
                            time.sleep(PulseWidth)
                            port.write([0x00])
                        elif target == 'left': #error response
                            port.write([0x0C])# 12
                            time.sleep(PulseWidth)
                            port.write([0x00])
                elif len(prac_stim_keyResp.keys) >= 2: #if this is NOT the first response
                    if prac_stim_keyResp.keys[-1] == '1':
                        if target == 'left': #technically correct response, but not the first response made
                            port.write([0x15]) # 21
                            time.sleep(PulseWidth)
                            port.write([0x00])
                        elif target == 'right': #technically error response, but not the first response made
                            port.write([0x16])# 22
                            time.sleep(PulseWidth)
                            port.write([0x00])
                    elif prac_stim_keyResp.keys[-1] == '8':
                        if target == 'right': #technically correct response, but not the first response made
                            port.write([0x15]) # 21
                            time.sleep(PulseWidth)
                            port.write([0x00])
                        elif target == 'left': #technically error response, but not the first response made
                            port.write([0x16])# 22
                            time.sleep(PulseWidth)
                            port.write([0x00])
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prac_stimRoutineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prac_stimRoutine" ---
        for thisComponent in prac_stimRoutineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if prac_stim_keyResp.keys in ['', [], None]:  # No response was made
            prac_stim_keyResp.keys = None
        prac_trial_loop.addData('prac_stim_keyResp.keys',prac_stim_keyResp.keys)
        if prac_stim_keyResp.keys != None:  # we had a response
            prac_trial_loop.addData('prac_stim_keyResp.rt', prac_stim_keyResp.rt)
        # Run 'End Routine' code from prac_respTrigger_code
        
        #instead of including here, should instead include something
        #in each frame section that computes t at stim onset and then
        #when thisISI - t <= .05 (50 ms) and then at that point we throw
        #the no-resp marker...
        
        #if not prac_stim_keyResp.keys or len(prac_stim_keyResp.keys) == 0:
        #            port.write([0x63]) # 99
        #            time.sleep(PulseWidth)
        #            port.write([0x00])
        # Run 'End Routine' code from prac_accuracy_code
        trialNum = trialNum + 1 #iterate trial number for this block
        
        if prac_stim_keyResp.keys: #if at least one response was made this trial
            if prac_stim_keyResp.keys[0] == '1': #if the FIRST button pressed was a '1'
                if target == 'left': #if a left target stim was shown this trial
                    accuracy = 1 #mark this trial as correct
                    numCorr = numCorr +1 #iterate number of correct responses for this block
                elif target == 'right': #if a right target stim was shown this trial
                    accuracy = 0 #mark this trial as an error
            elif prac_stim_keyResp.keys[0] == '8': #if the FIRST button pressed was a '8'
                if target == 'right': #if a right target stim was shown this trial
                    accuracy = 1 #mark this trial as correct
                    numCorr = numCorr +1 #iterate number of correct responses for this block
                elif target == 'left': #if a left target stim was shown this trial
                    accuracy = 0 #mark this trial as an error
                    
        # save this trial's accuracy to our output file
        prac_trial_loop.addData('accuracy', accuracy)
        # the Routine "prac_stimRoutine" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'prac_trial_loop'
    
    
    # --- Prepare to start Routine "prac_blockFeed" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from prac_blockFeed_code
    blockAcc = numCorr / trialNum #compute accuracy for this block
    
    if blockAcc >= .75: #if accuracy >= 75% then say practice is complete and end practice loop to continue to main exp
        outPut = 'You have completed the practice' #feedback presented
        prac_block_loop.finished = True #end practice loop to continue to main exp
    elif blockAcc <= .75: #if accuracy < 75% then say that practice needs to be repeated and DO NOT end practice loop, instead, allow it to repeat
        outPut = 'Please try the practice again' #feedback presented
        prac_block_loop.finished = False #DO NOT end practice loop and allow to repeat
    
    #reset the following variables to zero before the next practice block starts
    trialNum = 0
    numCorr = 0
    prac_blockFeed_text.setText(outPut)
    prac_blockFeed_keyResp.keys = []
    prac_blockFeed_keyResp.rt = []
    _prac_blockFeed_keyResp_allKeys = []
    # keep track of which components have finished
    prac_blockFeedComponents = [prac_blockFeed_text, prac_pressContinue, prac_blockFeed_keyResp]
    for thisComponent in prac_blockFeedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_blockFeed" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_blockFeed_text* updates
        if prac_blockFeed_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_blockFeed_text.frameNStart = frameN  # exact frame index
            prac_blockFeed_text.tStart = t  # local t and not account for scr refresh
            prac_blockFeed_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_blockFeed_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_blockFeed_text.started')
            prac_blockFeed_text.setAutoDraw(True)
        
        # *prac_pressContinue* updates
        if prac_pressContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_pressContinue.frameNStart = frameN  # exact frame index
            prac_pressContinue.tStart = t  # local t and not account for scr refresh
            prac_pressContinue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_pressContinue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_pressContinue.started')
            prac_pressContinue.setAutoDraw(True)
        
        # *prac_blockFeed_keyResp* updates
        waitOnFlip = False
        if prac_blockFeed_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_blockFeed_keyResp.frameNStart = frameN  # exact frame index
            prac_blockFeed_keyResp.tStart = t  # local t and not account for scr refresh
            prac_blockFeed_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_blockFeed_keyResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_blockFeed_keyResp.started')
            prac_blockFeed_keyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prac_blockFeed_keyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prac_blockFeed_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prac_blockFeed_keyResp.status == STARTED and not waitOnFlip:
            theseKeys = prac_blockFeed_keyResp.getKeys(keyList=['8'], waitRelease=False)
            _prac_blockFeed_keyResp_allKeys.extend(theseKeys)
            if len(_prac_blockFeed_keyResp_allKeys):
                prac_blockFeed_keyResp.keys = _prac_blockFeed_keyResp_allKeys[-1].name  # just the last key pressed
                prac_blockFeed_keyResp.rt = _prac_blockFeed_keyResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_blockFeedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_blockFeed" ---
    for thisComponent in prac_blockFeedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if prac_blockFeed_keyResp.keys in ['', [], None]:  # No response was made
        prac_blockFeed_keyResp.keys = None
    prac_block_loop.addData('prac_blockFeed_keyResp.keys',prac_blockFeed_keyResp.keys)
    if prac_blockFeed_keyResp.keys != None:  # we had a response
        prac_block_loop.addData('prac_blockFeed_keyResp.rt', prac_blockFeed_keyResp.rt)
    # the Routine "prac_blockFeed" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0 repeats of 'prac_block_loop'


# --- Prepare to start Routine "ringBell" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
bellKey.keys = []
bellKey.rt = []
_bellKey_allKeys = []
# keep track of which components have finished
ringBellComponents = [ringBell_text, bellKey]
for thisComponent in ringBellComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "ringBell" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ringBell_text* updates
    if ringBell_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ringBell_text.frameNStart = frameN  # exact frame index
        ringBell_text.tStart = t  # local t and not account for scr refresh
        ringBell_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ringBell_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ringBell_text.started')
        ringBell_text.setAutoDraw(True)
    
    # *bellKey* updates
    waitOnFlip = False
    if bellKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bellKey.frameNStart = frameN  # exact frame index
        bellKey.tStart = t  # local t and not account for scr refresh
        bellKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bellKey, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'bellKey.started')
        bellKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(bellKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(bellKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if bellKey.status == STARTED and not waitOnFlip:
        theseKeys = bellKey.getKeys(keyList=['c'], waitRelease=False)
        _bellKey_allKeys.extend(theseKeys)
        if len(_bellKey_allKeys):
            bellKey.keys = _bellKey_allKeys[-1].name  # just the last key pressed
            bellKey.rt = _bellKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ringBellComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ringBell" ---
for thisComponent in ringBellComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if bellKey.keys in ['', [], None]:  # No response was made
    bellKey.keys = None
thisExp.addData('bellKey.keys',bellKey.keys)
if bellKey.keys != None:  # we had a response
    thisExp.addData('bellKey.rt', bellKey.rt)
thisExp.nextEntry()
# the Routine "ringBell" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
task_block_loop = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blockSelect.csv'),
    seed=None, name='task_block_loop')
thisExp.addLoop(task_block_loop)  # add the loop to the experiment
thisTask_block_loop = task_block_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTask_block_loop.rgb)
if thisTask_block_loop != None:
    for paramName in thisTask_block_loop:
        exec('{} = thisTask_block_loop[paramName]'.format(paramName))

for thisTask_block_loop in task_block_loop:
    currentLoop = task_block_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTask_block_loop.rgb)
    if thisTask_block_loop != None:
        for paramName in thisTask_block_loop:
            exec('{} = thisTask_block_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "task_blockReminders" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from task_blockReminder_code
    blockCounter = blockCounter +1
    
    if blockCounter == 1:
        blockNumText = 'Block 1 of 12'
    elif blockCounter == 2:
        blockNumText = 'Block 2 of 12'
    elif blockCounter == 3:
        blockNumText = 'Block 3 of 12'
    elif blockCounter == 4:
        blockNumText = 'Block 4 of 12'
    elif blockCounter == 5:
        blockNumText = 'Block 5 of 12'
    elif blockCounter == 6:
        blockNumText = 'Block 6 of 12'
    elif blockCounter == 7:
        blockNumText = 'Block 7 of 12'
    elif blockCounter == 8:
        blockNumText = 'Block 8 of 12'
    elif blockCounter == 9:
        blockNumText = 'Block 9 of 12'
    elif blockCounter == 10:
        blockNumText = 'Block 10 of 12'    
    elif blockCounter == 11:
        blockNumText = 'Block 11 of 12'    
    elif blockCounter == 12:
        blockNumText = 'Block 12 of 12'    
        
        
    task_blockText.setText(blockNumText)
    task_blockReminders_keyResp.keys = []
    task_blockReminders_keyResp.rt = []
    _task_blockReminders_keyResp_allKeys = []
    # keep track of which components have finished
    task_blockRemindersComponents = [task_blockText, task_blockReminders_text, task_blockReminders_keyResp]
    for thisComponent in task_blockRemindersComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "task_blockReminders" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *task_blockText* updates
        if task_blockText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_blockText.frameNStart = frameN  # exact frame index
            task_blockText.tStart = t  # local t and not account for scr refresh
            task_blockText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_blockText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'task_blockText.started')
            task_blockText.setAutoDraw(True)
        
        # *task_blockReminders_text* updates
        if task_blockReminders_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_blockReminders_text.frameNStart = frameN  # exact frame index
            task_blockReminders_text.tStart = t  # local t and not account for scr refresh
            task_blockReminders_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_blockReminders_text, 'tStartRefresh')  # time at next scr refresh
            task_blockReminders_text.setAutoDraw(True)
        
        # *task_blockReminders_keyResp* updates
        waitOnFlip = False
        if task_blockReminders_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_blockReminders_keyResp.frameNStart = frameN  # exact frame index
            task_blockReminders_keyResp.tStart = t  # local t and not account for scr refresh
            task_blockReminders_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_blockReminders_keyResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'task_blockReminders_keyResp.started')
            task_blockReminders_keyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(task_blockReminders_keyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(task_blockReminders_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if task_blockReminders_keyResp.status == STARTED and not waitOnFlip:
            theseKeys = task_blockReminders_keyResp.getKeys(keyList=['8'], waitRelease=False)
            _task_blockReminders_keyResp_allKeys.extend(theseKeys)
            if len(_task_blockReminders_keyResp_allKeys):
                task_blockReminders_keyResp.keys = _task_blockReminders_keyResp_allKeys[-1].name  # just the last key pressed
                task_blockReminders_keyResp.rt = _task_blockReminders_keyResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in task_blockRemindersComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "task_blockReminders" ---
    for thisComponent in task_blockRemindersComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if task_blockReminders_keyResp.keys in ['', [], None]:  # No response was made
        task_blockReminders_keyResp.keys = None
    task_block_loop.addData('task_blockReminders_keyResp.keys',task_blockReminders_keyResp.keys)
    if task_blockReminders_keyResp.keys != None:  # we had a response
        task_block_loop.addData('task_blockReminders_keyResp.rt', task_blockReminders_keyResp.rt)
    # the Routine "task_blockReminders" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "initFixation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    initFixation_img.setImage('img/transp_fixation.png')
    # keep track of which components have finished
    initFixationComponents = [initFixation_img]
    for thisComponent in initFixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "initFixation" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *initFixation_img* updates
        if initFixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            initFixation_img.frameNStart = frameN  # exact frame index
            initFixation_img.tStart = t  # local t and not account for scr refresh
            initFixation_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(initFixation_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'initFixation_img.started')
            initFixation_img.setAutoDraw(True)
        if initFixation_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > initFixation_img.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                initFixation_img.tStop = t  # not accounting for scr refresh
                initFixation_img.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'initFixation_img.stopped')
                initFixation_img.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in initFixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "initFixation" ---
    for thisComponent in initFixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # set up handler to look after randomisation of conditions etc
    task_trial_loop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(whichBlock),
        seed=None, name='task_trial_loop')
    thisExp.addLoop(task_trial_loop)  # add the loop to the experiment
    thisTask_trial_loop = task_trial_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTask_trial_loop.rgb)
    if thisTask_trial_loop != None:
        for paramName in thisTask_trial_loop:
            exec('{} = thisTask_trial_loop[paramName]'.format(paramName))
    
    for thisTask_trial_loop in task_trial_loop:
        currentLoop = task_trial_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTask_trial_loop.rgb)
        if thisTask_trial_loop != None:
            for paramName in thisTask_trial_loop:
                exec('{} = thisTask_trial_loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "task_stimRoutine" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from task_isi_code
        # pick the ISI for the next routine
        # this code component is set to 'both' because we need to remove the 'np'
        # at the start of np.linspace (this is a python library JS won't know what to call. 
        
        # make range from a to b in n stepsizes
        ISIRange = np.linspace(3500, 4000, 500)
        
        # picking from a shuffled array is easier for random selection in JS
        shuffle(ISIRange)
        thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
        
        # save this ISI to our output file
        task_trial_loop.addData('ISI', thisISI)
        
        bigFace_2.setImage(straightFace)
        # Run 'Begin Routine' code from bigFace_trig_code_2
        #set stimTriggerSent to false at the start of the trial. this way
        #when the stimulus is shown, we can change it to True. This variable
        #is used to ensure we only throw the stimulus EEG trigger once.
        stimTriggerSentZ1 = False
        task_centerImg.setPos(locationC)
        task_centerImg.setSize(imageSize)
        task_centerImg.setImage(middleStim)
        task_rightImg1.setPos(locationR)
        task_rightImg1.setSize(imageSize)
        task_rightImg1.setImage(rightStim)
        task_rightImg2.setPos([0.077,0])
        task_rightImg2.setSize(imageSize)
        task_rightImg2.setImage(rightStim)
        task_leftImg1.setPos(locationL)
        task_leftImg1.setSize(imageSize)
        task_leftImg1.setImage(leftStim)
        task_leftImg2.setPos([-0.077,0])
        task_leftImg2.setSize(imageSize)
        task_leftImg2.setImage(leftStim)
        task_fixImg.setImage('img/transp_fixation.png')
        # Run 'Begin Routine' code from task_stimTrigger_code
        #set stimTriggerSent to false at the start of the trial. this way
        #when the stimulus is shown, we can change it to True. This variable
        #is used to ensure we only throw the stimulus EEG trigger once.
        stimTriggerSent = False
        # Run 'Begin Routine' code from distractor_trig_code_2
        #set stimTriggerSent to false at the start of the trial. this way
        #when the stimulus is shown, we can change it to True. This variable
        #is used to ensure we only throw the stimulus EEG trigger once.
        stimTriggerSentZ2 = False
        task1_stim_keyResp.keys = []
        task1_stim_keyResp.rt = []
        _task1_stim_keyResp_allKeys = []
        # Run 'Begin Routine' code from task_respTrigger_code
        #clear out the keys_counbted variable at the start of the trial
        #this variable will hold the keys that have had eeg triggers thrown
        #already within a given trial.
        keys_counted = []
        # keep track of which components have finished
        task_stimRoutineComponents = [bigFace_2, cover_background, task_centerImg, task_rightImg1, task_rightImg2, task_leftImg1, task_leftImg2, task_fixImg, task1_stim_keyResp]
        for thisComponent in task_stimRoutineComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "task_stimRoutine" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *bigFace_2* updates
            if bigFace_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bigFace_2.frameNStart = frameN  # exact frame index
                bigFace_2.tStart = t  # local t and not account for scr refresh
                bigFace_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bigFace_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bigFace_2.started')
                bigFace_2.setAutoDraw(True)
            if bigFace_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > bigFace_2.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    bigFace_2.tStop = t  # not accounting for scr refresh
                    bigFace_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'bigFace_2.stopped')
                    bigFace_2.setAutoDraw(False)
            # Run 'Each Frame' code from bigFace_trig_code_2
            #the first if statement below ensures that the subsequent if statements (and throwing of triggers)
            #only occurs once per trial. That is, only when the stimulus is presented (.status = STARTED) and
            #stimTriggerSent is still False. Once a trigger is sent, we change stimTriggerSent to True so that 
            #the stimulus eeg trigger will not be sent again for this trial
            if bigFace_2.status == STARTED and not stimTriggerSentZ1:
                    stimTriggerSentZ1 = True #switch stimTriggerSent to True so that the stimulus eeg trigger will not be sent again this trial
                    port.write([0x03]) #hexcode = 3; eeg trigger sent
                    time.sleep(PulseWidth) #how long to wait before clearing trigger port
                    port.write([0x00]) #clear trigger port by sending hexcode = 0
            
            
            # *cover_background* updates
            if cover_background.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cover_background.frameNStart = frameN  # exact frame index
                cover_background.tStart = t  # local t and not account for scr refresh
                cover_background.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cover_background, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cover_background.started')
                cover_background.setAutoDraw(True)
            if cover_background.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cover_background.tStartRefresh + 0.35-frameTolerance:
                    # keep track of stop time/frame for later
                    cover_background.tStop = t  # not accounting for scr refresh
                    cover_background.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cover_background.stopped')
                    cover_background.setAutoDraw(False)
            
            # *task_centerImg* updates
            if task_centerImg.status == NOT_STARTED and tThisFlip >= 0.15-frameTolerance:
                # keep track of start time/frame for later
                task_centerImg.frameNStart = frameN  # exact frame index
                task_centerImg.tStart = t  # local t and not account for scr refresh
                task_centerImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_centerImg, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'task_centerImg.started')
                task_centerImg.setAutoDraw(True)
            if task_centerImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task_centerImg.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    task_centerImg.tStop = t  # not accounting for scr refresh
                    task_centerImg.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'task_centerImg.stopped')
                    task_centerImg.setAutoDraw(False)
            
            # *task_rightImg1* updates
            if task_rightImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_rightImg1.frameNStart = frameN  # exact frame index
                task_rightImg1.tStart = t  # local t and not account for scr refresh
                task_rightImg1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_rightImg1, 'tStartRefresh')  # time at next scr refresh
                task_rightImg1.setAutoDraw(True)
            if task_rightImg1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task_rightImg1.tStartRefresh + .35-frameTolerance:
                    # keep track of stop time/frame for later
                    task_rightImg1.tStop = t  # not accounting for scr refresh
                    task_rightImg1.frameNStop = frameN  # exact frame index
                    task_rightImg1.setAutoDraw(False)
            
            # *task_rightImg2* updates
            if task_rightImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_rightImg2.frameNStart = frameN  # exact frame index
                task_rightImg2.tStart = t  # local t and not account for scr refresh
                task_rightImg2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_rightImg2, 'tStartRefresh')  # time at next scr refresh
                task_rightImg2.setAutoDraw(True)
            if task_rightImg2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task_rightImg2.tStartRefresh + .350-frameTolerance:
                    # keep track of stop time/frame for later
                    task_rightImg2.tStop = t  # not accounting for scr refresh
                    task_rightImg2.frameNStop = frameN  # exact frame index
                    task_rightImg2.setAutoDraw(False)
            
            # *task_leftImg1* updates
            if task_leftImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_leftImg1.frameNStart = frameN  # exact frame index
                task_leftImg1.tStart = t  # local t and not account for scr refresh
                task_leftImg1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_leftImg1, 'tStartRefresh')  # time at next scr refresh
                task_leftImg1.setAutoDraw(True)
            if task_leftImg1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task_leftImg1.tStartRefresh + .35-frameTolerance:
                    # keep track of stop time/frame for later
                    task_leftImg1.tStop = t  # not accounting for scr refresh
                    task_leftImg1.frameNStop = frameN  # exact frame index
                    task_leftImg1.setAutoDraw(False)
            
            # *task_leftImg2* updates
            if task_leftImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_leftImg2.frameNStart = frameN  # exact frame index
                task_leftImg2.tStart = t  # local t and not account for scr refresh
                task_leftImg2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_leftImg2, 'tStartRefresh')  # time at next scr refresh
                task_leftImg2.setAutoDraw(True)
            if task_leftImg2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task_leftImg2.tStartRefresh + .350-frameTolerance:
                    # keep track of stop time/frame for later
                    task_leftImg2.tStop = t  # not accounting for scr refresh
                    task_leftImg2.frameNStop = frameN  # exact frame index
                    task_leftImg2.setAutoDraw(False)
            
            # *task_fixImg* updates
            if task_fixImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_fixImg.frameNStart = frameN  # exact frame index
                task_fixImg.tStart = t  # local t and not account for scr refresh
                task_fixImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_fixImg, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'task_fixImg.started')
                task_fixImg.setAutoDraw(True)
            if task_fixImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task_fixImg.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    task_fixImg.tStop = t  # not accounting for scr refresh
                    task_fixImg.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'task_fixImg.stopped')
                    task_fixImg.setAutoDraw(False)
            # Run 'Each Frame' code from task_stimTrigger_code
            #the first if statement below ensures that the subsequent if statements (and throwing of triggers)
            #only occurs once per trial. That is, only when the stimulus is presented (.status = STARTED) and
            #stimTriggerSent is still False. Once a trigger is sent, we change stimTriggerSent to True so that 
            #the stimulus eeg trigger will not be sent again for this trial
            if task_centerImg.status == STARTED and not stimTriggerSent:
                if stimNum == 5: #code denoting which stimulus array was sent (from excel file)
                    stimTriggerSent = True #switch stimTriggerSent to True so that the stimulus eeg trigger will not be sent again this trial
                    port.write([0x05]) #hexcode = 1; eeg trigger sent
                    time.sleep(PulseWidth) #how long to wait before clearing trigger port
                    port.write([0x00]) #clear trigger port by sending hexcode = 0
                elif stimNum == 6:
                    stimTriggerSent = True
                    port.write([0x06])
                    time.sleep(PulseWidth)
                    port.write([0x00])
                elif stimNum == 7:
                    stimTriggerSent = True
                    port.write([0x07])
                    time.sleep(PulseWidth)
                    port.write([0x00])
                elif stimNum == 8:
                    stimTriggerSent = True
                    port.write([0x08])
                    time.sleep(PulseWidth)
                    port.write([0x00])
            # Run 'Each Frame' code from distractor_trig_code_2
            #the first if statement below ensures that the subsequent if statements (and throwing of triggers)
            #only occurs once per trial. That is, only when the stimulus is presented (.status = STARTED) and
            #stimTriggerSent is still False. Once a trigger is sent, we change stimTriggerSent to True so that 
            #the stimulus eeg trigger will not be sent again for this trial
            if task_leftImg1.status == STARTED and not stimTriggerSentZ2:
                if stimNum == 5: #code denoting which stimulus array was sent (from excel file)
                    stimTriggerSentZ2 = True #switch stimTriggerSent to True so that the stimulus eeg trigger will not be sent again this trial
                    port.write([0x0F]) #hexcode = 15; eeg trigger sent
                    time.sleep(PulseWidth) #how long to wait before clearing trigger port
                    port.write([0x00]) #clear trigger port by sending hexcode = 0
                elif stimNum == 6:
                    stimTriggerSentZ2 = True
                    port.write([0x10]) #16
                    time.sleep(PulseWidth)
                    port.write([0x00])
                elif stimNum == 7:
                    stimTriggerSentZ2 = True
                    port.write([0x11]) #17
                    time.sleep(PulseWidth)
                    port.write([0x00])
                elif stimNum == 8:
                    stimTriggerSentZ2 = True
                    port.write([0x12]) #18
                    time.sleep(PulseWidth)
                    port.write([0x00])
            
            # *task1_stim_keyResp* updates
            waitOnFlip = False
            if task1_stim_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task1_stim_keyResp.frameNStart = frameN  # exact frame index
                task1_stim_keyResp.tStart = t  # local t and not account for scr refresh
                task1_stim_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task1_stim_keyResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'task1_stim_keyResp.started')
                task1_stim_keyResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(task1_stim_keyResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(task1_stim_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if task1_stim_keyResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task1_stim_keyResp.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    task1_stim_keyResp.tStop = t  # not accounting for scr refresh
                    task1_stim_keyResp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'task1_stim_keyResp.stopped')
                    task1_stim_keyResp.status = FINISHED
            if task1_stim_keyResp.status == STARTED and not waitOnFlip:
                theseKeys = task1_stim_keyResp.getKeys(keyList=['1','8'], waitRelease=False)
                _task1_stim_keyResp_allKeys.extend(theseKeys)
                if len(_task1_stim_keyResp_allKeys):
                    task1_stim_keyResp.keys = [key.name for key in _task1_stim_keyResp_allKeys]  # storing all keys
                    task1_stim_keyResp.rt = [key.rt for key in _task1_stim_keyResp_allKeys]
            # Run 'Each Frame' code from task_respTrigger_code
            if task1_stim_keyResp.keys and len(task1_stim_keyResp.keys) > len(keys_counted):# A key response has been made but we haven't yet "counted" it
                keys_counted.append(task1_stim_keyResp.keys[-1]) #add this response to list of keys pressed this trial
                if len(task1_stim_keyResp.keys) < 2: #if this is  the first response
                    if task1_stim_keyResp.keys[-1] == '1':
                        if target == 'left': #correct response
                            port.write([0x0B]) # 11
                            time.sleep(PulseWidth)
                            port.write([0x00])
                        elif target == 'right': #error response
                            port.write([0x0C])# 12
                            time.sleep(PulseWidth)
                            port.write([0x00])
                    elif task1_stim_keyResp.keys[-1] == '8':
                        if target == 'right': #correct response
                            port.write([0x0B]) # 11
                            time.sleep(PulseWidth)
                            port.write([0x00])
                        elif target == 'left': #error response
                            port.write([0x0C])# 12
                            time.sleep(PulseWidth)
                            port.write([0x00])
                elif len(task1_stim_keyResp.keys) >= 2: #if this is NOT the first response
                    if task1_stim_keyResp.keys[-1] == '1':
                        if target == 'left': #technically correct response, but not the first response made
                            port.write([0x15]) # 21
                            time.sleep(PulseWidth)
                            port.write([0x00])
                        elif target == 'right': #technically error response, but not the first response made
                            port.write([0x16])# 22
                            time.sleep(PulseWidth)
                            port.write([0x00])
                    elif task1_stim_keyResp.keys[-1] == '8':
                        if target == 'right': #technically correct response, but not the first response made
                            port.write([0x15]) # 21
                            time.sleep(PulseWidth)
                            port.write([0x00])
                        elif target == 'left': #technically error response, but not the first response made
                            port.write([0x16])# 22
                            time.sleep(PulseWidth)
                            port.write([0x00])
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in task_stimRoutineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "task_stimRoutine" ---
        for thisComponent in task_stimRoutineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if task1_stim_keyResp.keys in ['', [], None]:  # No response was made
            task1_stim_keyResp.keys = None
        task_trial_loop.addData('task1_stim_keyResp.keys',task1_stim_keyResp.keys)
        if task1_stim_keyResp.keys != None:  # we had a response
            task_trial_loop.addData('task1_stim_keyResp.rt', task1_stim_keyResp.rt)
        # Run 'End Routine' code from task_respTrigger_code
        
        #instead of including here, should instead include something
        #in each frame section that computes t at stim onset and then
        #when thisISI - t <= .05 (50 ms) and then at that point we throw
        #the no-resp marker...
        
        #if not prac_stim_keyResp.keys or len(prac_stim_keyResp.keys) == 0:
        #            port.write([0x63]) # 99
        #            time.sleep(PulseWidth)
        #            port.write([0x00])
        # Run 'End Routine' code from task_accuracy_code
        trialNum = trialNum + 1 #iterate trial number for this block
        
        if task1_stim_keyResp.keys: #if at least one response was made this trial
            if task1_stim_keyResp.keys[0] == '1': #if the FIRST button pressed was a '1'
                if target == 'left': #if a left target stim was shown this trial
                    accuracy = 1 #mark this trial as correct
                    numCorr = numCorr +1 #iterate number of correct responses for this block
                elif target == 'right': #if a right target stim was shown this trial
                    accuracy = 0 #mark this trial as an error
            elif task1_stim_keyResp.keys[0] == '8': #if the FIRST button pressed was a '8'
                if target == 'right': #if a right target stim was shown this trial
                    accuracy = 1 #mark this trial as correct
                    numCorr = numCorr +1 #iterate number of correct responses for this block
                elif target == 'left': #if a left target stim was shown this trial
                    accuracy = 0 #mark this trial as an error
                    
        # save this trial's accuracy to our output file
        task_trial_loop.addData('accuracy', accuracy)
        # the Routine "task_stimRoutine" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'task_trial_loop'
    
    
    # --- Prepare to start Routine "task_blockFeed" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from task_blockFeed_code
    blockAcc = numCorr / trialNum #compute accuracy for this block
    
    if blockCounter < 10:
        if blockAcc >= .75:
            if blockAcc < .9:
                blockFeed = 'Good job'
                blockFeedCat = 1
            elif blockAcc >= .9:
                blockFeed = 'Respond faster'
                blockFeedCat = 2
        elif blockAcc < .75:
            blockFeed = 'Respond more accurately'
            blockFeedCat = 3
    elif blockCounter == 10:
        'You have completed all blocks'
    
    # save this block's feedback to our output file
    task_trial_loop.addData('blockFeedCat', blockFeedCat)
    
    #reset the following variables to zero before next block starts
    trialNum = 0
    numCorr = 0
    task_blockFeed_text.setText(blockFeed)
    task_blockFeed_text2.setText('Press the right button')
    task_blockFeed_keyResp.keys = []
    task_blockFeed_keyResp.rt = []
    _task_blockFeed_keyResp_allKeys = []
    # keep track of which components have finished
    task_blockFeedComponents = [task_blockFeed_text, task_blockFeed_text2, task_blockFeed_keyResp]
    for thisComponent in task_blockFeedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "task_blockFeed" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *task_blockFeed_text* updates
        if task_blockFeed_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_blockFeed_text.frameNStart = frameN  # exact frame index
            task_blockFeed_text.tStart = t  # local t and not account for scr refresh
            task_blockFeed_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_blockFeed_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'task_blockFeed_text.started')
            task_blockFeed_text.setAutoDraw(True)
        
        # *task_blockFeed_text2* updates
        if task_blockFeed_text2.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            task_blockFeed_text2.frameNStart = frameN  # exact frame index
            task_blockFeed_text2.tStart = t  # local t and not account for scr refresh
            task_blockFeed_text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_blockFeed_text2, 'tStartRefresh')  # time at next scr refresh
            task_blockFeed_text2.setAutoDraw(True)
        
        # *task_blockFeed_keyResp* updates
        waitOnFlip = False
        if task_blockFeed_keyResp.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            task_blockFeed_keyResp.frameNStart = frameN  # exact frame index
            task_blockFeed_keyResp.tStart = t  # local t and not account for scr refresh
            task_blockFeed_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_blockFeed_keyResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'task_blockFeed_keyResp.started')
            task_blockFeed_keyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(task_blockFeed_keyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(task_blockFeed_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if task_blockFeed_keyResp.status == STARTED and not waitOnFlip:
            theseKeys = task_blockFeed_keyResp.getKeys(keyList=['8'], waitRelease=False)
            _task_blockFeed_keyResp_allKeys.extend(theseKeys)
            if len(_task_blockFeed_keyResp_allKeys):
                task_blockFeed_keyResp.keys = _task_blockFeed_keyResp_allKeys[-1].name  # just the last key pressed
                task_blockFeed_keyResp.rt = _task_blockFeed_keyResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in task_blockFeedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "task_blockFeed" ---
    for thisComponent in task_blockFeedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if task_blockFeed_keyResp.keys in ['', [], None]:  # No response was made
        task_blockFeed_keyResp.keys = None
    task_block_loop.addData('task_blockFeed_keyResp.keys',task_blockFeed_keyResp.keys)
    if task_blockFeed_keyResp.keys != None:  # we had a response
        task_block_loop.addData('task_blockFeed_keyResp.rt', task_blockFeed_keyResp.rt)
    # the Routine "task_blockFeed" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'task_block_loop'


# --- Prepare to start Routine "ringBell2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
bellKey_2.keys = []
bellKey_2.rt = []
_bellKey_2_allKeys = []
# keep track of which components have finished
ringBell2Components = [ringBell_text_2, bellKey_2]
for thisComponent in ringBell2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "ringBell2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ringBell_text_2* updates
    if ringBell_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ringBell_text_2.frameNStart = frameN  # exact frame index
        ringBell_text_2.tStart = t  # local t and not account for scr refresh
        ringBell_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ringBell_text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ringBell_text_2.started')
        ringBell_text_2.setAutoDraw(True)
    
    # *bellKey_2* updates
    waitOnFlip = False
    if bellKey_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bellKey_2.frameNStart = frameN  # exact frame index
        bellKey_2.tStart = t  # local t and not account for scr refresh
        bellKey_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bellKey_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'bellKey_2.started')
        bellKey_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(bellKey_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(bellKey_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if bellKey_2.status == STARTED and not waitOnFlip:
        theseKeys = bellKey_2.getKeys(keyList=['c'], waitRelease=False)
        _bellKey_2_allKeys.extend(theseKeys)
        if len(_bellKey_2_allKeys):
            bellKey_2.keys = _bellKey_2_allKeys[-1].name  # just the last key pressed
            bellKey_2.rt = _bellKey_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ringBell2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ringBell2" ---
for thisComponent in ringBell2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if bellKey_2.keys in ['', [], None]:  # No response was made
    bellKey_2.keys = None
thisExp.addData('bellKey_2.keys',bellKey_2.keys)
if bellKey_2.keys != None:  # we had a response
    thisExp.addData('bellKey_2.rt', bellKey_2.rt)
thisExp.nextEntry()
# the Routine "ringBell2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "errorNumbers" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_2
event.clearEvents()
textbox_errorNum.reset()
errorN_key_resp.keys = []
errorN_key_resp.rt = []
_errorN_key_resp_allKeys = []
# keep track of which components have finished
errorNumbersComponents = [errorNum_text, textbox_errorNum, errorN_key_resp]
for thisComponent in errorNumbersComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "errorNumbers" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *errorNum_text* updates
    if errorNum_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        errorNum_text.frameNStart = frameN  # exact frame index
        errorNum_text.tStart = t  # local t and not account for scr refresh
        errorNum_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(errorNum_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'errorNum_text.started')
        errorNum_text.setAutoDraw(True)
    
    # *textbox_errorNum* updates
    if textbox_errorNum.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox_errorNum.frameNStart = frameN  # exact frame index
        textbox_errorNum.tStart = t  # local t and not account for scr refresh
        textbox_errorNum.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox_errorNum, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox_errorNum.started')
        textbox_errorNum.setAutoDraw(True)
    
    # *errorN_key_resp* updates
    waitOnFlip = False
    if errorN_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        errorN_key_resp.frameNStart = frameN  # exact frame index
        errorN_key_resp.tStart = t  # local t and not account for scr refresh
        errorN_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(errorN_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'errorN_key_resp.started')
        errorN_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(errorN_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(errorN_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if errorN_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = errorN_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _errorN_key_resp_allKeys.extend(theseKeys)
        if len(_errorN_key_resp_allKeys):
            errorN_key_resp.keys = _errorN_key_resp_allKeys[-1].name  # just the last key pressed
            errorN_key_resp.rt = _errorN_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in errorNumbersComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "errorNumbers" ---
for thisComponent in errorNumbersComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textbox_errorNum.text',textbox_errorNum.text)
# check responses
if errorN_key_resp.keys in ['', [], None]:  # No response was made
    errorN_key_resp.keys = None
thisExp.addData('errorN_key_resp.keys',errorN_key_resp.keys)
if errorN_key_resp.keys != None:  # we had a response
    thisExp.addData('errorN_key_resp.rt', errorN_key_resp.rt)
thisExp.nextEntry()
# the Routine "errorNumbers" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "errorPercentage" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code
event.clearEvents()
textbox_errorPercent.reset()
errorN_key_resp_2.keys = []
errorN_key_resp_2.rt = []
_errorN_key_resp_2_allKeys = []
# keep track of which components have finished
errorPercentageComponents = [errorPercent_text, textbox_errorPercent, errorN_key_resp_2]
for thisComponent in errorPercentageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "errorPercentage" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *errorPercent_text* updates
    if errorPercent_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        errorPercent_text.frameNStart = frameN  # exact frame index
        errorPercent_text.tStart = t  # local t and not account for scr refresh
        errorPercent_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(errorPercent_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'errorPercent_text.started')
        errorPercent_text.setAutoDraw(True)
    
    # *textbox_errorPercent* updates
    if textbox_errorPercent.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox_errorPercent.frameNStart = frameN  # exact frame index
        textbox_errorPercent.tStart = t  # local t and not account for scr refresh
        textbox_errorPercent.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox_errorPercent, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox_errorPercent.started')
        textbox_errorPercent.setAutoDraw(True)
    
    # *errorN_key_resp_2* updates
    waitOnFlip = False
    if errorN_key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        errorN_key_resp_2.frameNStart = frameN  # exact frame index
        errorN_key_resp_2.tStart = t  # local t and not account for scr refresh
        errorN_key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(errorN_key_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'errorN_key_resp_2.started')
        errorN_key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(errorN_key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(errorN_key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if errorN_key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = errorN_key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _errorN_key_resp_2_allKeys.extend(theseKeys)
        if len(_errorN_key_resp_2_allKeys):
            errorN_key_resp_2.keys = _errorN_key_resp_2_allKeys[-1].name  # just the last key pressed
            errorN_key_resp_2.rt = _errorN_key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in errorPercentageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "errorPercentage" ---
for thisComponent in errorPercentageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textbox_errorPercent.text',textbox_errorPercent.text)
# check responses
if errorN_key_resp_2.keys in ['', [], None]:  # No response was made
    errorN_key_resp_2.keys = None
thisExp.addData('errorN_key_resp_2.keys',errorN_key_resp_2.keys)
if errorN_key_resp_2.keys != None:  # we had a response
    thisExp.addData('errorN_key_resp_2.rt', errorN_key_resp_2.rt)
thisExp.nextEntry()
# the Routine "errorPercentage" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "botherRate" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_3
event.clearEvents()
textbox_botherRate.reset()
botherRate_key_resp.keys = []
botherRate_key_resp.rt = []
_botherRate_key_resp_allKeys = []
# keep track of which components have finished
botherRateComponents = [botherRate_text, textbox_botherRate, botherRate_key_resp]
for thisComponent in botherRateComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "botherRate" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *botherRate_text* updates
    if botherRate_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        botherRate_text.frameNStart = frameN  # exact frame index
        botherRate_text.tStart = t  # local t and not account for scr refresh
        botherRate_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(botherRate_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'botherRate_text.started')
        botherRate_text.setAutoDraw(True)
    
    # *textbox_botherRate* updates
    if textbox_botherRate.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox_botherRate.frameNStart = frameN  # exact frame index
        textbox_botherRate.tStart = t  # local t and not account for scr refresh
        textbox_botherRate.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox_botherRate, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox_botherRate.started')
        textbox_botherRate.setAutoDraw(True)
    
    # *botherRate_key_resp* updates
    waitOnFlip = False
    if botherRate_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        botherRate_key_resp.frameNStart = frameN  # exact frame index
        botherRate_key_resp.tStart = t  # local t and not account for scr refresh
        botherRate_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(botherRate_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'botherRate_key_resp.started')
        botherRate_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(botherRate_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(botherRate_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if botherRate_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = botherRate_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _botherRate_key_resp_allKeys.extend(theseKeys)
        if len(_botherRate_key_resp_allKeys):
            botherRate_key_resp.keys = _botherRate_key_resp_allKeys[-1].name  # just the last key pressed
            botherRate_key_resp.rt = _botherRate_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in botherRateComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "botherRate" ---
for thisComponent in botherRateComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textbox_botherRate.text',textbox_botherRate.text)
# check responses
if botherRate_key_resp.keys in ['', [], None]:  # No response was made
    botherRate_key_resp.keys = None
thisExp.addData('botherRate_key_resp.keys',botherRate_key_resp.keys)
if botherRate_key_resp.keys != None:  # we had a response
    thisExp.addData('botherRate_key_resp.rt', botherRate_key_resp.rt)
thisExp.nextEntry()
# the Routine "botherRate" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "ringBell3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
bellKey_3.keys = []
bellKey_3.rt = []
_bellKey_3_allKeys = []
# keep track of which components have finished
ringBell3Components = [ringBell_text_3, bellKey_3]
for thisComponent in ringBell3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "ringBell3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ringBell_text_3* updates
    if ringBell_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ringBell_text_3.frameNStart = frameN  # exact frame index
        ringBell_text_3.tStart = t  # local t and not account for scr refresh
        ringBell_text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ringBell_text_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ringBell_text_3.started')
        ringBell_text_3.setAutoDraw(True)
    
    # *bellKey_3* updates
    waitOnFlip = False
    if bellKey_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bellKey_3.frameNStart = frameN  # exact frame index
        bellKey_3.tStart = t  # local t and not account for scr refresh
        bellKey_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bellKey_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'bellKey_3.started')
        bellKey_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(bellKey_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(bellKey_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if bellKey_3.status == STARTED and not waitOnFlip:
        theseKeys = bellKey_3.getKeys(keyList=['c'], waitRelease=False)
        _bellKey_3_allKeys.extend(theseKeys)
        if len(_bellKey_3_allKeys):
            bellKey_3.keys = _bellKey_3_allKeys[-1].name  # just the last key pressed
            bellKey_3.rt = _bellKey_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ringBell3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ringBell3" ---
for thisComponent in ringBell3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if bellKey_3.keys in ['', [], None]:  # No response was made
    bellKey_3.keys = None
thisExp.addData('bellKey_3.keys',bellKey_3.keys)
if bellKey_3.keys != None:  # we had a response
    thisExp.addData('bellKey_3.rt', bellKey_3.rt)
thisExp.nextEntry()
# the Routine "ringBell3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "surpriseInstruct" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instruct_surp1_key_resp.keys = []
instruct_surp1_key_resp.rt = []
_instruct_surp1_key_resp_allKeys = []
# keep track of which components have finished
surpriseInstructComponents = [instruct_surprise1, instruct_surp1_key_resp]
for thisComponent in surpriseInstructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "surpriseInstruct" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct_surprise1* updates
    if instruct_surprise1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_surprise1.frameNStart = frameN  # exact frame index
        instruct_surprise1.tStart = t  # local t and not account for scr refresh
        instruct_surprise1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_surprise1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instruct_surprise1.started')
        instruct_surprise1.setAutoDraw(True)
    
    # *instruct_surp1_key_resp* updates
    waitOnFlip = False
    if instruct_surp1_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_surp1_key_resp.frameNStart = frameN  # exact frame index
        instruct_surp1_key_resp.tStart = t  # local t and not account for scr refresh
        instruct_surp1_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_surp1_key_resp, 'tStartRefresh')  # time at next scr refresh
        instruct_surp1_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instruct_surp1_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instruct_surp1_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instruct_surp1_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = instruct_surp1_key_resp.getKeys(keyList=['8'], waitRelease=False)
        _instruct_surp1_key_resp_allKeys.extend(theseKeys)
        if len(_instruct_surp1_key_resp_allKeys):
            instruct_surp1_key_resp.keys = _instruct_surp1_key_resp_allKeys[-1].name  # just the last key pressed
            instruct_surp1_key_resp.rt = _instruct_surp1_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in surpriseInstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "surpriseInstruct" ---
for thisComponent in surpriseInstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instruct_surp1_key_resp.keys in ['', [], None]:  # No response was made
    instruct_surp1_key_resp.keys = None
thisExp.addData('instruct_surp1_key_resp.keys',instruct_surp1_key_resp.keys)
if instruct_surp1_key_resp.keys != None:  # we had a response
    thisExp.addData('instruct_surp1_key_resp.rt', instruct_surp1_key_resp.rt)
thisExp.nextEntry()
# the Routine "surpriseInstruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "surpIns2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
prac_firstSlider_2.reset()
text_7.setText(Left_first_inst)
text_8.setText(Right_first_inst)
# keep track of which components have finished
surpIns2Components = [instruct_surprise1_5, prac_firstSlider_2, text_7, text_8]
for thisComponent in surpIns2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "surpIns2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct_surprise1_5* updates
    if instruct_surprise1_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_surprise1_5.frameNStart = frameN  # exact frame index
        instruct_surprise1_5.tStart = t  # local t and not account for scr refresh
        instruct_surprise1_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_surprise1_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instruct_surprise1_5.started')
        instruct_surprise1_5.setAutoDraw(True)
    
    # *prac_firstSlider_2* updates
    if prac_firstSlider_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_firstSlider_2.frameNStart = frameN  # exact frame index
        prac_firstSlider_2.tStart = t  # local t and not account for scr refresh
        prac_firstSlider_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_firstSlider_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'prac_firstSlider_2.started')
        prac_firstSlider_2.setAutoDraw(True)
    
    # Check prac_firstSlider_2 for response to end routine
    if prac_firstSlider_2.getRating() is not None and prac_firstSlider_2.status == STARTED:
        continueRoutine = False
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_7.started')
        text_7.setAutoDraw(True)
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_8.started')
        text_8.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in surpIns2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "surpIns2" ---
for thisComponent in surpIns2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('prac_firstSlider_2.response', prac_firstSlider_2.getRating())
thisExp.addData('prac_firstSlider_2.rt', prac_firstSlider_2.getRT())
# the Routine "surpIns2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "surpIns2_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
prac_firstSlider_3.reset()
text_9.setText(Left_first_inst)
text_10.setText(Right_first_inst)
# keep track of which components have finished
surpIns2_2Components = [instruct_surprise1_7, prac_firstSlider_3, text_9, text_10]
for thisComponent in surpIns2_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "surpIns2_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct_surprise1_7* updates
    if instruct_surprise1_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_surprise1_7.frameNStart = frameN  # exact frame index
        instruct_surprise1_7.tStart = t  # local t and not account for scr refresh
        instruct_surprise1_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_surprise1_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instruct_surprise1_7.started')
        instruct_surprise1_7.setAutoDraw(True)
    
    # *prac_firstSlider_3* updates
    if prac_firstSlider_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_firstSlider_3.frameNStart = frameN  # exact frame index
        prac_firstSlider_3.tStart = t  # local t and not account for scr refresh
        prac_firstSlider_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_firstSlider_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'prac_firstSlider_3.started')
        prac_firstSlider_3.setAutoDraw(True)
    
    # Check prac_firstSlider_3 for response to end routine
    if prac_firstSlider_3.getRating() is not None and prac_firstSlider_3.status == STARTED:
        continueRoutine = False
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_9.started')
        text_9.setAutoDraw(True)
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_10.started')
        text_10.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in surpIns2_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "surpIns2_2" ---
for thisComponent in surpIns2_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('prac_firstSlider_3.response', prac_firstSlider_3.getRating())
thisExp.addData('prac_firstSlider_3.rt', prac_firstSlider_3.getRT())
# the Routine "surpIns2_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
surprise_block_loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("surpriseBlock_select_"+expInfo['cb']+".xlsx"),
    seed=None, name='surprise_block_loop')
thisExp.addLoop(surprise_block_loop)  # add the loop to the experiment
thisSurprise_block_loop = surprise_block_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSurprise_block_loop.rgb)
if thisSurprise_block_loop != None:
    for paramName in thisSurprise_block_loop:
        exec('{} = thisSurprise_block_loop[paramName]'.format(paramName))

for thisSurprise_block_loop in surprise_block_loop:
    currentLoop = surprise_block_loop
    # abbreviate parameter names if possible (e.g. rgb = thisSurprise_block_loop.rgb)
    if thisSurprise_block_loop != None:
        for paramName in thisSurprise_block_loop:
            exec('{} = thisSurprise_block_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "surp_taskReminders" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from task_blockReminder_code_2
    blockCounterZ1 = blockCounterZ1 +1
    
    if blockCounterZ1 == 1:
        blockNumText = 'Block 1 of 8'
    elif blockCounterZ1 == 2:
        blockNumText = 'Block 2 of 8'
    elif blockCounterZ1 == 3:
        blockNumText = 'Block 3 of 8'
    elif blockCounterZ1 == 4:
        blockNumText = 'Block 4 of 8'
    elif blockCounterZ1 == 5:
        blockNumText = 'Block 5 of 8'
    elif blockCounterZ1 == 6:
        blockNumText = 'Block 6 of 8'
    elif blockCounterZ1 == 7:
        blockNumText = 'Block 7 of 8'
    elif blockCounterZ1 == 8:
        blockNumText = 'Block 8 of 8'
    
        
    task_blockText_2.setText(blockNumText)
    task_blockReminders_keyResp_2.keys = []
    task_blockReminders_keyResp_2.rt = []
    _task_blockReminders_keyResp_2_allKeys = []
    # keep track of which components have finished
    surp_taskRemindersComponents = [task_blockText_2, task_blockReminders_text_2, task_blockReminders_keyResp_2]
    for thisComponent in surp_taskRemindersComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "surp_taskReminders" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *task_blockText_2* updates
        if task_blockText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_blockText_2.frameNStart = frameN  # exact frame index
            task_blockText_2.tStart = t  # local t and not account for scr refresh
            task_blockText_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_blockText_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'task_blockText_2.started')
            task_blockText_2.setAutoDraw(True)
        
        # *task_blockReminders_text_2* updates
        if task_blockReminders_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_blockReminders_text_2.frameNStart = frameN  # exact frame index
            task_blockReminders_text_2.tStart = t  # local t and not account for scr refresh
            task_blockReminders_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_blockReminders_text_2, 'tStartRefresh')  # time at next scr refresh
            task_blockReminders_text_2.setAutoDraw(True)
        
        # *task_blockReminders_keyResp_2* updates
        waitOnFlip = False
        if task_blockReminders_keyResp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_blockReminders_keyResp_2.frameNStart = frameN  # exact frame index
            task_blockReminders_keyResp_2.tStart = t  # local t and not account for scr refresh
            task_blockReminders_keyResp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_blockReminders_keyResp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'task_blockReminders_keyResp_2.started')
            task_blockReminders_keyResp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(task_blockReminders_keyResp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(task_blockReminders_keyResp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if task_blockReminders_keyResp_2.status == STARTED and not waitOnFlip:
            theseKeys = task_blockReminders_keyResp_2.getKeys(keyList=['8'], waitRelease=False)
            _task_blockReminders_keyResp_2_allKeys.extend(theseKeys)
            if len(_task_blockReminders_keyResp_2_allKeys):
                task_blockReminders_keyResp_2.keys = _task_blockReminders_keyResp_2_allKeys[-1].name  # just the last key pressed
                task_blockReminders_keyResp_2.rt = _task_blockReminders_keyResp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in surp_taskRemindersComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "surp_taskReminders" ---
    for thisComponent in surp_taskRemindersComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if task_blockReminders_keyResp_2.keys in ['', [], None]:  # No response was made
        task_blockReminders_keyResp_2.keys = None
    surprise_block_loop.addData('task_blockReminders_keyResp_2.keys',task_blockReminders_keyResp_2.keys)
    if task_blockReminders_keyResp_2.keys != None:  # we had a response
        surprise_block_loop.addData('task_blockReminders_keyResp_2.rt', task_blockReminders_keyResp_2.rt)
    # the Routine "surp_taskReminders" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(whichSurpriseBlock),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        trials_2 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(surp_csv_name),
            seed=None, name='trials_2')
        thisExp.addLoop(trials_2)  # add the loop to the experiment
        thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        for thisTrial_2 in trials_2:
            currentLoop = trials_2
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
            if thisTrial_2 != None:
                for paramName in thisTrial_2:
                    exec('{} = thisTrial_2[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "firstStim_A1" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            first_surpStimuliA1.setImage(surpriseFaces)
            fStimA1.setPos((0, 0.32))
            fStimA1.setText(firstTextA)
            fStimA1.setHeight(0.045)
            # Run 'Begin Routine' code from stimulus_trig_code_3
            #set stimTriggerSent to false at the start of the trial. this way
            #when the stimulus is shown, we can change it to True. This variable
            #is used to ensure we only throw the stimulus EEG trigger once.
            stimulusTriggerSent = False
            firstStim_sliderA1.reset()
            # Run 'Begin Routine' code from response_trigger_code_3
            
            #already within a given trial.
            
            resp_triggerSentQ1 = False
            
            # setup some python lists for storing info about the first_mouseA1
            first_mouseA1.x = []
            first_mouseA1.y = []
            first_mouseA1.leftButton = []
            first_mouseA1.midButton = []
            first_mouseA1.rightButton = []
            first_mouseA1.time = []
            gotValidClick = False  # until a click is received
            # Run 'Begin Routine' code from code_5
            
            first_mouseA1.setPos([0, -0.2])
            text.setText(firstLeft)
            text_2.setText(firstRight)
            # keep track of which components have finished
            firstStim_A1Components = [first_surpStimuliA1, fStimA1, firstStim_sliderA1, first_mouseA1, text, text_2]
            for thisComponent in firstStim_A1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "firstStim_A1" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *first_surpStimuliA1* updates
                if first_surpStimuliA1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    first_surpStimuliA1.frameNStart = frameN  # exact frame index
                    first_surpStimuliA1.tStart = t  # local t and not account for scr refresh
                    first_surpStimuliA1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(first_surpStimuliA1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'first_surpStimuliA1.started')
                    first_surpStimuliA1.setAutoDraw(True)
                
                # *fStimA1* updates
                if fStimA1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fStimA1.frameNStart = frameN  # exact frame index
                    fStimA1.tStart = t  # local t and not account for scr refresh
                    fStimA1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fStimA1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fStimA1.started')
                    fStimA1.setAutoDraw(True)
                # Run 'Each Frame' code from stimulus_trig_code_3
                
                if first_surpStimuliA1.status == STARTED and not stimulusTriggerSent:
                    stimulusTriggerSent = True #switch stimTriggerSent to True so that the stimulus eeg trigger will not be sent again this trial
                    port.write([0x1F]) #hexcode = 31; eeg trigger sent
                    time.sleep(PulseWidth) #how long to wait before clearing trigger port
                    port.write([0x00]) #clear trigger port by sending hexcode = 0
                
                
                # *firstStim_sliderA1* updates
                if firstStim_sliderA1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    firstStim_sliderA1.frameNStart = frameN  # exact frame index
                    firstStim_sliderA1.tStart = t  # local t and not account for scr refresh
                    firstStim_sliderA1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(firstStim_sliderA1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'firstStim_sliderA1.started')
                    firstStim_sliderA1.setAutoDraw(True)
                
                # Check firstStim_sliderA1 for response to end routine
                if firstStim_sliderA1.getRating() is not None and firstStim_sliderA1.status == STARTED:
                    continueRoutine = False
                # Run 'Each Frame' code from response_trigger_code_3
                if firstStim_sliderA1.getRating() is not None and not resp_triggerSentQ1:
                    if firstStim_sliderA1.getRating() == 1:
                        port.write([0x29]) # 41 # to get these converted hexcodes you can use this link https://www.rapidtables.com/convert/number/decimal-to-hex.html
                        time.sleep(PulseWidth)
                        port.write([0x00])
                        resp_triggerSentQ1 = True
                    elif firstStim_sliderA1.getRating() == 2: 
                        port.write([0x2A])# 42
                        time.sleep(PulseWidth)
                        port.write([0x00])
                        resp_triggerSentQ1 = True
                    elif firstStim_sliderA1.getRating() == 3: 
                        port.write([0x2B])# 43
                        time.sleep(PulseWidth)
                        port.write([0x00])
                        resp_triggerSentQ1 = True
                    elif firstStim_sliderA1.getRating() == 4: 
                        port.write([0x2C])# 44
                        time.sleep(PulseWidth)
                        port.write([0x00])
                        resp_triggerSentQ1 = True
                    elif firstStim_sliderA1.getRating() == 5: 
                        port.write([0x2D])# 45
                        time.sleep(PulseWidth)
                        port.write([0x00])
                        resp_triggerSentQ1 = True
                    elif firstStim_sliderA1.getRating() == 6: 
                        port.write([0x2E])# 46
                        time.sleep(PulseWidth)
                        port.write([0x00])
                        resp_triggerSentQ1 = True
                
                # *first_mouseA1* updates
                if first_mouseA1.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    first_mouseA1.frameNStart = frameN  # exact frame index
                    first_mouseA1.tStart = t  # local t and not account for scr refresh
                    first_mouseA1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(first_mouseA1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('first_mouseA1.started', t)
                    first_mouseA1.status = STARTED
                    first_mouseA1.mouseClock.reset()
                    prevButtonState = first_mouseA1.getPressed()  # if button is down already this ISN'T a new click
                if first_mouseA1.status == STARTED:  # only update if started and not finished!
                    buttons = first_mouseA1.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            x, y = first_mouseA1.getPos()
                            first_mouseA1.x.append(x)
                            first_mouseA1.y.append(y)
                            buttons = first_mouseA1.getPressed()
                            first_mouseA1.leftButton.append(buttons[0])
                            first_mouseA1.midButton.append(buttons[1])
                            first_mouseA1.rightButton.append(buttons[2])
                            first_mouseA1.time.append(first_mouseA1.mouseClock.getTime())
                
                # *text* updates
                if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text.frameNStart = frameN  # exact frame index
                    text.tStart = t  # local t and not account for scr refresh
                    text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.started')
                    text.setAutoDraw(True)
                
                # *text_2* updates
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.started')
                    text_2.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in firstStim_A1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "firstStim_A1" ---
            for thisComponent in firstStim_A1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_2.addData('firstStim_sliderA1.response', firstStim_sliderA1.getRating())
            trials_2.addData('firstStim_sliderA1.rt', firstStim_sliderA1.getRT())
            # store data for trials_2 (TrialHandler)
            trials_2.addData('first_mouseA1.x', first_mouseA1.x)
            trials_2.addData('first_mouseA1.y', first_mouseA1.y)
            trials_2.addData('first_mouseA1.leftButton', first_mouseA1.leftButton)
            trials_2.addData('first_mouseA1.midButton', first_mouseA1.midButton)
            trials_2.addData('first_mouseA1.rightButton', first_mouseA1.rightButton)
            trials_2.addData('first_mouseA1.time', first_mouseA1.time)
            # the Routine "firstStim_A1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "fixation2" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_4
            event.clearEvents()
            # make range from a to b in n stepsizes
            ISIRange3 = np.linspace(1000, 1350, 350)
            
            # picking from a shuffled array is easier for random selection in JS
            shuffle(ISIRange3)
            thisISI3 = ISIRange3[0]/1000 # the first item of the shuffled array 
            trials_2.addData('thisISI3', thisISI3)
            # Run 'Begin Routine' code from fixation_trig
            #set stimTriggerSent to false at the start of the trial. this way
            #when the stimulus is shown, we can change it to True. This variable
            #is used to ensure we only throw the stimulus EEG trigger once.
            stimulusTriggerSentQ1 = False
            # keep track of which components have finished
            fixation2Components = [polygon]
            for thisComponent in fixation2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "fixation2" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *polygon* updates
                if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon.frameNStart = frameN  # exact frame index
                    polygon.tStart = t  # local t and not account for scr refresh
                    polygon.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.started')
                    polygon.setAutoDraw(True)
                if polygon.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon.tStartRefresh + thisISI3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon.tStop = t  # not accounting for scr refresh
                        polygon.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon.stopped')
                        polygon.setAutoDraw(False)
                # Run 'Each Frame' code from fixation_trig
                
                if polygon.status == STARTED and not stimulusTriggerSentQ1:
                    stimulusTriggerSentQ1 = True #switch stimTriggerSent to True so that the stimulus eeg trigger will not be sent again this trial
                    port.write([0x3D]) #hexcode = 61; eeg trigger sent
                    time.sleep(PulseWidth) #how long to wait before clearing trigger port
                    port.write([0x00]) #clear trigger port by sending hexcode = 0
                
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fixation2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "fixation2" ---
            for thisComponent in fixation2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "fixation2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials_2'
        
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'surprise_block_loop'


# --- Prepare to start Routine "ringBell4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
bellKey_4.keys = []
bellKey_4.rt = []
_bellKey_4_allKeys = []
# keep track of which components have finished
ringBell4Components = [ringBell_text_4, bellKey_4]
for thisComponent in ringBell4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "ringBell4" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ringBell_text_4* updates
    if ringBell_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ringBell_text_4.frameNStart = frameN  # exact frame index
        ringBell_text_4.tStart = t  # local t and not account for scr refresh
        ringBell_text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ringBell_text_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ringBell_text_4.started')
        ringBell_text_4.setAutoDraw(True)
    
    # *bellKey_4* updates
    waitOnFlip = False
    if bellKey_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bellKey_4.frameNStart = frameN  # exact frame index
        bellKey_4.tStart = t  # local t and not account for scr refresh
        bellKey_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bellKey_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'bellKey_4.started')
        bellKey_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(bellKey_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(bellKey_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if bellKey_4.status == STARTED and not waitOnFlip:
        theseKeys = bellKey_4.getKeys(keyList=['c'], waitRelease=False)
        _bellKey_4_allKeys.extend(theseKeys)
        if len(_bellKey_4_allKeys):
            bellKey_4.keys = _bellKey_4_allKeys[-1].name  # just the last key pressed
            bellKey_4.rt = _bellKey_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ringBell4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ringBell4" ---
for thisComponent in ringBell4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if bellKey_4.keys in ['', [], None]:  # No response was made
    bellKey_4.keys = None
thisExp.addData('bellKey_4.keys',bellKey_4.keys)
if bellKey_4.keys != None:  # we had a response
    thisExp.addData('bellKey_4.rt', bellKey_4.rt)
thisExp.nextEntry()
# the Routine "ringBell4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "finishMessage" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
finishMessageComponents = [finishMessage_text]
for thisComponent in finishMessageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "finishMessage" ---
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finishMessage_text* updates
    if finishMessage_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finishMessage_text.frameNStart = frameN  # exact frame index
        finishMessage_text.tStart = t  # local t and not account for scr refresh
        finishMessage_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finishMessage_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'finishMessage_text.started')
        finishMessage_text.setAutoDraw(True)
    if finishMessage_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finishMessage_text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            finishMessage_text.tStop = t  # not accounting for scr refresh
            finishMessage_text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'finishMessage_text.stopped')
            finishMessage_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishMessageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "finishMessage" ---
for thisComponent in finishMessageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)
# Run 'End Experiment' code from setup_code
win.mouseVisible = True #make the mouse cursor visable again
port.write([0xFF]) #set port values back to default state (FF)
time.sleep(PulseWidth) #wait PulseWidth amount of time before doing anything else
port.close() #close port opened at start of exp

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
