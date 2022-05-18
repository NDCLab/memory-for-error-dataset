#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Wed May 11 10:19:14 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'flanker-basic_v2'  # from the Builder filename that created this script
expInfo = {'id': ''}
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
    originPath='/Users/khoss005/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Projects/Psychopy/mfeFlanker/faceFlanker_with_background_and_arrows_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='0.5000, 0.5000, 0.5000', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "JS_code"
JS_codeClock = core.Clock()

# Initialize components for Routine "setup"
setupClock = core.Clock()

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='Face Game\n\nWelcome to the face game. In this game, faces will be quickly flashed on the screen. Your goal is to respond to the direction of the MIDDLE face, and to respond as quickly as you can without making mistakes. \n\nIf the MIDDLE face is pointing to the right, use your right hand to press the right button. If the MIDDLE face is pointing to the left, use your left hand to press the left button. \n\nPress the right button to continue\n',
    font='Arial',
    units='height', pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
welcome_keyResp = keyboard.Keyboard()

# Initialize components for Routine "instructRight"
instructRightClock = core.Clock()
instructRight_text = visual.TextStim(win=win, name='instructRight_text',
    text='Below, the MIDDLE face is pointing to the right, so you would respond by pressing the right button with your right hand.\n\nPress the right button to continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructRight_centerImg = visual.ImageStim(
    win=win,
    name='instructRight_centerImg', 
    image='img/renders/face000_45.png', mask=None,
    ori=0, pos=(0, -.3), size=(.18, .18),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
instructRight_rightImg1 = visual.ImageStim(
    win=win,
    name='instructRight_rightImg1', 
    image='img/renders/face000_45.png', mask=None,
    ori=0, pos=(.13, -.3), size=(.18, .18),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
instructRight_leftImg1 = visual.ImageStim(
    win=win,
    name='instructRight_leftImg1', 
    image='img/renders/face000_45.png', mask=None,
    ori=0, pos=(-.13, -.3), size=(.18, .18),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
insructRight_keyResp = keyboard.Keyboard()

# Initialize components for Routine "instructLeft"
instructLeftClock = core.Clock()
instructLeft_text = visual.TextStim(win=win, name='instructLeft_text',
    text='Below, the MIDDLE face is pointing to the left, so you would respond by pressing the left button with your left hand.\n\nPress the left button to continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructLeft_centerImg = visual.ImageStim(
    win=win,
    name='instructLeft_centerImg', 
    image='img/renders/face000_-45.png', mask=None,
    ori=0, pos=(0, -.3), size=(.18, .18),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
instructLeft_rightImg1 = visual.ImageStim(
    win=win,
    name='instructLeft_rightImg1', 
    image='img/renders/face000_-45.png', mask=None,
    ori=0, pos=(.13, -.3), size=(.18, .18),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
instructLeft_leftImg1 = visual.ImageStim(
    win=win,
    name='instructLeft_leftImg1', 
    image='img/renders/face000_-45.png', mask=None,
    ori=0, pos=(-.13, -.3), size=(.18, .18),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
instructLeft_keyResp = keyboard.Keyboard()

# Initialize components for Routine "instructInconRight"
instructInconRightClock = core.Clock()
instructInconRight_text = visual.TextStim(win=win, name='instructInconRight_text',
    text='Sometimes the MIDDLE face will point in a different direction from the other faces. However, your goal is to always respond based on the direction of the MIDDLE face.\n\nBelow, the MIDDLE face is pointing to the right, so you would respond by pressing the right button with your right hand.\n\nPress the right button to continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructIncon_centerImg = visual.ImageStim(
    win=win,
    name='instructIncon_centerImg', 
    image='img/renders/face000_45.png', mask=None,
    ori=0, pos=(0.058, -.3), size=(.18, .18),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
instructIncon_rightImg1 = visual.ImageStim(
    win=win,
    name='instructIncon_rightImg1', 
    image='img/renders/face000_-45.png', mask=None,
    ori=0, pos=(.14, -.3), size=(.18, .18),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
instructIncon_leftImg1 = visual.ImageStim(
    win=win,
    name='instructIncon_leftImg1', 
    image='img/renders/face000_-45.png', mask=None,
    ori=0, pos=(-.13, -.3), size=(.18, .18),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
insructInconRight_keyResp = keyboard.Keyboard()

# Initialize components for Routine "instructInconLeft"
instructInconLeftClock = core.Clock()
instructInconLeft_text = visual.TextStim(win=win, name='instructInconLeft_text',
    text='Below, the MIDDLE face is pointing to the left, so you would respond by pressing the left button with your left hand.\n\nPress the left button to continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructInconLeft_centerImg = visual.ImageStim(
    win=win,
    name='instructInconLeft_centerImg', 
    image='img/renders/face000_-45.png', mask=None,
    ori=0, pos=(-0.058, -.3), size=(.18, .18),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
instructInconLeft_rightImg1 = visual.ImageStim(
    win=win,
    name='instructInconLeft_rightImg1', 
    image='img/renders/face000_45.png', mask=None,
    ori=0, pos=(.13, -.3), size=(.18, .18),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
instructInconLeft_leftImg1 = visual.ImageStim(
    win=win,
    name='instructInconLeft_leftImg1', 
    image='img/renders/face000_45.png', mask=None,
    ori=0, pos=(-.13, -.3), size=(.18, .18),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
instructInconLeft_keyResp = keyboard.Keyboard()

# Initialize components for Routine "prac_blockReminders"
prac_blockRemindersClock = core.Clock()
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
    text='You will now practice responding to the faces. Remember to always respond to the direction of the MIDDLE face.\n\nRespond as quickly as you can without making mistakes.\n\nTo get ready, rest your right and left index fingers on the right and left buttons, then press the right button when you are ready to begin.\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
prac_reminder_keyResp = keyboard.Keyboard()

# Initialize components for Routine "initFixation"
initFixationClock = core.Clock()
initFixation_img = visual.ImageStim(
    win=win,
    name='initFixation_img', 
    image='sin', mask=None,
    ori=0, pos=(0, -.05), size=(.015, .015),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "prac_stimRoutine"
prac_stimRoutineClock = core.Clock()
#initialize the thisISI variable
thisISI = 0
prac_centerImg = visual.ImageStim(
    win=win,
    name='prac_centerImg', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(.18, .18),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
prac_rightImg1 = visual.ImageStim(
    win=win,
    name='prac_rightImg1', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(.18, .18),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
prac_leftImg1 = visual.ImageStim(
    win=win,
    name='prac_leftImg1', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(.18, .18),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
prac_fixImg = visual.ImageStim(
    win=win,
    name='prac_fixImg', 
    image='sin', mask=None,
    ori=0, pos=(0, -.05), size=(.015, .015),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
prac_stim_keyResp = keyboard.Keyboard()

# Initialize components for Routine "prac_blockFeed"
prac_blockFeedClock = core.Clock()
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

# Initialize components for Routine "counterbalance1"
counterbalance1Clock = core.Clock()
cb_text1 = visual.TextStim(win=win, name='cb_text1',
    text='Please select the order at which you want to perform this experiment.\n\nTo perform the arrow flanker first, press the right key, but If you want to do the face flanker first, press the left key.\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_counterbalance1 = keyboard.Keyboard()

# Initialize components for Routine "firstTask_instruct"
firstTask_instructClock = core.Clock()
#initialize the following variables at the start of experiment
blockCounter = 0

#note that we do not need to initialize the accuracy and numCorr vars here
#because they were already initialilzed in the code snippet of the practice loop
firstT_text1 = visual.TextStim(win=win, name='firstT_text1',
    text='',
    font='Arial',
    pos=(0, .3), height=0.06, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
firstT_text2 = visual.TextStim(win=win, name='firstT_text2',
    text='Remember to always respond to the direction of the MIDDLE image.\n\nRespond as quickly as you can without making mistakes.\n\nTo get ready, rest your right and left index fingers on the right and left buttons, then press the right button when you are ready to begin.\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
firstT_key = keyboard.Keyboard()

# Initialize components for Routine "initFixation"
initFixationClock = core.Clock()
initFixation_img = visual.ImageStim(
    win=win,
    name='initFixation_img', 
    image='sin', mask=None,
    ori=0, pos=(0, -.05), size=(.015, .015),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "firstT"
firstTClock = core.Clock()
#no need to initialize thisISI, as already done in practice code snippit
bigFace_2 = visual.ImageStim(
    win=win,
    name='bigFace_2', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
cover_background = visual.ImageStim(
    win=win,
    name='cover_background', 
    image='img/cover_background.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.65, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
task_centerImg_3 = visual.ImageStim(
    win=win,
    name='task_centerImg_3', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
task_rightImg1_3 = visual.ImageStim(
    win=win,
    name='task_rightImg1_3', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
task_leftImg1_3 = visual.ImageStim(
    win=win,
    name='task_leftImg1_3', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
task_fixImg_3 = visual.ImageStim(
    win=win,
    name='task_fixImg_3', 
    image='sin', mask=None,
    ori=0, pos=(0, -.05), size=(.015, .015),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)
first_task_stim_keyResp = keyboard.Keyboard()

# Initialize components for Routine "firstT_feed"
firstT_feedClock = core.Clock()
fTfeed_text1_1 = visual.TextStim(win=win, name='fTfeed_text1_1',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.12, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
fTFeed_text2_1 = visual.TextStim(win=win, name='fTFeed_text2_1',
    text='',
    font='Arial',
    pos=(0, -0.3), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
fTfeed_key_1 = keyboard.Keyboard()

# Initialize components for Routine "firstTask_instruct"
firstTask_instructClock = core.Clock()
#initialize the following variables at the start of experiment
blockCounter = 0

#note that we do not need to initialize the accuracy and numCorr vars here
#because they were already initialilzed in the code snippet of the practice loop
firstT_text1 = visual.TextStim(win=win, name='firstT_text1',
    text='',
    font='Arial',
    pos=(0, .3), height=0.06, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
firstT_text2 = visual.TextStim(win=win, name='firstT_text2',
    text='Remember to always respond to the direction of the MIDDLE image.\n\nRespond as quickly as you can without making mistakes.\n\nTo get ready, rest your right and left index fingers on the right and left buttons, then press the right button when you are ready to begin.\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
firstT_key = keyboard.Keyboard()

# Initialize components for Routine "initFixation"
initFixationClock = core.Clock()
initFixation_img = visual.ImageStim(
    win=win,
    name='initFixation_img', 
    image='sin', mask=None,
    ori=0, pos=(0, -.05), size=(.015, .015),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "secondT"
secondTClock = core.Clock()
#no need to initialize thisISI, as already done in practice code snippit
bigFace = visual.ImageStim(
    win=win,
    name='bigFace', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
cover_background_2 = visual.ImageStim(
    win=win,
    name='cover_background_2', 
    image='img/cover_background.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.65, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
task_centerImg_2 = visual.ImageStim(
    win=win,
    name='task_centerImg_2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
task_rightImg1_2 = visual.ImageStim(
    win=win,
    name='task_rightImg1_2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
task_leftImg1_2 = visual.ImageStim(
    win=win,
    name='task_leftImg1_2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
task_fixImg_2 = visual.ImageStim(
    win=win,
    name='task_fixImg_2', 
    image='sin', mask=None,
    ori=0, pos=(0, -.05), size=(.015, .015),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)
second_task_stim_keyResp = keyboard.Keyboard()

# Initialize components for Routine "secondT_feed"
secondT_feedClock = core.Clock()
sTfeed_text1 = visual.TextStim(win=win, name='sTfeed_text1',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.12, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
scFeed_text2 = visual.TextStim(win=win, name='scFeed_text2',
    text='',
    font='Arial',
    pos=(0, -0.3), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
sTfeed_key = keyboard.Keyboard()

# Initialize components for Routine "surpriseInstruct"
surpriseInstructClock = core.Clock()
instruct_surprise1 = visual.TextStim(win=win, name='instruct_surprise1',
    text='You will now begin a game in which you will be asked if the displayed face on the screen looks OLD or NEW to you.  \n\n\nFor example, if you think that you have seen a displayed face in the previous game, please select OLD as your response.\n\nPress right key to proceed.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instruct_surp1_key_resp = keyboard.Keyboard()

# Initialize components for Routine "counterbalance2"
counterbalance2Clock = core.Clock()
cb_text1_2 = visual.TextStim(win=win, name='cb_text1_2',
    text='Do not Proceed!\nPlease let the experimenter choose the way you need to play the upcoming game.\n\n\nFor the experimenter:\nPress the right key, the game in which the OLD faces correspond to the right key be the first.\n\nPress the left key, the game in which the OLD faces correspond to the left key be the first.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_counterbalance1_2 = keyboard.Keyboard()

# Initialize components for Routine "instructSurpriseTask2"
instructSurpriseTask2Clock = core.Clock()
instructMainTask_text = visual.TextStim(win=win, name='instructMainTask_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructMainTask_keyResp = keyboard.Keyboard()

# Initialize components for Routine "surpriseTask"
surpriseTaskClock = core.Clock()
stimulus = visual.ImageStim(
    win=win,
    name='stimulus', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.2), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
instructsurpA1_right = visual.TextStim(win=win, name='instructsurpA1_right',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructsurpA2_left = visual.TextStim(win=win, name='instructsurpA2_left',
    text='',
    font='Open Sans',
    pos=(-0.4, -0.03), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
surprise_key_resp = keyboard.Keyboard()

# Initialize components for Routine "instructSurpriseTask2_2"
instructSurpriseTask2_2Clock = core.Clock()
instructMainTask_text_2 = visual.TextStim(win=win, name='instructMainTask_text_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructMainTask_keyResp_2 = keyboard.Keyboard()

# Initialize components for Routine "surpriseTask_2"
surpriseTask_2Clock = core.Clock()
stimulus_2 = visual.ImageStim(
    win=win,
    name='stimulus_2', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.2), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
instructsurpA1_right_2 = visual.TextStim(win=win, name='instructsurpA1_right_2',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructsurpA2_left_2 = visual.TextStim(win=win, name='instructsurpA2_left_2',
    text='',
    font='Open Sans',
    pos=(-0.4, -0.03), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
surprise_key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "finishMessage"
finishMessageClock = core.Clock()
finishMessage_text = visual.TextStim(win=win, name='finishMessage_text',
    text='Thank you for your participation!',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "JS_code"-------
continueRoutine = True
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
JS_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "JS_code"-------
while continueRoutine:
    # get current time
    t = JS_codeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=JS_codeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in JS_codeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "JS_code"-------
for thisComponent in JS_codeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "JS_code" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "setup"-------
continueRoutine = True
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
setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
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
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
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
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructRight"-------
continueRoutine = True
# update component parameters for each repeat
insructRight_keyResp.keys = []
insructRight_keyResp.rt = []
_insructRight_keyResp_allKeys = []
# keep track of which components have finished
instructRightComponents = [instructRight_text, instructRight_centerImg, instructRight_rightImg1, instructRight_leftImg1, insructRight_keyResp]
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
instructRightClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructRight"-------
while continueRoutine:
    # get current time
    t = instructRightClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructRightClock)
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
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructRightComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructRight"-------
for thisComponent in instructRightComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructRight" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructLeft"-------
continueRoutine = True
# update component parameters for each repeat
instructLeft_keyResp.keys = []
instructLeft_keyResp.rt = []
_instructLeft_keyResp_allKeys = []
# keep track of which components have finished
instructLeftComponents = [instructLeft_text, instructLeft_centerImg, instructLeft_rightImg1, instructLeft_leftImg1, instructLeft_keyResp]
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
instructLeftClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructLeft"-------
while continueRoutine:
    # get current time
    t = instructLeftClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructLeftClock)
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
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructLeftComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructLeft"-------
for thisComponent in instructLeftComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructLeft" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructInconRight"-------
continueRoutine = True
# update component parameters for each repeat
insructInconRight_keyResp.keys = []
insructInconRight_keyResp.rt = []
_insructInconRight_keyResp_allKeys = []
# keep track of which components have finished
instructInconRightComponents = [instructInconRight_text, instructIncon_centerImg, instructIncon_rightImg1, instructIncon_leftImg1, insructInconRight_keyResp]
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
instructInconRightClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructInconRight"-------
while continueRoutine:
    # get current time
    t = instructInconRightClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructInconRightClock)
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
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructInconRightComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructInconRight"-------
for thisComponent in instructInconRightComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructInconRight" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructInconLeft"-------
continueRoutine = True
# update component parameters for each repeat
instructInconLeft_keyResp.keys = []
instructInconLeft_keyResp.rt = []
_instructInconLeft_keyResp_allKeys = []
# keep track of which components have finished
instructInconLeftComponents = [instructInconLeft_text, instructInconLeft_centerImg, instructInconLeft_rightImg1, instructInconLeft_leftImg1, instructInconLeft_keyResp]
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
instructInconLeftClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructInconLeft"-------
while continueRoutine:
    # get current time
    t = instructInconLeftClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructInconLeftClock)
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
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructInconLeftComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructInconLeft"-------
for thisComponent in instructInconLeftComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructInconLeft" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac_block_loop = data.TrialHandler(nReps=999, method='random', 
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
    
    # ------Prepare to start Routine "prac_blockReminders"-------
    continueRoutine = True
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
    prac_blockRemindersClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "prac_blockReminders"-------
    while continueRoutine:
        # get current time
        t = prac_blockRemindersClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=prac_blockRemindersClock)
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
            prac_blockText.setAutoDraw(True)
        
        # *prac_reminder_text* updates
        if prac_reminder_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_reminder_text.frameNStart = frameN  # exact frame index
            prac_reminder_text.tStart = t  # local t and not account for scr refresh
            prac_reminder_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_reminder_text, 'tStartRefresh')  # time at next scr refresh
            prac_reminder_text.setAutoDraw(True)
        
        # *prac_reminder_keyResp* updates
        waitOnFlip = False
        if prac_reminder_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_reminder_keyResp.frameNStart = frameN  # exact frame index
            prac_reminder_keyResp.tStart = t  # local t and not account for scr refresh
            prac_reminder_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_reminder_keyResp, 'tStartRefresh')  # time at next scr refresh
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
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_blockRemindersComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prac_blockReminders"-------
    for thisComponent in prac_blockRemindersComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac_block_loop.addData('prac_blockText.started', prac_blockText.tStartRefresh)
    prac_block_loop.addData('prac_blockText.stopped', prac_blockText.tStopRefresh)
    prac_block_loop.addData('prac_reminder_text.started', prac_reminder_text.tStartRefresh)
    prac_block_loop.addData('prac_reminder_text.stopped', prac_reminder_text.tStopRefresh)
    # check responses
    if prac_reminder_keyResp.keys in ['', [], None]:  # No response was made
        prac_reminder_keyResp.keys = None
    prac_block_loop.addData('prac_reminder_keyResp.keys',prac_reminder_keyResp.keys)
    if prac_reminder_keyResp.keys != None:  # we had a response
        prac_block_loop.addData('prac_reminder_keyResp.rt', prac_reminder_keyResp.rt)
    prac_block_loop.addData('prac_reminder_keyResp.started', prac_reminder_keyResp.tStartRefresh)
    prac_block_loop.addData('prac_reminder_keyResp.stopped', prac_reminder_keyResp.tStopRefresh)
    # the Routine "prac_blockReminders" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "initFixation"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    initFixation_img.setImage('img/fixationCross.png')
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
    initFixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "initFixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = initFixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=initFixationClock)
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
            initFixation_img.setAutoDraw(True)
        if initFixation_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > initFixation_img.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                initFixation_img.tStop = t  # not accounting for scr refresh
                initFixation_img.frameNStop = frameN  # exact frame index
                win.timeOnFlip(initFixation_img, 'tStopRefresh')  # time at next scr refresh
                initFixation_img.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in initFixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "initFixation"-------
    for thisComponent in initFixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac_block_loop.addData('initFixation_img.started', initFixation_img.tStartRefresh)
    prac_block_loop.addData('initFixation_img.stopped', initFixation_img.tStopRefresh)
    
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
        
        # ------Prepare to start Routine "prac_stimRoutine"-------
        continueRoutine = True
        # update component parameters for each repeat
        # pick the ISI for the next routine
        # this code component is set to 'both' because we need to remove the 'np'
        # at the start of np.linspace (this is a python library JS won't know what to call. 
        
        # make range from a to b in n stepsizes
        ISIRange = np.linspace(1500, 2000, 500)
        
        # picking from a shuffled array is easier for random selection in JS
        shuffle(ISIRange)
        thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
        
        # save this ISI to our output file
        prac_trial_loop.addData('ISI', thisISI)
        
        
        # show in console for debugging
        #print('thisISI: ', thisISI)
        prac_centerImg.setPos(locationC)
        prac_centerImg.setImage(middleStim)
        prac_rightImg1.setPos(locationR)
        prac_rightImg1.setImage(rightStim)
        prac_leftImg1.setPos(locationL)
        prac_leftImg1.setImage(leftStim)
        prac_fixImg.setImage('img/fixationCross.png')
        prac_stim_keyResp.keys = []
        prac_stim_keyResp.rt = []
        _prac_stim_keyResp_allKeys = []
        # keep track of which components have finished
        prac_stimRoutineComponents = [prac_centerImg, prac_rightImg1, prac_leftImg1, prac_fixImg, prac_stim_keyResp]
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
        prac_stimRoutineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "prac_stimRoutine"-------
        while continueRoutine:
            # get current time
            t = prac_stimRoutineClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=prac_stimRoutineClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *prac_centerImg* updates
            if prac_centerImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_centerImg.frameNStart = frameN  # exact frame index
                prac_centerImg.tStart = t  # local t and not account for scr refresh
                prac_centerImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_centerImg, 'tStartRefresh')  # time at next scr refresh
                prac_centerImg.setAutoDraw(True)
            if prac_centerImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_centerImg.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_centerImg.tStop = t  # not accounting for scr refresh
                    prac_centerImg.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(prac_centerImg, 'tStopRefresh')  # time at next scr refresh
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
                if tThisFlipGlobal > prac_rightImg1.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_rightImg1.tStop = t  # not accounting for scr refresh
                    prac_rightImg1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(prac_rightImg1, 'tStopRefresh')  # time at next scr refresh
                    prac_rightImg1.setAutoDraw(False)
            
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
                if tThisFlipGlobal > prac_leftImg1.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_leftImg1.tStop = t  # not accounting for scr refresh
                    prac_leftImg1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(prac_leftImg1, 'tStopRefresh')  # time at next scr refresh
                    prac_leftImg1.setAutoDraw(False)
            
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
                    win.timeOnFlip(prac_fixImg, 'tStopRefresh')  # time at next scr refresh
                    prac_fixImg.setAutoDraw(False)
            
            # *prac_stim_keyResp* updates
            waitOnFlip = False
            if prac_stim_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_stim_keyResp.frameNStart = frameN  # exact frame index
                prac_stim_keyResp.tStart = t  # local t and not account for scr refresh
                prac_stim_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_stim_keyResp, 'tStartRefresh')  # time at next scr refresh
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
                    win.timeOnFlip(prac_stim_keyResp, 'tStopRefresh')  # time at next scr refresh
                    prac_stim_keyResp.status = FINISHED
            if prac_stim_keyResp.status == STARTED and not waitOnFlip:
                theseKeys = prac_stim_keyResp.getKeys(keyList=['1', '8'], waitRelease=False)
                _prac_stim_keyResp_allKeys.extend(theseKeys)
                if len(_prac_stim_keyResp_allKeys):
                    prac_stim_keyResp.keys = [key.name for key in _prac_stim_keyResp_allKeys]  # storing all keys
                    prac_stim_keyResp.rt = [key.rt for key in _prac_stim_keyResp_allKeys]
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prac_stimRoutineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "prac_stimRoutine"-------
        for thisComponent in prac_stimRoutineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        prac_trial_loop.addData('prac_centerImg.started', prac_centerImg.tStartRefresh)
        prac_trial_loop.addData('prac_centerImg.stopped', prac_centerImg.tStopRefresh)
        # check responses
        if prac_stim_keyResp.keys in ['', [], None]:  # No response was made
            prac_stim_keyResp.keys = None
        prac_trial_loop.addData('prac_stim_keyResp.keys',prac_stim_keyResp.keys)
        if prac_stim_keyResp.keys != None:  # we had a response
            prac_trial_loop.addData('prac_stim_keyResp.rt', prac_stim_keyResp.rt)
        prac_trial_loop.addData('prac_stim_keyResp.started', prac_stim_keyResp.tStartRefresh)
        prac_trial_loop.addData('prac_stim_keyResp.stopped', prac_stim_keyResp.tStopRefresh)
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
    
    
    # ------Prepare to start Routine "prac_blockFeed"-------
    continueRoutine = True
    # update component parameters for each repeat
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
    prac_blockFeedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "prac_blockFeed"-------
    while continueRoutine:
        # get current time
        t = prac_blockFeedClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=prac_blockFeedClock)
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
            prac_blockFeed_text.setAutoDraw(True)
        
        # *prac_pressContinue* updates
        if prac_pressContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_pressContinue.frameNStart = frameN  # exact frame index
            prac_pressContinue.tStart = t  # local t and not account for scr refresh
            prac_pressContinue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_pressContinue, 'tStartRefresh')  # time at next scr refresh
            prac_pressContinue.setAutoDraw(True)
        
        # *prac_blockFeed_keyResp* updates
        waitOnFlip = False
        if prac_blockFeed_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_blockFeed_keyResp.frameNStart = frameN  # exact frame index
            prac_blockFeed_keyResp.tStart = t  # local t and not account for scr refresh
            prac_blockFeed_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_blockFeed_keyResp, 'tStartRefresh')  # time at next scr refresh
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
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_blockFeedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prac_blockFeed"-------
    for thisComponent in prac_blockFeedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac_block_loop.addData('prac_blockFeed_text.started', prac_blockFeed_text.tStartRefresh)
    prac_block_loop.addData('prac_blockFeed_text.stopped', prac_blockFeed_text.tStopRefresh)
    prac_block_loop.addData('prac_pressContinue.started', prac_pressContinue.tStartRefresh)
    prac_block_loop.addData('prac_pressContinue.stopped', prac_pressContinue.tStopRefresh)
    # check responses
    if prac_blockFeed_keyResp.keys in ['', [], None]:  # No response was made
        prac_blockFeed_keyResp.keys = None
    prac_block_loop.addData('prac_blockFeed_keyResp.keys',prac_blockFeed_keyResp.keys)
    if prac_blockFeed_keyResp.keys != None:  # we had a response
        prac_block_loop.addData('prac_blockFeed_keyResp.rt', prac_blockFeed_keyResp.rt)
    prac_block_loop.addData('prac_blockFeed_keyResp.started', prac_blockFeed_keyResp.tStartRefresh)
    prac_block_loop.addData('prac_blockFeed_keyResp.stopped', prac_blockFeed_keyResp.tStopRefresh)
    # the Routine "prac_blockFeed" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 999 repeats of 'prac_block_loop'


# ------Prepare to start Routine "counterbalance1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_counterbalance1.keys = []
key_resp_counterbalance1.rt = []
_key_resp_counterbalance1_allKeys = []
# keep track of which components have finished
counterbalance1Components = [cb_text1, key_resp_counterbalance1]
for thisComponent in counterbalance1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
counterbalance1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "counterbalance1"-------
while continueRoutine:
    # get current time
    t = counterbalance1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=counterbalance1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *cb_text1* updates
    if cb_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cb_text1.frameNStart = frameN  # exact frame index
        cb_text1.tStart = t  # local t and not account for scr refresh
        cb_text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cb_text1, 'tStartRefresh')  # time at next scr refresh
        cb_text1.setAutoDraw(True)
    
    # *key_resp_counterbalance1* updates
    waitOnFlip = False
    if key_resp_counterbalance1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_counterbalance1.frameNStart = frameN  # exact frame index
        key_resp_counterbalance1.tStart = t  # local t and not account for scr refresh
        key_resp_counterbalance1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_counterbalance1, 'tStartRefresh')  # time at next scr refresh
        key_resp_counterbalance1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_counterbalance1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_counterbalance1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_counterbalance1.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_counterbalance1.getKeys(keyList=['1', '8'], waitRelease=False)
        _key_resp_counterbalance1_allKeys.extend(theseKeys)
        if len(_key_resp_counterbalance1_allKeys):
            key_resp_counterbalance1.keys = _key_resp_counterbalance1_allKeys[-1].name  # just the last key pressed
            key_resp_counterbalance1.rt = _key_resp_counterbalance1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in counterbalance1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "counterbalance1"-------
for thisComponent in counterbalance1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_counterbalance1.keys in ['', [], None]:  # No response was made
    key_resp_counterbalance1.keys = None
thisExp.addData('key_resp_counterbalance1.keys',key_resp_counterbalance1.keys)
if key_resp_counterbalance1.keys != None:  # we had a response
    thisExp.addData('key_resp_counterbalance1.rt', key_resp_counterbalance1.rt)
thisExp.addData('key_resp_counterbalance1.started', key_resp_counterbalance1.tStartRefresh)
thisExp.addData('key_resp_counterbalance1.stopped', key_resp_counterbalance1.tStopRefresh)
thisExp.nextEntry()
if key_resp_counterbalance1.keys[-1] == '8': # Running the arrow flanker task was chosen to be done first.
     firstLoop = 'alt_arrow_blockSelect.xlsx'
     secondLoop = 'alt_face_blockSelect.xlsx'
elif key_resp_counterbalance1.keys[-1] == '1': # Running the face flanker task was chosen to be done first.
     firstLoop = 'alt_face_blockSelect.xlsx'
     secondLoop = 'alt_arrow_blockSelect.xlsx'



# the Routine "counterbalance1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
first_block_loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(firstLoop),
    seed=None, name='first_block_loop')
thisExp.addLoop(first_block_loop)  # add the loop to the experiment
thisFirst_block_loop = first_block_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFirst_block_loop.rgb)
if thisFirst_block_loop != None:
    for paramName in thisFirst_block_loop:
        exec('{} = thisFirst_block_loop[paramName]'.format(paramName))

for thisFirst_block_loop in first_block_loop:
    currentLoop = first_block_loop
    # abbreviate parameter names if possible (e.g. rgb = thisFirst_block_loop.rgb)
    if thisFirst_block_loop != None:
        for paramName in thisFirst_block_loop:
            exec('{} = thisFirst_block_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "firstTask_instruct"-------
    continueRoutine = True
    # update component parameters for each repeat
    blockCounter = blockCounter +1
    
    if blockCounter == 1:
        blockNumText = 'Block 1 of 6'
    elif blockCounter == 2:
        blockNumText = 'Block 2 of 6'
    elif blockCounter == 3:
        blockNumText = 'Block 3 of 6'
    elif blockCounter == 4:
        blockNumText = 'Block 4 of 6'
    elif blockCounter == 5:
        blockNumText = 'Block 5 of 6'
    elif blockCounter == 6:
        blockNumText = 'Block 6 of 6'
    
    firstT_text1.setText(blockNumText)
    firstT_key.keys = []
    firstT_key.rt = []
    _firstT_key_allKeys = []
    # keep track of which components have finished
    firstTask_instructComponents = [firstT_text1, firstT_text2, firstT_key]
    for thisComponent in firstTask_instructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    firstTask_instructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "firstTask_instruct"-------
    while continueRoutine:
        # get current time
        t = firstTask_instructClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=firstTask_instructClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *firstT_text1* updates
        if firstT_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            firstT_text1.frameNStart = frameN  # exact frame index
            firstT_text1.tStart = t  # local t and not account for scr refresh
            firstT_text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(firstT_text1, 'tStartRefresh')  # time at next scr refresh
            firstT_text1.setAutoDraw(True)
        
        # *firstT_text2* updates
        if firstT_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            firstT_text2.frameNStart = frameN  # exact frame index
            firstT_text2.tStart = t  # local t and not account for scr refresh
            firstT_text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(firstT_text2, 'tStartRefresh')  # time at next scr refresh
            firstT_text2.setAutoDraw(True)
        
        # *firstT_key* updates
        waitOnFlip = False
        if firstT_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            firstT_key.frameNStart = frameN  # exact frame index
            firstT_key.tStart = t  # local t and not account for scr refresh
            firstT_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(firstT_key, 'tStartRefresh')  # time at next scr refresh
            firstT_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(firstT_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(firstT_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if firstT_key.status == STARTED and not waitOnFlip:
            theseKeys = firstT_key.getKeys(keyList=['8'], waitRelease=False)
            _firstT_key_allKeys.extend(theseKeys)
            if len(_firstT_key_allKeys):
                firstT_key.keys = _firstT_key_allKeys[-1].name  # just the last key pressed
                firstT_key.rt = _firstT_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in firstTask_instructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "firstTask_instruct"-------
    for thisComponent in firstTask_instructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    first_block_loop.addData('firstT_text1.started', firstT_text1.tStartRefresh)
    first_block_loop.addData('firstT_text1.stopped', firstT_text1.tStopRefresh)
    # check responses
    if firstT_key.keys in ['', [], None]:  # No response was made
        firstT_key.keys = None
    first_block_loop.addData('firstT_key.keys',firstT_key.keys)
    if firstT_key.keys != None:  # we had a response
        first_block_loop.addData('firstT_key.rt', firstT_key.rt)
    first_block_loop.addData('firstT_key.started', firstT_key.tStartRefresh)
    first_block_loop.addData('firstT_key.stopped', firstT_key.tStopRefresh)
    # the Routine "firstTask_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "initFixation"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    initFixation_img.setImage('img/fixationCross.png')
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
    initFixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "initFixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = initFixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=initFixationClock)
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
            initFixation_img.setAutoDraw(True)
        if initFixation_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > initFixation_img.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                initFixation_img.tStop = t  # not accounting for scr refresh
                initFixation_img.frameNStop = frameN  # exact frame index
                win.timeOnFlip(initFixation_img, 'tStopRefresh')  # time at next scr refresh
                initFixation_img.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in initFixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "initFixation"-------
    for thisComponent in initFixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    first_block_loop.addData('initFixation_img.started', initFixation_img.tStartRefresh)
    first_block_loop.addData('initFixation_img.stopped', initFixation_img.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    firstTrial_loop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(whichBlock),
        seed=None, name='firstTrial_loop')
    thisExp.addLoop(firstTrial_loop)  # add the loop to the experiment
    thisFirstTrial_loop = firstTrial_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFirstTrial_loop.rgb)
    if thisFirstTrial_loop != None:
        for paramName in thisFirstTrial_loop:
            exec('{} = thisFirstTrial_loop[paramName]'.format(paramName))
    
    for thisFirstTrial_loop in firstTrial_loop:
        currentLoop = firstTrial_loop
        # abbreviate parameter names if possible (e.g. rgb = thisFirstTrial_loop.rgb)
        if thisFirstTrial_loop != None:
            for paramName in thisFirstTrial_loop:
                exec('{} = thisFirstTrial_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "firstT"-------
        continueRoutine = True
        # update component parameters for each repeat
        # pick the ISI for the next routine
        # this code component is set to 'both' because we need to remove the 'np'
        # at the start of np.linspace (this is a python library JS won't know what to call. 
        
        # make range from a to b in n stepsizes
        ISIRange = np.linspace(1500, 2000, 500)
        
        # picking from a shuffled array is easier for random selection in JS
        shuffle(ISIRange)
        thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
        
        # save this ISI to our output file
        firstTrial_loop.addData('ISI', thisISI)
        
        bigFace_2.setImage(straightFace)
        task_centerImg_3.setPos(locationC)
        task_centerImg_3.setSize(imageSize)
        task_centerImg_3.setImage(middleStim)
        task_rightImg1_3.setPos(locationR)
        task_rightImg1_3.setSize(imageSize)
        task_rightImg1_3.setImage(rightStim)
        task_leftImg1_3.setPos(locationL)
        task_leftImg1_3.setSize(imageSize)
        task_leftImg1_3.setImage(leftStim)
        task_fixImg_3.setImage('img/fixationCross.png')
        first_task_stim_keyResp.keys = []
        first_task_stim_keyResp.rt = []
        _first_task_stim_keyResp_allKeys = []
        # keep track of which components have finished
        firstTComponents = [bigFace_2, cover_background, task_centerImg_3, task_rightImg1_3, task_leftImg1_3, task_fixImg_3, first_task_stim_keyResp]
        for thisComponent in firstTComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        firstTClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "firstT"-------
        while continueRoutine:
            # get current time
            t = firstTClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=firstTClock)
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
                bigFace_2.setAutoDraw(True)
            if bigFace_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > bigFace_2.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    bigFace_2.tStop = t  # not accounting for scr refresh
                    bigFace_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(bigFace_2, 'tStopRefresh')  # time at next scr refresh
                    bigFace_2.setAutoDraw(False)
            
            # *cover_background* updates
            if cover_background.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cover_background.frameNStart = frameN  # exact frame index
                cover_background.tStart = t  # local t and not account for scr refresh
                cover_background.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cover_background, 'tStartRefresh')  # time at next scr refresh
                cover_background.setAutoDraw(True)
            if cover_background.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cover_background.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    cover_background.tStop = t  # not accounting for scr refresh
                    cover_background.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cover_background, 'tStopRefresh')  # time at next scr refresh
                    cover_background.setAutoDraw(False)
            
            # *task_centerImg_3* updates
            if task_centerImg_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_centerImg_3.frameNStart = frameN  # exact frame index
                task_centerImg_3.tStart = t  # local t and not account for scr refresh
                task_centerImg_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_centerImg_3, 'tStartRefresh')  # time at next scr refresh
                task_centerImg_3.setAutoDraw(True)
            if task_centerImg_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task_centerImg_3.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    task_centerImg_3.tStop = t  # not accounting for scr refresh
                    task_centerImg_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(task_centerImg_3, 'tStopRefresh')  # time at next scr refresh
                    task_centerImg_3.setAutoDraw(False)
            
            # *task_rightImg1_3* updates
            if task_rightImg1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_rightImg1_3.frameNStart = frameN  # exact frame index
                task_rightImg1_3.tStart = t  # local t and not account for scr refresh
                task_rightImg1_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_rightImg1_3, 'tStartRefresh')  # time at next scr refresh
                task_rightImg1_3.setAutoDraw(True)
            if task_rightImg1_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task_rightImg1_3.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    task_rightImg1_3.tStop = t  # not accounting for scr refresh
                    task_rightImg1_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(task_rightImg1_3, 'tStopRefresh')  # time at next scr refresh
                    task_rightImg1_3.setAutoDraw(False)
            
            # *task_leftImg1_3* updates
            if task_leftImg1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_leftImg1_3.frameNStart = frameN  # exact frame index
                task_leftImg1_3.tStart = t  # local t and not account for scr refresh
                task_leftImg1_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_leftImg1_3, 'tStartRefresh')  # time at next scr refresh
                task_leftImg1_3.setAutoDraw(True)
            if task_leftImg1_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task_leftImg1_3.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    task_leftImg1_3.tStop = t  # not accounting for scr refresh
                    task_leftImg1_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(task_leftImg1_3, 'tStopRefresh')  # time at next scr refresh
                    task_leftImg1_3.setAutoDraw(False)
            
            # *task_fixImg_3* updates
            if task_fixImg_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_fixImg_3.frameNStart = frameN  # exact frame index
                task_fixImg_3.tStart = t  # local t and not account for scr refresh
                task_fixImg_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_fixImg_3, 'tStartRefresh')  # time at next scr refresh
                task_fixImg_3.setAutoDraw(True)
            if task_fixImg_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task_fixImg_3.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    task_fixImg_3.tStop = t  # not accounting for scr refresh
                    task_fixImg_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(task_fixImg_3, 'tStopRefresh')  # time at next scr refresh
                    task_fixImg_3.setAutoDraw(False)
            
            # *first_task_stim_keyResp* updates
            waitOnFlip = False
            if first_task_stim_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                first_task_stim_keyResp.frameNStart = frameN  # exact frame index
                first_task_stim_keyResp.tStart = t  # local t and not account for scr refresh
                first_task_stim_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(first_task_stim_keyResp, 'tStartRefresh')  # time at next scr refresh
                first_task_stim_keyResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(first_task_stim_keyResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(first_task_stim_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if first_task_stim_keyResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > first_task_stim_keyResp.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    first_task_stim_keyResp.tStop = t  # not accounting for scr refresh
                    first_task_stim_keyResp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(first_task_stim_keyResp, 'tStopRefresh')  # time at next scr refresh
                    first_task_stim_keyResp.status = FINISHED
            if first_task_stim_keyResp.status == STARTED and not waitOnFlip:
                theseKeys = first_task_stim_keyResp.getKeys(keyList=['1', '8'], waitRelease=False)
                _first_task_stim_keyResp_allKeys.extend(theseKeys)
                if len(_first_task_stim_keyResp_allKeys):
                    first_task_stim_keyResp.keys = [key.name for key in _first_task_stim_keyResp_allKeys]  # storing all keys
                    first_task_stim_keyResp.rt = [key.rt for key in _first_task_stim_keyResp_allKeys]
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in firstTComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "firstT"-------
        for thisComponent in firstTComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        firstTrial_loop.addData('bigFace_2.started', bigFace_2.tStartRefresh)
        firstTrial_loop.addData('bigFace_2.stopped', bigFace_2.tStopRefresh)
        firstTrial_loop.addData('cover_background.started', cover_background.tStartRefresh)
        firstTrial_loop.addData('cover_background.stopped', cover_background.tStopRefresh)
        firstTrial_loop.addData('task_centerImg_3.started', task_centerImg_3.tStartRefresh)
        firstTrial_loop.addData('task_centerImg_3.stopped', task_centerImg_3.tStopRefresh)
        firstTrial_loop.addData('task_fixImg_3.started', task_fixImg_3.tStartRefresh)
        firstTrial_loop.addData('task_fixImg_3.stopped', task_fixImg_3.tStopRefresh)
        # check responses
        if first_task_stim_keyResp.keys in ['', [], None]:  # No response was made
            first_task_stim_keyResp.keys = None
        firstTrial_loop.addData('first_task_stim_keyResp.keys',first_task_stim_keyResp.keys)
        if first_task_stim_keyResp.keys != None:  # we had a response
            firstTrial_loop.addData('first_task_stim_keyResp.rt', first_task_stim_keyResp.rt)
        firstTrial_loop.addData('first_task_stim_keyResp.started', first_task_stim_keyResp.tStartRefresh)
        firstTrial_loop.addData('first_task_stim_keyResp.stopped', first_task_stim_keyResp.tStopRefresh)
        trialNum = trialNum + 1 #iterate trial number for this block
        
        if first_task_stim_keyResp.keys: #if at least one response was made this trial
            if first_task_stim_keyResp.keys[0] == '1': #if the FIRST button pressed was a '1'
                if target == 'left': #if a left target stim was shown this trial
                    accuracy = 1 #mark this trial as correct
                    numCorr = numCorr +1 #iterate number of correct responses for this block
                elif target == 'right': #if a right target stim was shown this trial
                    accuracy = 0 #mark this trial as an error
            elif first_task_stim_keyResp.keys[0] == '8': #if the FIRST button pressed was a '8'
                if target == 'right': #if a right target stim was shown this trial
                    accuracy = 1 #mark this trial as correct
                    numCorr = numCorr +1 #iterate number of correct responses for this block
                elif target == 'left': #if a left target stim was shown this trial
                    accuracy = 0 #mark this trial as an error
                    
        # save this trial's accuracy to our output file
        firstTrial_loop.addData('accuracy', accuracy)
        # the Routine "firstT" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'firstTrial_loop'
    
    
    # ------Prepare to start Routine "firstT_feed"-------
    continueRoutine = True
    # update component parameters for each repeat
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
    firstTrial_loop.addData('blockFeedCat', blockFeedCat)
    
    #reset the following variables to zero before next block starts
    trialNum = 0
    numCorr = 0
    fTfeed_text1_1.setText(blockFeed)
    fTFeed_text2_1.setText('Press the right button')
    fTfeed_key_1.keys = []
    fTfeed_key_1.rt = []
    _fTfeed_key_1_allKeys = []
    # keep track of which components have finished
    firstT_feedComponents = [fTfeed_text1_1, fTFeed_text2_1, fTfeed_key_1]
    for thisComponent in firstT_feedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    firstT_feedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "firstT_feed"-------
    while continueRoutine:
        # get current time
        t = firstT_feedClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=firstT_feedClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fTfeed_text1_1* updates
        if fTfeed_text1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fTfeed_text1_1.frameNStart = frameN  # exact frame index
            fTfeed_text1_1.tStart = t  # local t and not account for scr refresh
            fTfeed_text1_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fTfeed_text1_1, 'tStartRefresh')  # time at next scr refresh
            fTfeed_text1_1.setAutoDraw(True)
        
        # *fTFeed_text2_1* updates
        if fTFeed_text2_1.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            fTFeed_text2_1.frameNStart = frameN  # exact frame index
            fTFeed_text2_1.tStart = t  # local t and not account for scr refresh
            fTFeed_text2_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fTFeed_text2_1, 'tStartRefresh')  # time at next scr refresh
            fTFeed_text2_1.setAutoDraw(True)
        
        # *fTfeed_key_1* updates
        waitOnFlip = False
        if fTfeed_key_1.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            fTfeed_key_1.frameNStart = frameN  # exact frame index
            fTfeed_key_1.tStart = t  # local t and not account for scr refresh
            fTfeed_key_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fTfeed_key_1, 'tStartRefresh')  # time at next scr refresh
            fTfeed_key_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fTfeed_key_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fTfeed_key_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fTfeed_key_1.status == STARTED and not waitOnFlip:
            theseKeys = fTfeed_key_1.getKeys(keyList=['8'], waitRelease=False)
            _fTfeed_key_1_allKeys.extend(theseKeys)
            if len(_fTfeed_key_1_allKeys):
                fTfeed_key_1.keys = _fTfeed_key_1_allKeys[-1].name  # just the last key pressed
                fTfeed_key_1.rt = _fTfeed_key_1_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in firstT_feedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "firstT_feed"-------
    for thisComponent in firstT_feedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    first_block_loop.addData('fTfeed_text1_1.started', fTfeed_text1_1.tStartRefresh)
    first_block_loop.addData('fTfeed_text1_1.stopped', fTfeed_text1_1.tStopRefresh)
    # check responses
    if fTfeed_key_1.keys in ['', [], None]:  # No response was made
        fTfeed_key_1.keys = None
    first_block_loop.addData('fTfeed_key_1.keys',fTfeed_key_1.keys)
    if fTfeed_key_1.keys != None:  # we had a response
        first_block_loop.addData('fTfeed_key_1.rt', fTfeed_key_1.rt)
    first_block_loop.addData('fTfeed_key_1.started', fTfeed_key_1.tStartRefresh)
    first_block_loop.addData('fTfeed_key_1.stopped', fTfeed_key_1.tStopRefresh)
    # the Routine "firstT_feed" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'first_block_loop'


# set up handler to look after randomisation of conditions etc
second_block_loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(secondLoop),
    seed=None, name='second_block_loop')
thisExp.addLoop(second_block_loop)  # add the loop to the experiment
thisSecond_block_loop = second_block_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSecond_block_loop.rgb)
if thisSecond_block_loop != None:
    for paramName in thisSecond_block_loop:
        exec('{} = thisSecond_block_loop[paramName]'.format(paramName))

for thisSecond_block_loop in second_block_loop:
    currentLoop = second_block_loop
    # abbreviate parameter names if possible (e.g. rgb = thisSecond_block_loop.rgb)
    if thisSecond_block_loop != None:
        for paramName in thisSecond_block_loop:
            exec('{} = thisSecond_block_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "firstTask_instruct"-------
    continueRoutine = True
    # update component parameters for each repeat
    blockCounter = blockCounter +1
    
    if blockCounter == 1:
        blockNumText = 'Block 1 of 6'
    elif blockCounter == 2:
        blockNumText = 'Block 2 of 6'
    elif blockCounter == 3:
        blockNumText = 'Block 3 of 6'
    elif blockCounter == 4:
        blockNumText = 'Block 4 of 6'
    elif blockCounter == 5:
        blockNumText = 'Block 5 of 6'
    elif blockCounter == 6:
        blockNumText = 'Block 6 of 6'
    
    firstT_text1.setText(blockNumText)
    firstT_key.keys = []
    firstT_key.rt = []
    _firstT_key_allKeys = []
    # keep track of which components have finished
    firstTask_instructComponents = [firstT_text1, firstT_text2, firstT_key]
    for thisComponent in firstTask_instructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    firstTask_instructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "firstTask_instruct"-------
    while continueRoutine:
        # get current time
        t = firstTask_instructClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=firstTask_instructClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *firstT_text1* updates
        if firstT_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            firstT_text1.frameNStart = frameN  # exact frame index
            firstT_text1.tStart = t  # local t and not account for scr refresh
            firstT_text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(firstT_text1, 'tStartRefresh')  # time at next scr refresh
            firstT_text1.setAutoDraw(True)
        
        # *firstT_text2* updates
        if firstT_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            firstT_text2.frameNStart = frameN  # exact frame index
            firstT_text2.tStart = t  # local t and not account for scr refresh
            firstT_text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(firstT_text2, 'tStartRefresh')  # time at next scr refresh
            firstT_text2.setAutoDraw(True)
        
        # *firstT_key* updates
        waitOnFlip = False
        if firstT_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            firstT_key.frameNStart = frameN  # exact frame index
            firstT_key.tStart = t  # local t and not account for scr refresh
            firstT_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(firstT_key, 'tStartRefresh')  # time at next scr refresh
            firstT_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(firstT_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(firstT_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if firstT_key.status == STARTED and not waitOnFlip:
            theseKeys = firstT_key.getKeys(keyList=['8'], waitRelease=False)
            _firstT_key_allKeys.extend(theseKeys)
            if len(_firstT_key_allKeys):
                firstT_key.keys = _firstT_key_allKeys[-1].name  # just the last key pressed
                firstT_key.rt = _firstT_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in firstTask_instructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "firstTask_instruct"-------
    for thisComponent in firstTask_instructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    second_block_loop.addData('firstT_text1.started', firstT_text1.tStartRefresh)
    second_block_loop.addData('firstT_text1.stopped', firstT_text1.tStopRefresh)
    # check responses
    if firstT_key.keys in ['', [], None]:  # No response was made
        firstT_key.keys = None
    second_block_loop.addData('firstT_key.keys',firstT_key.keys)
    if firstT_key.keys != None:  # we had a response
        second_block_loop.addData('firstT_key.rt', firstT_key.rt)
    second_block_loop.addData('firstT_key.started', firstT_key.tStartRefresh)
    second_block_loop.addData('firstT_key.stopped', firstT_key.tStopRefresh)
    # the Routine "firstTask_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "initFixation"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    initFixation_img.setImage('img/fixationCross.png')
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
    initFixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "initFixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = initFixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=initFixationClock)
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
            initFixation_img.setAutoDraw(True)
        if initFixation_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > initFixation_img.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                initFixation_img.tStop = t  # not accounting for scr refresh
                initFixation_img.frameNStop = frameN  # exact frame index
                win.timeOnFlip(initFixation_img, 'tStopRefresh')  # time at next scr refresh
                initFixation_img.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in initFixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "initFixation"-------
    for thisComponent in initFixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    second_block_loop.addData('initFixation_img.started', initFixation_img.tStartRefresh)
    second_block_loop.addData('initFixation_img.stopped', initFixation_img.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    secondTrial_loop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(whichBlock),
        seed=None, name='secondTrial_loop')
    thisExp.addLoop(secondTrial_loop)  # add the loop to the experiment
    thisSecondTrial_loop = secondTrial_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSecondTrial_loop.rgb)
    if thisSecondTrial_loop != None:
        for paramName in thisSecondTrial_loop:
            exec('{} = thisSecondTrial_loop[paramName]'.format(paramName))
    
    for thisSecondTrial_loop in secondTrial_loop:
        currentLoop = secondTrial_loop
        # abbreviate parameter names if possible (e.g. rgb = thisSecondTrial_loop.rgb)
        if thisSecondTrial_loop != None:
            for paramName in thisSecondTrial_loop:
                exec('{} = thisSecondTrial_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "secondT"-------
        continueRoutine = True
        # update component parameters for each repeat
        # pick the ISI for the next routine
        # this code component is set to 'both' because we need to remove the 'np'
        # at the start of np.linspace (this is a python library JS won't know what to call. 
        
        # make range from a to b in n stepsizes
        ISIRange = np.linspace(1500, 2000, 500)
        
        # picking from a shuffled array is easier for random selection in JS
        shuffle(ISIRange)
        thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
        
        # save this ISI to our output file
        secondTrial_loop.addData('ISI', thisISI)
        
        bigFace.setImage(straightFace)
        task_centerImg_2.setPos(locationC)
        task_centerImg_2.setSize(imageSize)
        task_centerImg_2.setImage(middleStim)
        task_rightImg1_2.setPos(locationR)
        task_rightImg1_2.setSize(imageSize)
        task_rightImg1_2.setImage(rightStim)
        task_leftImg1_2.setPos(locationL)
        task_leftImg1_2.setSize(imageSize)
        task_leftImg1_2.setImage(leftStim)
        task_fixImg_2.setImage('img/fixationCross.png')
        second_task_stim_keyResp.keys = []
        second_task_stim_keyResp.rt = []
        _second_task_stim_keyResp_allKeys = []
        # keep track of which components have finished
        secondTComponents = [bigFace, cover_background_2, task_centerImg_2, task_rightImg1_2, task_leftImg1_2, task_fixImg_2, second_task_stim_keyResp]
        for thisComponent in secondTComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        secondTClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "secondT"-------
        while continueRoutine:
            # get current time
            t = secondTClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=secondTClock)
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
                bigFace.setAutoDraw(True)
            if bigFace.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > bigFace.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    bigFace.tStop = t  # not accounting for scr refresh
                    bigFace.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(bigFace, 'tStopRefresh')  # time at next scr refresh
                    bigFace.setAutoDraw(False)
            
            # *cover_background_2* updates
            if cover_background_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cover_background_2.frameNStart = frameN  # exact frame index
                cover_background_2.tStart = t  # local t and not account for scr refresh
                cover_background_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cover_background_2, 'tStartRefresh')  # time at next scr refresh
                cover_background_2.setAutoDraw(True)
            if cover_background_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cover_background_2.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    cover_background_2.tStop = t  # not accounting for scr refresh
                    cover_background_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cover_background_2, 'tStopRefresh')  # time at next scr refresh
                    cover_background_2.setAutoDraw(False)
            
            # *task_centerImg_2* updates
            if task_centerImg_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_centerImg_2.frameNStart = frameN  # exact frame index
                task_centerImg_2.tStart = t  # local t and not account for scr refresh
                task_centerImg_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_centerImg_2, 'tStartRefresh')  # time at next scr refresh
                task_centerImg_2.setAutoDraw(True)
            if task_centerImg_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task_centerImg_2.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    task_centerImg_2.tStop = t  # not accounting for scr refresh
                    task_centerImg_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(task_centerImg_2, 'tStopRefresh')  # time at next scr refresh
                    task_centerImg_2.setAutoDraw(False)
            
            # *task_rightImg1_2* updates
            if task_rightImg1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_rightImg1_2.frameNStart = frameN  # exact frame index
                task_rightImg1_2.tStart = t  # local t and not account for scr refresh
                task_rightImg1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_rightImg1_2, 'tStartRefresh')  # time at next scr refresh
                task_rightImg1_2.setAutoDraw(True)
            if task_rightImg1_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task_rightImg1_2.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    task_rightImg1_2.tStop = t  # not accounting for scr refresh
                    task_rightImg1_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(task_rightImg1_2, 'tStopRefresh')  # time at next scr refresh
                    task_rightImg1_2.setAutoDraw(False)
            
            # *task_leftImg1_2* updates
            if task_leftImg1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_leftImg1_2.frameNStart = frameN  # exact frame index
                task_leftImg1_2.tStart = t  # local t and not account for scr refresh
                task_leftImg1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_leftImg1_2, 'tStartRefresh')  # time at next scr refresh
                task_leftImg1_2.setAutoDraw(True)
            if task_leftImg1_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task_leftImg1_2.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    task_leftImg1_2.tStop = t  # not accounting for scr refresh
                    task_leftImg1_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(task_leftImg1_2, 'tStopRefresh')  # time at next scr refresh
                    task_leftImg1_2.setAutoDraw(False)
            
            # *task_fixImg_2* updates
            if task_fixImg_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_fixImg_2.frameNStart = frameN  # exact frame index
                task_fixImg_2.tStart = t  # local t and not account for scr refresh
                task_fixImg_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_fixImg_2, 'tStartRefresh')  # time at next scr refresh
                task_fixImg_2.setAutoDraw(True)
            if task_fixImg_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task_fixImg_2.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    task_fixImg_2.tStop = t  # not accounting for scr refresh
                    task_fixImg_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(task_fixImg_2, 'tStopRefresh')  # time at next scr refresh
                    task_fixImg_2.setAutoDraw(False)
            
            # *second_task_stim_keyResp* updates
            waitOnFlip = False
            if second_task_stim_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                second_task_stim_keyResp.frameNStart = frameN  # exact frame index
                second_task_stim_keyResp.tStart = t  # local t and not account for scr refresh
                second_task_stim_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(second_task_stim_keyResp, 'tStartRefresh')  # time at next scr refresh
                second_task_stim_keyResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(second_task_stim_keyResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(second_task_stim_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if second_task_stim_keyResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > second_task_stim_keyResp.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    second_task_stim_keyResp.tStop = t  # not accounting for scr refresh
                    second_task_stim_keyResp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(second_task_stim_keyResp, 'tStopRefresh')  # time at next scr refresh
                    second_task_stim_keyResp.status = FINISHED
            if second_task_stim_keyResp.status == STARTED and not waitOnFlip:
                theseKeys = second_task_stim_keyResp.getKeys(keyList=['1', '8'], waitRelease=False)
                _second_task_stim_keyResp_allKeys.extend(theseKeys)
                if len(_second_task_stim_keyResp_allKeys):
                    second_task_stim_keyResp.keys = [key.name for key in _second_task_stim_keyResp_allKeys]  # storing all keys
                    second_task_stim_keyResp.rt = [key.rt for key in _second_task_stim_keyResp_allKeys]
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in secondTComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "secondT"-------
        for thisComponent in secondTComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        secondTrial_loop.addData('bigFace.started', bigFace.tStartRefresh)
        secondTrial_loop.addData('bigFace.stopped', bigFace.tStopRefresh)
        secondTrial_loop.addData('cover_background_2.started', cover_background_2.tStartRefresh)
        secondTrial_loop.addData('cover_background_2.stopped', cover_background_2.tStopRefresh)
        secondTrial_loop.addData('task_centerImg_2.started', task_centerImg_2.tStartRefresh)
        secondTrial_loop.addData('task_centerImg_2.stopped', task_centerImg_2.tStopRefresh)
        secondTrial_loop.addData('task_fixImg_2.started', task_fixImg_2.tStartRefresh)
        secondTrial_loop.addData('task_fixImg_2.stopped', task_fixImg_2.tStopRefresh)
        # check responses
        if second_task_stim_keyResp.keys in ['', [], None]:  # No response was made
            second_task_stim_keyResp.keys = None
        secondTrial_loop.addData('second_task_stim_keyResp.keys',second_task_stim_keyResp.keys)
        if second_task_stim_keyResp.keys != None:  # we had a response
            secondTrial_loop.addData('second_task_stim_keyResp.rt', second_task_stim_keyResp.rt)
        secondTrial_loop.addData('second_task_stim_keyResp.started', second_task_stim_keyResp.tStartRefresh)
        secondTrial_loop.addData('second_task_stim_keyResp.stopped', second_task_stim_keyResp.tStopRefresh)
        trialNum = trialNum + 1 #iterate trial number for this block
        
        if second_task_stim_keyResp.keys: #if at least one response was made this trial
            if second_task_stim_keyResp.keys[0] == '1': #if the FIRST button pressed was a '1'
                if target == 'left': #if a left target stim was shown this trial
                    accuracy = 1 #mark this trial as correct
                    numCorr = numCorr +1 #iterate number of correct responses for this block
                elif target == 'right': #if a right target stim was shown this trial
                    accuracy = 0 #mark this trial as an error
            elif second_task_stim_keyResp.keys[0] == '8': #if the FIRST button pressed was a '8'
                if target == 'right': #if a right target stim was shown this trial
                    accuracy = 1 #mark this trial as correct
                    numCorr = numCorr +1 #iterate number of correct responses for this block
                elif target == 'left': #if a left target stim was shown this trial
                    accuracy = 0 #mark this trial as an error
                    
        # save this trial's accuracy to our output file
        secondTrial_loop.addData('accuracy', accuracy)
        # the Routine "secondT" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'secondTrial_loop'
    
    
    # ------Prepare to start Routine "secondT_feed"-------
    continueRoutine = True
    # update component parameters for each repeat
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
    secondTrial_loop.addData('blockFeedCat', blockFeedCat)
    
    #reset the following variables to zero before next block starts
    trialNum = 0
    numCorr = 0
    sTfeed_text1.setText(blockFeed)
    scFeed_text2.setText('Press the right button')
    sTfeed_key.keys = []
    sTfeed_key.rt = []
    _sTfeed_key_allKeys = []
    # keep track of which components have finished
    secondT_feedComponents = [sTfeed_text1, scFeed_text2, sTfeed_key]
    for thisComponent in secondT_feedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    secondT_feedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "secondT_feed"-------
    while continueRoutine:
        # get current time
        t = secondT_feedClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=secondT_feedClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sTfeed_text1* updates
        if sTfeed_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sTfeed_text1.frameNStart = frameN  # exact frame index
            sTfeed_text1.tStart = t  # local t and not account for scr refresh
            sTfeed_text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sTfeed_text1, 'tStartRefresh')  # time at next scr refresh
            sTfeed_text1.setAutoDraw(True)
        
        # *scFeed_text2* updates
        if scFeed_text2.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            scFeed_text2.frameNStart = frameN  # exact frame index
            scFeed_text2.tStart = t  # local t and not account for scr refresh
            scFeed_text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(scFeed_text2, 'tStartRefresh')  # time at next scr refresh
            scFeed_text2.setAutoDraw(True)
        
        # *sTfeed_key* updates
        waitOnFlip = False
        if sTfeed_key.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            sTfeed_key.frameNStart = frameN  # exact frame index
            sTfeed_key.tStart = t  # local t and not account for scr refresh
            sTfeed_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sTfeed_key, 'tStartRefresh')  # time at next scr refresh
            sTfeed_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(sTfeed_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(sTfeed_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if sTfeed_key.status == STARTED and not waitOnFlip:
            theseKeys = sTfeed_key.getKeys(keyList=['8'], waitRelease=False)
            _sTfeed_key_allKeys.extend(theseKeys)
            if len(_sTfeed_key_allKeys):
                sTfeed_key.keys = _sTfeed_key_allKeys[-1].name  # just the last key pressed
                sTfeed_key.rt = _sTfeed_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in secondT_feedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "secondT_feed"-------
    for thisComponent in secondT_feedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    second_block_loop.addData('sTfeed_text1.started', sTfeed_text1.tStartRefresh)
    second_block_loop.addData('sTfeed_text1.stopped', sTfeed_text1.tStopRefresh)
    # check responses
    if sTfeed_key.keys in ['', [], None]:  # No response was made
        sTfeed_key.keys = None
    second_block_loop.addData('sTfeed_key.keys',sTfeed_key.keys)
    if sTfeed_key.keys != None:  # we had a response
        second_block_loop.addData('sTfeed_key.rt', sTfeed_key.rt)
    second_block_loop.addData('sTfeed_key.started', sTfeed_key.tStartRefresh)
    second_block_loop.addData('sTfeed_key.stopped', sTfeed_key.tStopRefresh)
    # the Routine "secondT_feed" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'second_block_loop'


# ------Prepare to start Routine "surpriseInstruct"-------
continueRoutine = True
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
surpriseInstructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "surpriseInstruct"-------
while continueRoutine:
    # get current time
    t = surpriseInstructClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=surpriseInstructClock)
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
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in surpriseInstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "surpriseInstruct"-------
for thisComponent in surpriseInstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruct_surprise1.started', instruct_surprise1.tStartRefresh)
thisExp.addData('instruct_surprise1.stopped', instruct_surprise1.tStopRefresh)
# check responses
if instruct_surp1_key_resp.keys in ['', [], None]:  # No response was made
    instruct_surp1_key_resp.keys = None
thisExp.addData('instruct_surp1_key_resp.keys',instruct_surp1_key_resp.keys)
if instruct_surp1_key_resp.keys != None:  # we had a response
    thisExp.addData('instruct_surp1_key_resp.rt', instruct_surp1_key_resp.rt)
thisExp.nextEntry()
# the Routine "surpriseInstruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "counterbalance2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_counterbalance1_2.keys = []
key_resp_counterbalance1_2.rt = []
_key_resp_counterbalance1_2_allKeys = []
# keep track of which components have finished
counterbalance2Components = [cb_text1_2, key_resp_counterbalance1_2]
for thisComponent in counterbalance2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
counterbalance2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "counterbalance2"-------
while continueRoutine:
    # get current time
    t = counterbalance2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=counterbalance2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *cb_text1_2* updates
    if cb_text1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cb_text1_2.frameNStart = frameN  # exact frame index
        cb_text1_2.tStart = t  # local t and not account for scr refresh
        cb_text1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cb_text1_2, 'tStartRefresh')  # time at next scr refresh
        cb_text1_2.setAutoDraw(True)
    
    # *key_resp_counterbalance1_2* updates
    waitOnFlip = False
    if key_resp_counterbalance1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_counterbalance1_2.frameNStart = frameN  # exact frame index
        key_resp_counterbalance1_2.tStart = t  # local t and not account for scr refresh
        key_resp_counterbalance1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_counterbalance1_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_counterbalance1_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_counterbalance1_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_counterbalance1_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_counterbalance1_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_counterbalance1_2.getKeys(keyList=['1', '8'], waitRelease=False)
        _key_resp_counterbalance1_2_allKeys.extend(theseKeys)
        if len(_key_resp_counterbalance1_2_allKeys):
            key_resp_counterbalance1_2.keys = _key_resp_counterbalance1_2_allKeys[-1].name  # just the last key pressed
            key_resp_counterbalance1_2.rt = _key_resp_counterbalance1_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in counterbalance2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "counterbalance2"-------
for thisComponent in counterbalance2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_counterbalance1_2.keys in ['', [], None]:  # No response was made
    key_resp_counterbalance1_2.keys = None
thisExp.addData('key_resp_counterbalance1_2.keys',key_resp_counterbalance1_2.keys)
if key_resp_counterbalance1_2.keys != None:  # we had a response
    thisExp.addData('key_resp_counterbalance1_2.rt', key_resp_counterbalance1_2.rt)
thisExp.addData('key_resp_counterbalance1_2.started', key_resp_counterbalance1_2.tStartRefresh)
thisExp.addData('key_resp_counterbalance1_2.stopped', key_resp_counterbalance1_2.tStopRefresh)
thisExp.nextEntry()
if key_resp_counterbalance1.keys[-1] == '8': 
     first_surpriseLoop = 'surpriseBlock_select1.xlsx'
     second_surpriseLoop = 'surpriseBlock_select2.xlsx'
elif key_resp_counterbalance1.keys[-1] == '1': 
     first_surpriseLoop = 'surpriseBlock_select2.xlsx'
     second_surpriseLoop = 'surpriseBlock_select1.xlsx'



# the Routine "counterbalance2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
surprise_block_loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(first_surpriseLoop),
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
    
    # ------Prepare to start Routine "instructSurpriseTask2"-------
    continueRoutine = True
    # update component parameters for each repeat
    instructMainTask_text.setText(taskTextSource)
    instructMainTask_keyResp.keys = []
    instructMainTask_keyResp.rt = []
    _instructMainTask_keyResp_allKeys = []
    # keep track of which components have finished
    instructSurpriseTask2Components = [instructMainTask_text, instructMainTask_keyResp]
    for thisComponent in instructSurpriseTask2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructSurpriseTask2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructSurpriseTask2"-------
    while continueRoutine:
        # get current time
        t = instructSurpriseTask2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructSurpriseTask2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructMainTask_text* updates
        if instructMainTask_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructMainTask_text.frameNStart = frameN  # exact frame index
            instructMainTask_text.tStart = t  # local t and not account for scr refresh
            instructMainTask_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructMainTask_text, 'tStartRefresh')  # time at next scr refresh
            instructMainTask_text.setAutoDraw(True)
        
        # *instructMainTask_keyResp* updates
        waitOnFlip = False
        if instructMainTask_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructMainTask_keyResp.frameNStart = frameN  # exact frame index
            instructMainTask_keyResp.tStart = t  # local t and not account for scr refresh
            instructMainTask_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructMainTask_keyResp, 'tStartRefresh')  # time at next scr refresh
            instructMainTask_keyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instructMainTask_keyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instructMainTask_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instructMainTask_keyResp.status == STARTED and not waitOnFlip:
            theseKeys = instructMainTask_keyResp.getKeys(keyList=['8'], waitRelease=False)
            _instructMainTask_keyResp_allKeys.extend(theseKeys)
            if len(_instructMainTask_keyResp_allKeys):
                instructMainTask_keyResp.keys = _instructMainTask_keyResp_allKeys[-1].name  # just the last key pressed
                instructMainTask_keyResp.rt = _instructMainTask_keyResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructSurpriseTask2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructSurpriseTask2"-------
    for thisComponent in instructSurpriseTask2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    surprise_block_loop.addData('instructMainTask_text.started', instructMainTask_text.tStartRefresh)
    surprise_block_loop.addData('instructMainTask_text.stopped', instructMainTask_text.tStopRefresh)
    # check responses
    if instructMainTask_keyResp.keys in ['', [], None]:  # No response was made
        instructMainTask_keyResp.keys = None
    surprise_block_loop.addData('instructMainTask_keyResp.keys',instructMainTask_keyResp.keys)
    if instructMainTask_keyResp.keys != None:  # we had a response
        surprise_block_loop.addData('instructMainTask_keyResp.rt', instructMainTask_keyResp.rt)
    surprise_block_loop.addData('instructMainTask_keyResp.started', instructMainTask_keyResp.tStartRefresh)
    surprise_block_loop.addData('instructMainTask_keyResp.stopped', instructMainTask_keyResp.tStopRefresh)
    # the Routine "instructSurpriseTask2" was not non-slip safe, so reset the non-slip timer
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
        
        # ------Prepare to start Routine "surpriseTask"-------
        continueRoutine = True
        # update component parameters for each repeat
        stimulus.setImage(surpriseFaces)
        instructsurpA1_right.setPos((0.4, -0.03))
        instructsurpA1_right.setText(instructsurpA1)
        instructsurpA2_left.setText(instructsurpA2)
        surprise_key_resp.keys = []
        surprise_key_resp.rt = []
        _surprise_key_resp_allKeys = []
        # keep track of which components have finished
        surpriseTaskComponents = [stimulus, instructsurpA1_right, instructsurpA2_left, surprise_key_resp]
        for thisComponent in surpriseTaskComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        surpriseTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "surpriseTask"-------
        while continueRoutine:
            # get current time
            t = surpriseTaskClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=surpriseTaskClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stimulus* updates
            if stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stimulus.frameNStart = frameN  # exact frame index
                stimulus.tStart = t  # local t and not account for scr refresh
                stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimulus, 'tStartRefresh')  # time at next scr refresh
                stimulus.setAutoDraw(True)
            
            # *instructsurpA1_right* updates
            if instructsurpA1_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instructsurpA1_right.frameNStart = frameN  # exact frame index
                instructsurpA1_right.tStart = t  # local t and not account for scr refresh
                instructsurpA1_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instructsurpA1_right, 'tStartRefresh')  # time at next scr refresh
                instructsurpA1_right.setAutoDraw(True)
            
            # *instructsurpA2_left* updates
            if instructsurpA2_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instructsurpA2_left.frameNStart = frameN  # exact frame index
                instructsurpA2_left.tStart = t  # local t and not account for scr refresh
                instructsurpA2_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instructsurpA2_left, 'tStartRefresh')  # time at next scr refresh
                instructsurpA2_left.setAutoDraw(True)
            
            # *surprise_key_resp* updates
            waitOnFlip = False
            if surprise_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                surprise_key_resp.frameNStart = frameN  # exact frame index
                surprise_key_resp.tStart = t  # local t and not account for scr refresh
                surprise_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(surprise_key_resp, 'tStartRefresh')  # time at next scr refresh
                surprise_key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(surprise_key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(surprise_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if surprise_key_resp.status == STARTED and not waitOnFlip:
                theseKeys = surprise_key_resp.getKeys(keyList=['1', '8'], waitRelease=False)
                _surprise_key_resp_allKeys.extend(theseKeys)
                if len(_surprise_key_resp_allKeys):
                    surprise_key_resp.keys = _surprise_key_resp_allKeys[-1].name  # just the last key pressed
                    surprise_key_resp.rt = _surprise_key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in surpriseTaskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "surpriseTask"-------
        for thisComponent in surpriseTaskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('stimulus.started', stimulus.tStartRefresh)
        trials.addData('stimulus.stopped', stimulus.tStopRefresh)
        trials.addData('instructsurpA1_right.started', instructsurpA1_right.tStartRefresh)
        trials.addData('instructsurpA1_right.stopped', instructsurpA1_right.tStopRefresh)
        trials.addData('instructsurpA2_left.started', instructsurpA2_left.tStartRefresh)
        trials.addData('instructsurpA2_left.stopped', instructsurpA2_left.tStopRefresh)
        # check responses
        if surprise_key_resp.keys in ['', [], None]:  # No response was made
            surprise_key_resp.keys = None
        trials.addData('surprise_key_resp.keys',surprise_key_resp.keys)
        if surprise_key_resp.keys != None:  # we had a response
            trials.addData('surprise_key_resp.rt', surprise_key_resp.rt)
        trials.addData('surprise_key_resp.started', surprise_key_resp.tStartRefresh)
        trials.addData('surprise_key_resp.stopped', surprise_key_resp.tStopRefresh)
        # the Routine "surpriseTask" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'surprise_block_loop'


# set up handler to look after randomisation of conditions etc
surprise_block_loop2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(second_surpriseLoop),
    seed=None, name='surprise_block_loop2')
thisExp.addLoop(surprise_block_loop2)  # add the loop to the experiment
thisSurprise_block_loop2 = surprise_block_loop2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSurprise_block_loop2.rgb)
if thisSurprise_block_loop2 != None:
    for paramName in thisSurprise_block_loop2:
        exec('{} = thisSurprise_block_loop2[paramName]'.format(paramName))

for thisSurprise_block_loop2 in surprise_block_loop2:
    currentLoop = surprise_block_loop2
    # abbreviate parameter names if possible (e.g. rgb = thisSurprise_block_loop2.rgb)
    if thisSurprise_block_loop2 != None:
        for paramName in thisSurprise_block_loop2:
            exec('{} = thisSurprise_block_loop2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructSurpriseTask2_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    instructMainTask_text_2.setText(taskTextSource)
    instructMainTask_keyResp_2.keys = []
    instructMainTask_keyResp_2.rt = []
    _instructMainTask_keyResp_2_allKeys = []
    # keep track of which components have finished
    instructSurpriseTask2_2Components = [instructMainTask_text_2, instructMainTask_keyResp_2]
    for thisComponent in instructSurpriseTask2_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructSurpriseTask2_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructSurpriseTask2_2"-------
    while continueRoutine:
        # get current time
        t = instructSurpriseTask2_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructSurpriseTask2_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructMainTask_text_2* updates
        if instructMainTask_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructMainTask_text_2.frameNStart = frameN  # exact frame index
            instructMainTask_text_2.tStart = t  # local t and not account for scr refresh
            instructMainTask_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructMainTask_text_2, 'tStartRefresh')  # time at next scr refresh
            instructMainTask_text_2.setAutoDraw(True)
        
        # *instructMainTask_keyResp_2* updates
        waitOnFlip = False
        if instructMainTask_keyResp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructMainTask_keyResp_2.frameNStart = frameN  # exact frame index
            instructMainTask_keyResp_2.tStart = t  # local t and not account for scr refresh
            instructMainTask_keyResp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructMainTask_keyResp_2, 'tStartRefresh')  # time at next scr refresh
            instructMainTask_keyResp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instructMainTask_keyResp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instructMainTask_keyResp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instructMainTask_keyResp_2.status == STARTED and not waitOnFlip:
            theseKeys = instructMainTask_keyResp_2.getKeys(keyList=['8'], waitRelease=False)
            _instructMainTask_keyResp_2_allKeys.extend(theseKeys)
            if len(_instructMainTask_keyResp_2_allKeys):
                instructMainTask_keyResp_2.keys = _instructMainTask_keyResp_2_allKeys[-1].name  # just the last key pressed
                instructMainTask_keyResp_2.rt = _instructMainTask_keyResp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructSurpriseTask2_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructSurpriseTask2_2"-------
    for thisComponent in instructSurpriseTask2_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    surprise_block_loop2.addData('instructMainTask_text_2.started', instructMainTask_text_2.tStartRefresh)
    surprise_block_loop2.addData('instructMainTask_text_2.stopped', instructMainTask_text_2.tStopRefresh)
    # check responses
    if instructMainTask_keyResp_2.keys in ['', [], None]:  # No response was made
        instructMainTask_keyResp_2.keys = None
    surprise_block_loop2.addData('instructMainTask_keyResp_2.keys',instructMainTask_keyResp_2.keys)
    if instructMainTask_keyResp_2.keys != None:  # we had a response
        surprise_block_loop2.addData('instructMainTask_keyResp_2.rt', instructMainTask_keyResp_2.rt)
    surprise_block_loop2.addData('instructMainTask_keyResp_2.started', instructMainTask_keyResp_2.tStartRefresh)
    surprise_block_loop2.addData('instructMainTask_keyResp_2.stopped', instructMainTask_keyResp_2.tStopRefresh)
    # the Routine "instructSurpriseTask2_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(whichSurpriseBlock),
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
        
        # ------Prepare to start Routine "surpriseTask_2"-------
        continueRoutine = True
        # update component parameters for each repeat
        stimulus_2.setImage(surpriseFaces)
        instructsurpA1_right_2.setPos((0.4, -0.03))
        instructsurpA1_right_2.setText(instructsurpA1)
        instructsurpA2_left_2.setText(instructsurpA2)
        surprise_key_resp_2.keys = []
        surprise_key_resp_2.rt = []
        _surprise_key_resp_2_allKeys = []
        # keep track of which components have finished
        surpriseTask_2Components = [stimulus_2, instructsurpA1_right_2, instructsurpA2_left_2, surprise_key_resp_2]
        for thisComponent in surpriseTask_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        surpriseTask_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "surpriseTask_2"-------
        while continueRoutine:
            # get current time
            t = surpriseTask_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=surpriseTask_2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stimulus_2* updates
            if stimulus_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stimulus_2.frameNStart = frameN  # exact frame index
                stimulus_2.tStart = t  # local t and not account for scr refresh
                stimulus_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimulus_2, 'tStartRefresh')  # time at next scr refresh
                stimulus_2.setAutoDraw(True)
            
            # *instructsurpA1_right_2* updates
            if instructsurpA1_right_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instructsurpA1_right_2.frameNStart = frameN  # exact frame index
                instructsurpA1_right_2.tStart = t  # local t and not account for scr refresh
                instructsurpA1_right_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instructsurpA1_right_2, 'tStartRefresh')  # time at next scr refresh
                instructsurpA1_right_2.setAutoDraw(True)
            
            # *instructsurpA2_left_2* updates
            if instructsurpA2_left_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instructsurpA2_left_2.frameNStart = frameN  # exact frame index
                instructsurpA2_left_2.tStart = t  # local t and not account for scr refresh
                instructsurpA2_left_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instructsurpA2_left_2, 'tStartRefresh')  # time at next scr refresh
                instructsurpA2_left_2.setAutoDraw(True)
            
            # *surprise_key_resp_2* updates
            waitOnFlip = False
            if surprise_key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                surprise_key_resp_2.frameNStart = frameN  # exact frame index
                surprise_key_resp_2.tStart = t  # local t and not account for scr refresh
                surprise_key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(surprise_key_resp_2, 'tStartRefresh')  # time at next scr refresh
                surprise_key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(surprise_key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(surprise_key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if surprise_key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = surprise_key_resp_2.getKeys(keyList=['1', '8'], waitRelease=False)
                _surprise_key_resp_2_allKeys.extend(theseKeys)
                if len(_surprise_key_resp_2_allKeys):
                    surprise_key_resp_2.keys = _surprise_key_resp_2_allKeys[-1].name  # just the last key pressed
                    surprise_key_resp_2.rt = _surprise_key_resp_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in surpriseTask_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "surpriseTask_2"-------
        for thisComponent in surpriseTask_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('stimulus_2.started', stimulus_2.tStartRefresh)
        trials_2.addData('stimulus_2.stopped', stimulus_2.tStopRefresh)
        trials_2.addData('instructsurpA1_right_2.started', instructsurpA1_right_2.tStartRefresh)
        trials_2.addData('instructsurpA1_right_2.stopped', instructsurpA1_right_2.tStopRefresh)
        trials_2.addData('instructsurpA2_left_2.started', instructsurpA2_left_2.tStartRefresh)
        trials_2.addData('instructsurpA2_left_2.stopped', instructsurpA2_left_2.tStopRefresh)
        # check responses
        if surprise_key_resp_2.keys in ['', [], None]:  # No response was made
            surprise_key_resp_2.keys = None
        trials_2.addData('surprise_key_resp_2.keys',surprise_key_resp_2.keys)
        if surprise_key_resp_2.keys != None:  # we had a response
            trials_2.addData('surprise_key_resp_2.rt', surprise_key_resp_2.rt)
        trials_2.addData('surprise_key_resp_2.started', surprise_key_resp_2.tStartRefresh)
        trials_2.addData('surprise_key_resp_2.stopped', surprise_key_resp_2.tStopRefresh)
        # the Routine "surpriseTask_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_2'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'surprise_block_loop2'


# ------Prepare to start Routine "finishMessage"-------
continueRoutine = True
routineTimer.add(3.000000)
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
finishMessageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "finishMessage"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = finishMessageClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finishMessageClock)
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
        finishMessage_text.setAutoDraw(True)
    if finishMessage_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finishMessage_text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            finishMessage_text.tStop = t  # not accounting for scr refresh
            finishMessage_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finishMessage_text, 'tStopRefresh')  # time at next scr refresh
            finishMessage_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishMessageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "finishMessage"-------
for thisComponent in finishMessageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('finishMessage_text.started', finishMessage_text.tStartRefresh)
thisExp.addData('finishMessage_text.stopped', finishMessage_text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
