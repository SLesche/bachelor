#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on December 17, 2022, at 08:32
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

# Run 'Before Experiment' code from code_gen_list_practice
import random
# Run 'Before Experiment' code from code_correct_response
import random
# Run 'Before Experiment' code from code_gen_list_exp
import random
# Run 'Before Experiment' code from code_rsi_exp
rsi = "replace me" # replace this later
# Run 'Before Experiment' code from code_correct_response
import random


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = '00_bat_bachelor'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'Alter': '',
    'Geschlecht (w/m/d/andere)': '',
    'Studiengang': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Sven\\Documents\\Psychologie\\Bachelor-Arbeit\\sven_lesche_ba\\psychopy\\00_bat_bachelor_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1504, 1003], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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

# --- Initialize components for Routine "exp_settings" ---

# --- Initialize components for Routine "init_counterbal" ---
# Run 'Begin Experiment' code from code_set_counterbal
# this is to determine key mappings
map_condition = int(expInfo['participant']) % 2

# Get correct instruction screen
if map_condition == 0:
    instruction_slide_set = "instructions_loop_d.xlsx"
    instruction_rsi_slide = "./instructions_bat_d/Slide10.png"
    instruction_final_slide = "./instructions_bat_d/Slide7.png"

else:
    instruction_slide_set = "instructions_loop_l.xlsx"
    instruction_rsi_slide = "./instructions_bat_l/Slide10.png"
    instruction_final_slide = "./instructions_bat_l/Slide7.png"
final_slide = "./instructions_bat_l/Slide9.png"
# Get correct key mappings
if map_condition == 0:
    map_x_key = "d"
    map_y_key = "l"
else:
    map_x_key = "l"
    map_y_key = "d"

# --- Initialize components for Routine "instruction_screen" ---
key_resp_welcome = keyboard.Keyboard()
image_welcome_slide = visual.ImageStim(
    win=win,
    name='image_welcome_slide', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[2,2],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "generate_list_practice" ---
# Run 'Begin Experiment' code from code_gen_list_practice
# Functions for random generation of 1, 0 at specified rate
def rand50():
    x = random.uniform(0, 1)
    return 1 if (x > 0.5) else 0

def rand60():
    x = random.uniform(0, 1)
    return 1 if (x > 0.4) else 0    

def rand75():
    x = random.uniform(0, 1)
    return 1 if (x > 0.25) else 0

def rand90():
    x = random.uniform(0, 1)
    return 1 if (x > 0.1) else 0


# --- Initialize components for Routine "init_index_practice" ---

# --- Initialize components for Routine "rsi_practice" ---
# Run 'Begin Experiment' code from code_rsi_prac
def randrsi():
    x = random.uniform(0, 1)
    return 0.2 if (x > 0.5) else 1
fixation_cross_practice = visual.ShapeStim(
    win=win, name='fixation_cross_practice', vertices='cross',units='deg', 
    size=(1, 1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)
text_empty_rsi_practice = visual.TextStim(win=win, name='text_empty_rsi_practice',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "stimuli" ---
stimulus = visual.TextStim(win=win, name='stimulus',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_trial = keyboard.Keyboard()

# --- Initialize components for Routine "feedback" ---
# Run 'Begin Experiment' code from code_feedback
feedback_msg = "empty!"
text_feedback = visual.TextStim(win=win, name='text_feedback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "display_instruction" ---

# --- Initialize components for Routine "instruction_rsi" ---
key_resp_instruction_rsi = keyboard.Keyboard()
image_instruction_rsi = visual.ImageStim(
    win=win,
    name='image_instruction_rsi', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[2,2],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "instruction_final" ---
key_resp_instruction_final = keyboard.Keyboard()
image_instruction_final = visual.ImageStim(
    win=win,
    name='image_instruction_final', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[2,2],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "generate_list_exp" ---

# --- Initialize components for Routine "init_index_exp" ---

# --- Initialize components for Routine "rsi_exp" ---
fixation_cross_exp = visual.ShapeStim(
    win=win, name='fixation_cross_exp', vertices='cross',units='deg', 
    size=(1, 1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)
text_empty_rsi_exp = visual.TextStim(win=win, name='text_empty_rsi_exp',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "stimuli" ---
stimulus = visual.TextStim(win=win, name='stimulus',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_trial = keyboard.Keyboard()

# --- Initialize components for Routine "display_break" ---

# --- Initialize components for Routine "break_short" ---
# Run 'Begin Experiment' code from code_block_feedback
feedback_block_msg ='doh!'#if this comes up we forgot to update the msg!
text_short_break = visual.TextStim(win=win, name='text_short_break',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_break = keyboard.Keyboard()

# --- Initialize components for Routine "end_screen" ---
text_end_screen = visual.TextStim(win=win, name='text_end_screen',
    text='Du hast es geschafft. Vielen Dank für deine Teilnahme!! \n\nmit "P" beendest du das Experiment',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_end_screen = keyboard.Keyboard()
image_end_screen = visual.ImageStim(
    win=win,
    name='image_end_screen', units='norm', 
    image=final_slide, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[2,2],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "exp_settings" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_exp_settings
# controls the size of each practice block length
practice_list_size = 15
# amount of trials per experimental block
exp_list_size = 250
# amount of blocks 
exp_nblocks =  12
# Want rsi blocked? 1 for yes, 0 for random rsi
rsi_block = 1
# Fixation cross?
display_fix = 1
# keep track of which components have finished
exp_settingsComponents = []
for thisComponent in exp_settingsComponents:
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

# --- Run Routine "exp_settings" ---
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
    for thisComponent in exp_settingsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "exp_settings" ---
for thisComponent in exp_settingsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "exp_settings" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "init_counterbal" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
init_counterbalComponents = []
for thisComponent in init_counterbalComponents:
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

# --- Run Routine "init_counterbal" ---
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
    for thisComponent in init_counterbalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "init_counterbal" ---
for thisComponent in init_counterbalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from code_set_counterbal
thisExp.addData("map_condition", map_condition)
thisExp.addData("map_x_key", map_x_key)
thisExp.addData("map_y_key", map_y_key)
# the Routine "init_counterbal" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_instruction = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(instruction_slide_set),
    seed=None, name='loop_instruction')
thisExp.addLoop(loop_instruction)  # add the loop to the experiment
thisLoop_instruction = loop_instruction.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_instruction.rgb)
if thisLoop_instruction != None:
    for paramName in thisLoop_instruction:
        exec('{} = thisLoop_instruction[paramName]'.format(paramName))

for thisLoop_instruction in loop_instruction:
    currentLoop = loop_instruction
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_instruction.rgb)
    if thisLoop_instruction != None:
        for paramName in thisLoop_instruction:
            exec('{} = thisLoop_instruction[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "instruction_screen" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_welcome.keys = []
    key_resp_welcome.rt = []
    _key_resp_welcome_allKeys = []
    image_welcome_slide.setImage(slide)
    # keep track of which components have finished
    instruction_screenComponents = [key_resp_welcome, image_welcome_slide]
    for thisComponent in instruction_screenComponents:
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
    
    # --- Run Routine "instruction_screen" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_welcome* updates
        waitOnFlip = False
        if key_resp_welcome.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_welcome.frameNStart = frameN  # exact frame index
            key_resp_welcome.tStart = t  # local t and not account for scr refresh
            key_resp_welcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_welcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_welcome.started')
            key_resp_welcome.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_welcome.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_welcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_welcome.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_welcome.getKeys(keyList=['space', 'j'], waitRelease=False)
            _key_resp_welcome_allKeys.extend(theseKeys)
            if len(_key_resp_welcome_allKeys):
                key_resp_welcome.keys = _key_resp_welcome_allKeys[-1].name  # just the last key pressed
                key_resp_welcome.rt = _key_resp_welcome_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *image_welcome_slide* updates
        if image_welcome_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_welcome_slide.frameNStart = frameN  # exact frame index
            image_welcome_slide.tStart = t  # local t and not account for scr refresh
            image_welcome_slide.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_welcome_slide, 'tStartRefresh')  # time at next scr refresh
            image_welcome_slide.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction_screenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction_screen" ---
    for thisComponent in instruction_screenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_welcome.keys in ['', [], None]:  # No response was made
        key_resp_welcome.keys = None
    loop_instruction.addData('key_resp_welcome.keys',key_resp_welcome.keys)
    if key_resp_welcome.keys != None:  # we had a response
        loop_instruction.addData('key_resp_welcome.rt', key_resp_welcome.rt)
    # the Routine "instruction_screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'loop_instruction'


# set up handler to look after randomisation of conditions etc
loop_rsi_practice = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop_rsi_practice')
thisExp.addLoop(loop_rsi_practice)  # add the loop to the experiment
thisLoop_rsi_practice = loop_rsi_practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_rsi_practice.rgb)
if thisLoop_rsi_practice != None:
    for paramName in thisLoop_rsi_practice:
        exec('{} = thisLoop_rsi_practice[paramName]'.format(paramName))

for thisLoop_rsi_practice in loop_rsi_practice:
    currentLoop = loop_rsi_practice
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_rsi_practice.rgb)
    if thisLoop_rsi_practice != None:
        for paramName in thisLoop_rsi_practice:
            exec('{} = thisLoop_rsi_practice[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "generate_list_practice" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_gen_list_practice
    # Create a list of size N to be filled later
    empty_list = ["fill me"] * practice_list_size
    
    # Create a variable for correct answer to be stored in later
    correct = "replace me"
    
    # want to generate a list of trial stimuli x,y with mostly alternating patter but some other instances
    # here 1 represents go trial, 0 represents nogo trial
    # I want to always have two go trials between nogo trials
    for i in range(len(empty_list)):
        if i <= 2:
            empty_list[i] = 1 # go trials on first 3
        elif ((empty_list[i-1] == 1) & (empty_list[i-2] == 1)): # if previous trial is go, then 25% chance of nogo
            empty_list[i] = rand60()
        elif ((empty_list[i-1] == 1) & (empty_list[i-2] == 0)): # always want two go trials after a nogo trial
            empty_list[i] = 1
        elif empty_list[i-1] == 0: # if prev trial is nogo
            if empty_list[i-2] == 0: # and two nogo trials in a row, always go with a go trial
                empty_list[i] = 1
            else: # if only 1 before is nogo, 10 % chance of creating another one
                empty_list[i] = rand90()
    
    # now translate 1 and 0 into stimuli
    for i in range(len(empty_list)):
        if i == 0: # first stim is always go trial and x
            empty_list[i] = "X"
        elif empty_list[i] == 1: # if go trial
            if empty_list[i-1] == "X": 
                empty_list[i] = "Y"
            elif empty_list[i-1] == "Y":
                empty_list[i] = "X"
        elif empty_list[i] == 0: # if nogo trial
            empty_list[i] = empty_list[i-1]
    
    
    # keep track of which components have finished
    generate_list_practiceComponents = []
    for thisComponent in generate_list_practiceComponents:
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
    
    # --- Run Routine "generate_list_practice" ---
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
        for thisComponent in generate_list_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "generate_list_practice" ---
    for thisComponent in generate_list_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "generate_list_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    loop_practice = data.TrialHandler(nReps=practice_list_size, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loop_practice')
    thisExp.addLoop(loop_practice)  # add the loop to the experiment
    thisLoop_practice = loop_practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_practice.rgb)
    if thisLoop_practice != None:
        for paramName in thisLoop_practice:
            exec('{} = thisLoop_practice[paramName]'.format(paramName))
    
    for thisLoop_practice in loop_practice:
        currentLoop = loop_practice
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_practice.rgb)
        if thisLoop_practice != None:
            for paramName in thisLoop_practice:
                exec('{} = thisLoop_practice[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "init_index_practice" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_init_index_prac
        index = loop_practice.thisN
        # keep track of which components have finished
        init_index_practiceComponents = []
        for thisComponent in init_index_practiceComponents:
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
        
        # --- Run Routine "init_index_practice" ---
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
            for thisComponent in init_index_practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "init_index_practice" ---
        for thisComponent in init_index_practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_init_index_prac
        thisExp.addData("index", index)
        # the Routine "init_index_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "rsi_practice" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_rsi_prac
        # check condition of rsi block first
        if rsi_block == 1:
            if loop_rsi_practice.thisN % 2 == 0:
                rsi = 1
            else:
                rsi = 0.2
        else:
            rsi = randrsi()
        
        # Fixation cross
        if display_fix == 1:
            fix_dur = rsi
        else:
            fix_dur = 0
        text_empty_rsi_practice.setText('')
        # keep track of which components have finished
        rsi_practiceComponents = [fixation_cross_practice, text_empty_rsi_practice]
        for thisComponent in rsi_practiceComponents:
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
        
        # --- Run Routine "rsi_practice" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_cross_practice* updates
            if fixation_cross_practice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                fixation_cross_practice.frameNStart = frameN  # exact frame index
                fixation_cross_practice.tStart = t  # local t and not account for scr refresh
                fixation_cross_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_cross_practice, 'tStartRefresh')  # time at next scr refresh
                fixation_cross_practice.setAutoDraw(True)
            if fixation_cross_practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_cross_practice.tStartRefresh + fix_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_cross_practice.tStop = t  # not accounting for scr refresh
                    fixation_cross_practice.frameNStop = frameN  # exact frame index
                    fixation_cross_practice.setAutoDraw(False)
            
            # *text_empty_rsi_practice* updates
            if text_empty_rsi_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_empty_rsi_practice.frameNStart = frameN  # exact frame index
                text_empty_rsi_practice.tStart = t  # local t and not account for scr refresh
                text_empty_rsi_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_empty_rsi_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_empty_rsi_practice.started')
                text_empty_rsi_practice.setAutoDraw(True)
            if text_empty_rsi_practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_empty_rsi_practice.tStartRefresh + rsi-frameTolerance:
                    # keep track of stop time/frame for later
                    text_empty_rsi_practice.tStop = t  # not accounting for scr refresh
                    text_empty_rsi_practice.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_empty_rsi_practice.stopped')
                    text_empty_rsi_practice.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rsi_practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "rsi_practice" ---
        for thisComponent in rsi_practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_rsi_prac
        thisExp.addData("rsi", rsi)
        # the Routine "rsi_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "stimuli" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_correct_response
        # Correct is correct_map set by counterbalance procedure
        if index == 0: # first trial is always go
            if empty_list[index] == "X":
                correct = map_x_key
            elif empty_list[index] == "Y":
                correct = map_y_key
        elif empty_list[index] != empty_list[index-1]: # if go trial
            if empty_list[index] == "X":
                correct = map_x_key
            elif empty_list[index] == "Y":
                correct = map_y_key
        elif empty_list[index] == empty_list[index - 1]: # if nogo trial
            correct = "None"
        
        # Get type of trial
        if correct == "None":
            trial_type = "nogo"
        else:
            trial_type = "go"
        stimulus.setText(empty_list[index])
        key_resp_trial.keys = []
        key_resp_trial.rt = []
        _key_resp_trial_allKeys = []
        # keep track of which components have finished
        stimuliComponents = [stimulus, key_resp_trial]
        for thisComponent in stimuliComponents:
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
        
        # --- Run Routine "stimuli" ---
        while continueRoutine and routineTimer.getTime() < 0.8:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimulus.started')
                stimulus.setAutoDraw(True)
            if stimulus.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stimulus.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    stimulus.tStop = t  # not accounting for scr refresh
                    stimulus.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stimulus.stopped')
                    stimulus.setAutoDraw(False)
            
            # *key_resp_trial* updates
            waitOnFlip = False
            if key_resp_trial.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                key_resp_trial.frameNStart = frameN  # exact frame index
                key_resp_trial.tStart = t  # local t and not account for scr refresh
                key_resp_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_trial, 'tStartRefresh')  # time at next scr refresh
                key_resp_trial.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_trial.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_trial.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_trial.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_trial.tStartRefresh + 0.7-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_trial.tStop = t  # not accounting for scr refresh
                    key_resp_trial.frameNStop = frameN  # exact frame index
                    key_resp_trial.status = FINISHED
            if key_resp_trial.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_trial.getKeys(keyList=["d", "l"], waitRelease=False)
                _key_resp_trial_allKeys.extend(theseKeys)
                if len(_key_resp_trial_allKeys):
                    key_resp_trial.keys = _key_resp_trial_allKeys[-1].name  # just the last key pressed
                    key_resp_trial.rt = _key_resp_trial_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_trial.keys == str(correct)) or (key_resp_trial.keys == correct):
                        key_resp_trial.corr = 1
                    else:
                        key_resp_trial.corr = 0
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
            for thisComponent in stimuliComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "stimuli" ---
        for thisComponent in stimuliComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_correct_response
        thisExp.addData("stimulus", empty_list[index])
        thisExp.addData("correct", correct)
        thisExp.addData("trial_type", trial_type)
        
        # check responses
        if key_resp_trial.keys in ['', [], None]:  # No response was made
            key_resp_trial.keys = None
            # was no response the correct answer?!
            if str(correct).lower() == 'none':
               key_resp_trial.corr = 1;  # correct non-response
            else:
               key_resp_trial.corr = 0;  # failed to respond (incorrectly)
        # store data for loop_practice (TrialHandler)
        loop_practice.addData('key_resp_trial.keys',key_resp_trial.keys)
        loop_practice.addData('key_resp_trial.corr', key_resp_trial.corr)
        if key_resp_trial.keys != None:  # we had a response
            loop_practice.addData('key_resp_trial.rt', key_resp_trial.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.800000)
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_feedback
        if key_resp_trial.corr:#stored on last run routine
            feedback_msg = "richtig"
            feedback_msg_color = 'green'
            feedback_dur = 0.6
        else:
            if ((empty_list[index] == empty_list[index-1]) & (index != 0)):
                feedback_msg = "falsch \n \n bei Wiederholungen keine Taste drücken"
                feedback_msg_color = 'red'
                feedback_dur = 1
            else:
                feedback_msg = "falsch"
                feedback_msg_color = 'red'
                feedback_dur = 0.6
        
        text_feedback.setColor(feedback_msg_color, colorSpace='rgb')
        text_feedback.setText(feedback_msg)
        # keep track of which components have finished
        feedbackComponents = [text_feedback]
        for thisComponent in feedbackComponents:
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
        
        # --- Run Routine "feedback" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_feedback* updates
            if text_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_feedback.frameNStart = frameN  # exact frame index
                text_feedback.tStart = t  # local t and not account for scr refresh
                text_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_feedback, 'tStartRefresh')  # time at next scr refresh
                text_feedback.setAutoDraw(True)
            if text_feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_feedback.tStartRefresh + feedback_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    text_feedback.tStop = t  # not accounting for scr refresh
                    text_feedback.frameNStop = frameN  # exact frame index
                    text_feedback.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed practice_list_size repeats of 'loop_practice'
    
    
    # --- Prepare to start Routine "display_instruction" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_instruction
    # check to see if loop is on last trial if it is, dont show the break/instruction slide
    if loop_rsi_practice.nRemaining == 0:
        inst_dur = 0
    else:
        inst_dur = 600
    # keep track of which components have finished
    display_instructionComponents = []
    for thisComponent in display_instructionComponents:
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
    
    # --- Run Routine "display_instruction" ---
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
        for thisComponent in display_instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "display_instruction" ---
    for thisComponent in display_instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "display_instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instruction_rsi" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_instruction_rsi.keys = []
    key_resp_instruction_rsi.rt = []
    _key_resp_instruction_rsi_allKeys = []
    image_instruction_rsi.setImage(instruction_rsi_slide)
    # keep track of which components have finished
    instruction_rsiComponents = [key_resp_instruction_rsi, image_instruction_rsi]
    for thisComponent in instruction_rsiComponents:
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
    
    # --- Run Routine "instruction_rsi" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_instruction_rsi* updates
        waitOnFlip = False
        if key_resp_instruction_rsi.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_instruction_rsi.frameNStart = frameN  # exact frame index
            key_resp_instruction_rsi.tStart = t  # local t and not account for scr refresh
            key_resp_instruction_rsi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_instruction_rsi, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_instruction_rsi.started')
            key_resp_instruction_rsi.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_instruction_rsi.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_instruction_rsi.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_instruction_rsi.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_instruction_rsi.tStartRefresh + inst_dur-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_instruction_rsi.tStop = t  # not accounting for scr refresh
                key_resp_instruction_rsi.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_instruction_rsi.stopped')
                key_resp_instruction_rsi.status = FINISHED
        if key_resp_instruction_rsi.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_instruction_rsi.getKeys(keyList=['space', 'j'], waitRelease=False)
            _key_resp_instruction_rsi_allKeys.extend(theseKeys)
            if len(_key_resp_instruction_rsi_allKeys):
                key_resp_instruction_rsi.keys = _key_resp_instruction_rsi_allKeys[-1].name  # just the last key pressed
                key_resp_instruction_rsi.rt = _key_resp_instruction_rsi_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *image_instruction_rsi* updates
        if image_instruction_rsi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_instruction_rsi.frameNStart = frameN  # exact frame index
            image_instruction_rsi.tStart = t  # local t and not account for scr refresh
            image_instruction_rsi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_instruction_rsi, 'tStartRefresh')  # time at next scr refresh
            image_instruction_rsi.setAutoDraw(True)
        if image_instruction_rsi.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_instruction_rsi.tStartRefresh + inst_dur-frameTolerance:
                # keep track of stop time/frame for later
                image_instruction_rsi.tStop = t  # not accounting for scr refresh
                image_instruction_rsi.frameNStop = frameN  # exact frame index
                image_instruction_rsi.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction_rsiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction_rsi" ---
    for thisComponent in instruction_rsiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_instruction_rsi.keys in ['', [], None]:  # No response was made
        key_resp_instruction_rsi.keys = None
    loop_rsi_practice.addData('key_resp_instruction_rsi.keys',key_resp_instruction_rsi.keys)
    if key_resp_instruction_rsi.keys != None:  # we had a response
        loop_rsi_practice.addData('key_resp_instruction_rsi.rt', key_resp_instruction_rsi.rt)
    # the Routine "instruction_rsi" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 2.0 repeats of 'loop_rsi_practice'


# --- Prepare to start Routine "instruction_final" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_instruction_final.keys = []
key_resp_instruction_final.rt = []
_key_resp_instruction_final_allKeys = []
image_instruction_final.setImage(instruction_final_slide)
# keep track of which components have finished
instruction_finalComponents = [key_resp_instruction_final, image_instruction_final]
for thisComponent in instruction_finalComponents:
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

# --- Run Routine "instruction_final" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_instruction_final* updates
    waitOnFlip = False
    if key_resp_instruction_final.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instruction_final.frameNStart = frameN  # exact frame index
        key_resp_instruction_final.tStart = t  # local t and not account for scr refresh
        key_resp_instruction_final.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instruction_final, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_instruction_final.started')
        key_resp_instruction_final.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instruction_final.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instruction_final.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instruction_final.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instruction_final.getKeys(keyList=['space', 'j'], waitRelease=False)
        _key_resp_instruction_final_allKeys.extend(theseKeys)
        if len(_key_resp_instruction_final_allKeys):
            key_resp_instruction_final.keys = _key_resp_instruction_final_allKeys[-1].name  # just the last key pressed
            key_resp_instruction_final.rt = _key_resp_instruction_final_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_instruction_final* updates
    if image_instruction_final.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_instruction_final.frameNStart = frameN  # exact frame index
        image_instruction_final.tStart = t  # local t and not account for scr refresh
        image_instruction_final.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_instruction_final, 'tStartRefresh')  # time at next scr refresh
        image_instruction_final.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_finalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction_final" ---
for thisComponent in instruction_finalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_instruction_final.keys in ['', [], None]:  # No response was made
    key_resp_instruction_final.keys = None
thisExp.addData('key_resp_instruction_final.keys',key_resp_instruction_final.keys)
if key_resp_instruction_final.keys != None:  # we had a response
    thisExp.addData('key_resp_instruction_final.rt', key_resp_instruction_final.rt)
thisExp.nextEntry()
# the Routine "instruction_final" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_exp = data.TrialHandler(nReps=exp_nblocks, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop_exp')
thisExp.addLoop(loop_exp)  # add the loop to the experiment
thisLoop_exp = loop_exp.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_exp.rgb)
if thisLoop_exp != None:
    for paramName in thisLoop_exp:
        exec('{} = thisLoop_exp[paramName]'.format(paramName))

for thisLoop_exp in loop_exp:
    currentLoop = loop_exp
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_exp.rgb)
    if thisLoop_exp != None:
        for paramName in thisLoop_exp:
            exec('{} = thisLoop_exp[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "generate_list_exp" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_gen_list_exp
    # Create a list of size N to be filled later
    empty_list = ["fill me"] * exp_list_size
    
    # Create a variable for correct answer to be stored in later
    correct = "replace me"
    
    # want to generate a list of trial stimuli x,y with mostly alternating patter but some other instances
    # here 1 represents go trial, 0 represents nogo trial
    # I want to always have two go trials between nogo trials
    for i in range(len(empty_list)):
        if i <= 2:
            empty_list[i] = 1 # go trials on first 3
        elif ((empty_list[i-1] == 1) & (empty_list[i-2] == 1)): # if previous trial is go, then 25% chance of nogo
            empty_list[i] = rand60()
        elif ((empty_list[i-1] == 1) & (empty_list[i-2] == 0)): # always want two go trials after a nogo trial
            empty_list[i] = 1
        elif empty_list[i-1] == 0: # if prev trial is nogo
            if empty_list[i-2] == 0: # and two nogo trials in a row, always go with a go trial
                empty_list[i] = 1
            else: # if only 1 before is nogo, 10 % chance of creating another one
                empty_list[i] = rand90()
    
    # now translate 1 and 0 into stimuli
    for i in range(len(empty_list)):
        if i == 0: # first stim is always go trial and x
            empty_list[i] = "X"
        elif empty_list[i] == 1: # if go trial
            if empty_list[i-1] == "X": 
                empty_list[i] = "Y"
            elif empty_list[i-1] == "Y":
                empty_list[i] = "X"
        elif empty_list[i] == 0: # if nogo trial
            empty_list[i] = empty_list[i-1]
    
    
    # keep track of which components have finished
    generate_list_expComponents = []
    for thisComponent in generate_list_expComponents:
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
    
    # --- Run Routine "generate_list_exp" ---
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
        for thisComponent in generate_list_expComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "generate_list_exp" ---
    for thisComponent in generate_list_expComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "generate_list_exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    loop_trials = data.TrialHandler(nReps=exp_list_size, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loop_trials')
    thisExp.addLoop(loop_trials)  # add the loop to the experiment
    thisLoop_trial = loop_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_trial.rgb)
    if thisLoop_trial != None:
        for paramName in thisLoop_trial:
            exec('{} = thisLoop_trial[paramName]'.format(paramName))
    
    for thisLoop_trial in loop_trials:
        currentLoop = loop_trials
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_trial.rgb)
        if thisLoop_trial != None:
            for paramName in thisLoop_trial:
                exec('{} = thisLoop_trial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "init_index_exp" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_init_index_exp
        index = loop_trials.thisN
        # keep track of which components have finished
        init_index_expComponents = []
        for thisComponent in init_index_expComponents:
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
        
        # --- Run Routine "init_index_exp" ---
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
            for thisComponent in init_index_expComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "init_index_exp" ---
        for thisComponent in init_index_expComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_init_index_exp
        thisExp.addData("index", index)
        # the Routine "init_index_exp" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "rsi_exp" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_rsi_exp
        # check condition of rsi block first
        if rsi_block == 1:
            if loop_exp.thisN % 2 == 0:
                rsi = 1
            else:
                rsi = 0.2
        else:
            rsi = randrsi()
        
        # Fixation cross
        if display_fix == 1:
            fix_dur = rsi
        else:
            fix_dur = 0
        text_empty_rsi_exp.setText('')
        # keep track of which components have finished
        rsi_expComponents = [fixation_cross_exp, text_empty_rsi_exp]
        for thisComponent in rsi_expComponents:
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
        
        # --- Run Routine "rsi_exp" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_cross_exp* updates
            if fixation_cross_exp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                fixation_cross_exp.frameNStart = frameN  # exact frame index
                fixation_cross_exp.tStart = t  # local t and not account for scr refresh
                fixation_cross_exp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_cross_exp, 'tStartRefresh')  # time at next scr refresh
                fixation_cross_exp.setAutoDraw(True)
            if fixation_cross_exp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_cross_exp.tStartRefresh + fix_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_cross_exp.tStop = t  # not accounting for scr refresh
                    fixation_cross_exp.frameNStop = frameN  # exact frame index
                    fixation_cross_exp.setAutoDraw(False)
            
            # *text_empty_rsi_exp* updates
            if text_empty_rsi_exp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_empty_rsi_exp.frameNStart = frameN  # exact frame index
                text_empty_rsi_exp.tStart = t  # local t and not account for scr refresh
                text_empty_rsi_exp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_empty_rsi_exp, 'tStartRefresh')  # time at next scr refresh
                text_empty_rsi_exp.setAutoDraw(True)
            if text_empty_rsi_exp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_empty_rsi_exp.tStartRefresh + rsi-frameTolerance:
                    # keep track of stop time/frame for later
                    text_empty_rsi_exp.tStop = t  # not accounting for scr refresh
                    text_empty_rsi_exp.frameNStop = frameN  # exact frame index
                    text_empty_rsi_exp.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rsi_expComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "rsi_exp" ---
        for thisComponent in rsi_expComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_rsi_exp
        thisExp.addData("rsi", rsi)
        # the Routine "rsi_exp" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "stimuli" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_correct_response
        # Correct is correct_map set by counterbalance procedure
        if index == 0: # first trial is always go
            if empty_list[index] == "X":
                correct = map_x_key
            elif empty_list[index] == "Y":
                correct = map_y_key
        elif empty_list[index] != empty_list[index-1]: # if go trial
            if empty_list[index] == "X":
                correct = map_x_key
            elif empty_list[index] == "Y":
                correct = map_y_key
        elif empty_list[index] == empty_list[index - 1]: # if nogo trial
            correct = "None"
        
        # Get type of trial
        if correct == "None":
            trial_type = "nogo"
        else:
            trial_type = "go"
        stimulus.setText(empty_list[index])
        key_resp_trial.keys = []
        key_resp_trial.rt = []
        _key_resp_trial_allKeys = []
        # keep track of which components have finished
        stimuliComponents = [stimulus, key_resp_trial]
        for thisComponent in stimuliComponents:
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
        
        # --- Run Routine "stimuli" ---
        while continueRoutine and routineTimer.getTime() < 0.8:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimulus.started')
                stimulus.setAutoDraw(True)
            if stimulus.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stimulus.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    stimulus.tStop = t  # not accounting for scr refresh
                    stimulus.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stimulus.stopped')
                    stimulus.setAutoDraw(False)
            
            # *key_resp_trial* updates
            waitOnFlip = False
            if key_resp_trial.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                key_resp_trial.frameNStart = frameN  # exact frame index
                key_resp_trial.tStart = t  # local t and not account for scr refresh
                key_resp_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_trial, 'tStartRefresh')  # time at next scr refresh
                key_resp_trial.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_trial.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_trial.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_trial.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_trial.tStartRefresh + 0.7-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_trial.tStop = t  # not accounting for scr refresh
                    key_resp_trial.frameNStop = frameN  # exact frame index
                    key_resp_trial.status = FINISHED
            if key_resp_trial.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_trial.getKeys(keyList=["d", "l"], waitRelease=False)
                _key_resp_trial_allKeys.extend(theseKeys)
                if len(_key_resp_trial_allKeys):
                    key_resp_trial.keys = _key_resp_trial_allKeys[-1].name  # just the last key pressed
                    key_resp_trial.rt = _key_resp_trial_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_trial.keys == str(correct)) or (key_resp_trial.keys == correct):
                        key_resp_trial.corr = 1
                    else:
                        key_resp_trial.corr = 0
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
            for thisComponent in stimuliComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "stimuli" ---
        for thisComponent in stimuliComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_correct_response
        thisExp.addData("stimulus", empty_list[index])
        thisExp.addData("correct", correct)
        thisExp.addData("trial_type", trial_type)
        
        # check responses
        if key_resp_trial.keys in ['', [], None]:  # No response was made
            key_resp_trial.keys = None
            # was no response the correct answer?!
            if str(correct).lower() == 'none':
               key_resp_trial.corr = 1;  # correct non-response
            else:
               key_resp_trial.corr = 0;  # failed to respond (incorrectly)
        # store data for loop_trials (TrialHandler)
        loop_trials.addData('key_resp_trial.keys',key_resp_trial.keys)
        loop_trials.addData('key_resp_trial.corr', key_resp_trial.corr)
        if key_resp_trial.keys != None:  # we had a response
            loop_trials.addData('key_resp_trial.rt', key_resp_trial.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.800000)
        thisExp.nextEntry()
        
    # completed exp_list_size repeats of 'loop_trials'
    
    
    # --- Prepare to start Routine "display_break" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_break
    # check to see if loop is on last trial if it is, dont show the break/instruction slide
    if loop_exp.nRemaining == 0:
        inst_dur = 0
    else:
        inst_dur = 600
    # keep track of which components have finished
    display_breakComponents = []
    for thisComponent in display_breakComponents:
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
    
    # --- Run Routine "display_break" ---
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
        for thisComponent in display_breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "display_break" ---
    for thisComponent in display_breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "display_break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "break_short" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_block_feedback
    nCorr = loop_trials.data['key_resp_trial.corr'].sum() #.std(), .mean() also available
    p_corr = round(nCorr / 80, 2)*100
    feedback_block_msg = "%i" %p_corr
    text_short_break.setText('Du hast nun Block ' + str(loop_exp.thisN + 1) + ' von ' + str(loop_exp.nRemaining + loop_exp.thisN + 1) + ' abgeschlossen. \n Mache gerne eine kurze Pause. \n \n Mit "Leertaste" geht es weiter')
    key_resp_break.keys = []
    key_resp_break.rt = []
    _key_resp_break_allKeys = []
    # keep track of which components have finished
    break_shortComponents = [text_short_break, key_resp_break]
    for thisComponent in break_shortComponents:
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
    
    # --- Run Routine "break_short" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_short_break* updates
        if text_short_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_short_break.frameNStart = frameN  # exact frame index
            text_short_break.tStart = t  # local t and not account for scr refresh
            text_short_break.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_short_break, 'tStartRefresh')  # time at next scr refresh
            text_short_break.setAutoDraw(True)
        if text_short_break.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_short_break.tStartRefresh + inst_dur-frameTolerance:
                # keep track of stop time/frame for later
                text_short_break.tStop = t  # not accounting for scr refresh
                text_short_break.frameNStop = frameN  # exact frame index
                text_short_break.setAutoDraw(False)
        
        # *key_resp_break* updates
        waitOnFlip = False
        if key_resp_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_break.frameNStart = frameN  # exact frame index
            key_resp_break.tStart = t  # local t and not account for scr refresh
            key_resp_break.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_break, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_break.started')
            key_resp_break.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_break.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_break.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_break.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_break.tStartRefresh + inst_dur-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_break.tStop = t  # not accounting for scr refresh
                key_resp_break.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_break.stopped')
                key_resp_break.status = FINISHED
        if key_resp_break.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_break.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_break_allKeys.extend(theseKeys)
            if len(_key_resp_break_allKeys):
                key_resp_break.keys = _key_resp_break_allKeys[-1].name  # just the last key pressed
                key_resp_break.rt = _key_resp_break_allKeys[-1].rt
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
        for thisComponent in break_shortComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "break_short" ---
    for thisComponent in break_shortComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_break.keys in ['', [], None]:  # No response was made
        key_resp_break.keys = None
    loop_exp.addData('key_resp_break.keys',key_resp_break.keys)
    if key_resp_break.keys != None:  # we had a response
        loop_exp.addData('key_resp_break.rt', key_resp_break.rt)
    # the Routine "break_short" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed exp_nblocks repeats of 'loop_exp'


# --- Prepare to start Routine "end_screen" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_end_screen.keys = []
key_resp_end_screen.rt = []
_key_resp_end_screen_allKeys = []
# keep track of which components have finished
end_screenComponents = [text_end_screen, key_resp_end_screen, image_end_screen]
for thisComponent in end_screenComponents:
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

# --- Run Routine "end_screen" ---
while continueRoutine and routineTimer.getTime() < 120.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_end_screen* updates
    if text_end_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_end_screen.frameNStart = frameN  # exact frame index
        text_end_screen.tStart = t  # local t and not account for scr refresh
        text_end_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_end_screen, 'tStartRefresh')  # time at next scr refresh
        text_end_screen.setAutoDraw(True)
    if text_end_screen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_end_screen.tStartRefresh + 120-frameTolerance:
            # keep track of stop time/frame for later
            text_end_screen.tStop = t  # not accounting for scr refresh
            text_end_screen.frameNStop = frameN  # exact frame index
            text_end_screen.setAutoDraw(False)
    
    # *key_resp_end_screen* updates
    waitOnFlip = False
    if key_resp_end_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_end_screen.frameNStart = frameN  # exact frame index
        key_resp_end_screen.tStart = t  # local t and not account for scr refresh
        key_resp_end_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_end_screen, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_end_screen.started')
        key_resp_end_screen.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_end_screen.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_end_screen.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_end_screen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_end_screen.tStartRefresh + 120-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_end_screen.tStop = t  # not accounting for scr refresh
            key_resp_end_screen.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_end_screen.stopped')
            key_resp_end_screen.status = FINISHED
    if key_resp_end_screen.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_end_screen.getKeys(keyList=['p'], waitRelease=False)
        _key_resp_end_screen_allKeys.extend(theseKeys)
        if len(_key_resp_end_screen_allKeys):
            key_resp_end_screen.keys = _key_resp_end_screen_allKeys[-1].name  # just the last key pressed
            key_resp_end_screen.rt = _key_resp_end_screen_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_end_screen* updates
    if image_end_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_end_screen.frameNStart = frameN  # exact frame index
        image_end_screen.tStart = t  # local t and not account for scr refresh
        image_end_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_end_screen, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_end_screen.started')
        image_end_screen.setAutoDraw(True)
    if image_end_screen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_end_screen.tStartRefresh + 120-frameTolerance:
            # keep track of stop time/frame for later
            image_end_screen.tStop = t  # not accounting for scr refresh
            image_end_screen.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_end_screen.stopped')
            image_end_screen.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end_screen" ---
for thisComponent in end_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_end_screen.keys in ['', [], None]:  # No response was made
    key_resp_end_screen.keys = None
thisExp.addData('key_resp_end_screen.keys',key_resp_end_screen.keys)
if key_resp_end_screen.keys != None:  # we had a response
    thisExp.addData('key_resp_end_screen.rt', key_resp_end_screen.rt)
thisExp.nextEntry()
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-120.000000)

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
