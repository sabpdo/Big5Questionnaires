#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on Fri Nov 13 13:35:05 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'Big5'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'sex': '', 'age': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
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
    originPath='/Users/sabrinado/Library/CELSYS/Big5/Big5_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='grey', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Big5Title"
Big5TitleClock = core.Clock()
IntroScreen = visual.TextStim(win=win, name='IntroScreen',
    text='Big 5 Test',
    font='Times New Roman',
    pos=(0, 0), height=0.10, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()
responseIndicator1 = visual.TextStim(win=win, name='responseIndicator1',
    text='Press any key to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='Spatial Anxiety Scale\n\nOn the next page, you will be presented a number of scenarios. Please rate your anxiety on the 5 point scale based off the scenario given. After selecting your rating by clicking on the scale, click once on the number below the scale to continue.',
    font='Times New Roman',
    pos=(0, 0), height=0.055, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()
responseIndicator2 = visual.TextStim(win=win, name='responseIndicator2',
    text='Press any key to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "SpatialAnxietyScale"
SpatialAnxietyScaleClock = core.Clock()
scenario1 = visual.TextStim(win=win, name='scenario1',
    text='default text',
    font='Times New Roman',
    pos=(0, 0.2), height=0.060, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
notAtAll = visual.TextStim(win=win, name='notAtAll',
    text='Not at All',
    font='Times New Roman',
    pos=(-0.40, -0.10), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
veryMuch = visual.TextStim(win=win, name='veryMuch',
    text='Very much',
    font='Times New Roman',
    pos=(0.40, -0.10), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.75, pos=[0.0, -0.4], low=1, high=5, labels=[''], scale='')

# Initialize components for Routine "SASEnd"
SASEndClock = core.Clock()
responseIndicator3 = visual.TextStim(win=win, name='responseIndicator3',
    text='Press any key to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()
SASendText = visual.TextStim(win=win, name='SASendText',
    text='You have finished this assessment.',
    font='Times New Roman',
    pos=(0, 0), height=0.080, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "RiskBehaviorStart"
RiskBehaviorStartClock = core.Clock()
RiskBehaviorScaleStartText = visual.TextStim(win=win, name='RiskBehaviorScaleStartText',
    text='You will now begin the Risk Behavior Scale assessment.',
    font='Times New Roman',
    pos=(0, 0), height=0.080, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
responseIndicator4 = visual.TextStim(win=win, name='responseIndicator4',
    text='Press any key to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "RBSInstr"
RBSInstrClock = core.Clock()
riskBehaviorInstrText = visual.TextStim(win=win, name='riskBehaviorInstrText',
    text='Risk Behavior Scale\n\nFor each of the statements, please indicate the likelihood of engaging in each activity. Provide a rating from 1 to 5, using the scale. After selecting your rating by clicking on the scale, click once on the number below the scale to continue.',
    font='Times New Roman',
    pos=(0, 0), height=0.060, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()
responseIndicator5 = visual.TextStim(win=win, name='responseIndicator5',
    text='Press any key to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "RBS"
RBSClock = core.Clock()
activity = visual.TextStim(win=win, name='activity',
    text='default text',
    font='Times New Roman',
    pos=(0, 0.2), height=0.060, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
extremelyUnlikely = visual.TextStim(win=win, name='extremelyUnlikely',
    text='Very unlikely',
    font='Times New Roman',
    pos=(-0.50, -0.1), height=0.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ExtremelyLikely = visual.TextStim(win=win, name='ExtremelyLikely',
    text='Very likely',
    font='Times New Roman',
    pos=(0.50, -0.1), height=0.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rating2 = visual.RatingScale(win=win, name='rating2', marker='triangle', size=2.0, pos=[0.0, -0.4], low=1, high=5, labels=[''], scale='')
unlikely = visual.TextStim(win=win, name='unlikely',
    text='Unlikely',
    font='Times New Roman',
    pos=(-0.25, -0.1), height=0.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
neutral = visual.TextStim(win=win, name='neutral',
    text='Not sure',
    font='Times New Roman',
    pos=(0, -0.1), height=0.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
Likely = visual.TextStim(win=win, name='Likely',
    text='Likely',
    font='Times New Roman',
    pos=(0.25, -0.1), height=0.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "RiskPerceptionStart"
RiskPerceptionStartClock = core.Clock()
riskPerceptionInstructions = visual.TextStim(win=win, name='riskPerceptionInstructions',
    text='People often see some risk in situations that contain uncertainty about what the outcome or consequences will be and for which there is the possibility of ‘bad’ consequences. However, riskiness is a very personal and intuitive notion, and we are interested in your gut level assessment of how risky each situation is. ',
    font='Times New Roman',
    pos=(0, 0), height=0.060, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()
responseIndicator6 = visual.TextStim(win=win, name='responseIndicator6',
    text='Press any key to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "RPInstr"
RPInstrClock = core.Clock()
riskPerceptionInstrText = visual.TextStim(win=win, name='riskPerceptionInstrText',
    text='For each of the following statements, please indicate how risky you perceive each situation. Provide a rating from 1 to 5 using the scale provided. After selecting your rating by clicking on the scale, click once on the number below the scale to continue.',
    font='Times New Roman',
    pos=(0, 0), height=0.060, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_11 = keyboard.Keyboard()
responseIndicator7 = visual.TextStim(win=win, name='responseIndicator7',
    text='Press any key to continue.',
    font='Times New Roman',
    pos=(0,-0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "RP"
RPClock = core.Clock()
riskPerceptionActivity2 = visual.TextStim(win=win, name='riskPerceptionActivity2',
    text='default text',
    font='Times New Roman',
    pos=(0, 0.2), height=0.060, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rating3 = visual.RatingScale(win=win, name='rating3', marker='triangle', size=1.75, pos=[0.0, -0.4], low=1, high=5, labels=[''], scale='')
notAtAllRisky = visual.TextStim(win=win, name='notAtAllRisky',
    text='Not at all risky',
    font='Times New Roman',
    pos=(-0.45, -0.1), height=0.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ModeratelyRisky = visual.TextStim(win=win, name='ModeratelyRisky',
    text='Moderately risky',
    font='Times New Roman',
    pos=(0, -0.1), height=0.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
ExtremelyRisky = visual.TextStim(win=win, name='ExtremelyRisky',
    text='Extremely risky',
    font='Times New Roman',
    pos=(0.45, -0.1), height=0.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "ExpectedBenefitsInstr"
ExpectedBenefitsInstrClock = core.Clock()
expBenefitsInstrText = visual.TextStim(win=win, name='expBenefitsInstrText',
    text='Expected Benefits Scale\n\nFor each of the following statements, please indicate the benefits you would obtain from each situation. Provide a rating from 1 to 5 using the scale. After selecting your rating by clicking on the scale, click once on the number below the scale to continue.',
    font='Times New Roman',
    pos=(0, 0), height=0.055, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()
responseIndicator8 = visual.TextStim(win=win, name='responseIndicator8',
    text='Press any key to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "EB"
EBClock = core.Clock()
riskBenefitsScale = visual.TextStim(win=win, name='riskBenefitsScale',
    text='default text',
    font='Times New Roman',
    pos=(0, 0.2), height=0.060, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
noBenefits = visual.TextStim(win=win, name='noBenefits',
    text='No benefits at all',
    font='Times New Roman',
    pos=(-0.45, -0.1), height=0.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating4 = visual.RatingScale(win=win, name='rating4', marker='triangle', size=1.75, pos=[0.0, -0.4], low=1, high=5, labels=[''], scale='')
greatBenefits = visual.TextStim(win=win, name='greatBenefits',
    text='Great benefits',
    font='Times New Roman',
    pos=(0.45, -0.1), height=0.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
moderateBenefits = visual.TextStim(win=win, name='moderateBenefits',
    text='Moderate benefits',
    font='Times New Roman',
    pos=(0, -0.1), height=0.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "finishedEB"
finishedEBClock = core.Clock()
end2 = visual.TextStim(win=win, name='end2',
    text='You have finished this assessment.',
    font='Times New Roman',
    pos=(0, 0), height=0.060, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_13 = keyboard.Keyboard()
responseIndicator9 = visual.TextStim(win=win, name='responseIndicator9',
    text='Press any key to continue. ',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "StartBig5"
StartBig5Clock = core.Clock()
Big5StartText = visual.TextStim(win=win, name='Big5StartText',
    text='You will now begin the Big 5 assessment.',
    font='Times New Roman',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_14 = keyboard.Keyboard()
responseIndicator10 = visual.TextStim(win=win, name='responseIndicator10',
    text='Press any key to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "B5Instr"
B5InstrClock = core.Clock()
Big5InstrText = visual.TextStim(win=win, name='Big5InstrText',
    text='The Big Five\n\nThe following slides will display a number of characteristics that may or may not apply to you. \n\nFor example, do you agree that you are someone who likes to spend time with others? ',
    font='Times New Roman',
    pos=(0, 0), height=0.060, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()
responseIndicator11 = visual.TextStim(win=win, name='responseIndicator11',
    text='Press any key to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "B5Instr2"
B5Instr2Clock = core.Clock()
Big5Instr2Text = visual.TextStim(win=win, name='Big5Instr2Text',
    text='Please click on a number on the scale to indicate the extent to which you agree or disagree with the statement. After clicking on the scale, press again on the number below the scale to continue.',
    font='Times New Roman',
    pos=(0, 0), height=0.070, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_12 = keyboard.Keyboard()
responseIndicator12 = visual.TextStim(win=win, name='responseIndicator12',
    text='Press any key to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "B5"
B5Clock = core.Clock()
rating5 = visual.RatingScale(win=win, name='rating5', marker='triangle', size=1.75, pos=[0.0, -0.4], low=1, high=5, labels=[''], scale='')
characText = visual.TextStim(win=win, name='characText',
    text='default text',
    font='Times New Roman',
    pos=(0, 0.2), height=0.060, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Someone = visual.TextStim(win=win, name='Someone',
    text='I am someone who…',
    font='Times New Roman',
    pos=(-0.40, 0.35), height=0.060, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
disagreeStrongly = visual.TextStim(win=win, name='disagreeStrongly',
    text='Disagree\nStrongly',
    font='Times New Roman',
    pos=(-0.40, -0.1), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
disagreeALittle = visual.TextStim(win=win, name='disagreeALittle',
    text='Disagree\na little',
    font='Times New Roman',
    pos=(-0.20, -0.1), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
Neutral = visual.TextStim(win=win, name='Neutral',
    text='Neutral;\nno opinion',
    font='Times New Roman',
    pos=(0, -0.1), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
AgreeALittle = visual.TextStim(win=win, name='AgreeALittle',
    text='Agree\na little',
    font='Times New Roman',
    pos=(0.20, -0.1), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
AgreeStrongly = visual.TextStim(win=win, name='AgreeStrongly',
    text='Agree\nstrongly',
    font='Times New Roman',
    pos=(0.40, -0.1), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "End"
EndClock = core.Clock()
End3 = visual.TextStim(win=win, name='End3',
    text='You have now completed the experiment.',
    font='Times New Roman',
    pos=(0, 0), height=0.080, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Big5Title"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
Big5TitleComponents = [IntroScreen, key_resp_3, responseIndicator1]
for thisComponent in Big5TitleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Big5TitleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Big5Title"-------
while continueRoutine:
    # get current time
    t = Big5TitleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Big5TitleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *IntroScreen* updates
    if IntroScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IntroScreen.frameNStart = frameN  # exact frame index
        IntroScreen.tStart = t  # local t and not account for scr refresh
        IntroScreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IntroScreen, 'tStartRefresh')  # time at next scr refresh
        IntroScreen.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=None, waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *responseIndicator1* updates
    if responseIndicator1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseIndicator1.frameNStart = frameN  # exact frame index
        responseIndicator1.tStart = t  # local t and not account for scr refresh
        responseIndicator1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseIndicator1, 'tStartRefresh')  # time at next scr refresh
        responseIndicator1.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Big5TitleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Big5Title"-------
for thisComponent in Big5TitleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('IntroScreen.started', IntroScreen.tStartRefresh)
thisExp.addData('IntroScreen.stopped', IntroScreen.tStopRefresh)
thisExp.addData('responseIndicator1.started', responseIndicator1.tStartRefresh)
thisExp.addData('responseIndicator1.stopped', responseIndicator1.tStopRefresh)
# the Routine "Big5Title" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
InstructionsComponents = [instructions, key_resp_2, responseIndicator2]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        instructions.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=None, waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *responseIndicator2* updates
    if responseIndicator2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseIndicator2.frameNStart = frameN  # exact frame index
        responseIndicator2.tStart = t  # local t and not account for scr refresh
        responseIndicator2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseIndicator2, 'tStartRefresh')  # time at next scr refresh
        responseIndicator2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions.started', instructions.tStartRefresh)
thisExp.addData('instructions.stopped', instructions.tStopRefresh)
thisExp.addData('responseIndicator2.started', responseIndicator2.tStartRefresh)
thisExp.addData('responseIndicator2.stopped', responseIndicator2.tStopRefresh)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('spatialAnxietyScale1.xlsx'),
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
    
    # ------Prepare to start Routine "SpatialAnxietyScale"-------
    continueRoutine = True
    # update component parameters for each repeat
    scenario1.setText(Scenario)
    rating.reset()
    # keep track of which components have finished
    SpatialAnxietyScaleComponents = [scenario1, notAtAll, veryMuch, rating]
    for thisComponent in SpatialAnxietyScaleComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SpatialAnxietyScaleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "SpatialAnxietyScale"-------
    while continueRoutine:
        # get current time
        t = SpatialAnxietyScaleClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SpatialAnxietyScaleClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *scenario1* updates
        if scenario1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            scenario1.frameNStart = frameN  # exact frame index
            scenario1.tStart = t  # local t and not account for scr refresh
            scenario1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(scenario1, 'tStartRefresh')  # time at next scr refresh
            scenario1.setAutoDraw(True)
        
        # *notAtAll* updates
        if notAtAll.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            notAtAll.frameNStart = frameN  # exact frame index
            notAtAll.tStart = t  # local t and not account for scr refresh
            notAtAll.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(notAtAll, 'tStartRefresh')  # time at next scr refresh
            notAtAll.setAutoDraw(True)
        
        # *veryMuch* updates
        if veryMuch.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            veryMuch.frameNStart = frameN  # exact frame index
            veryMuch.tStart = t  # local t and not account for scr refresh
            veryMuch.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(veryMuch, 'tStartRefresh')  # time at next scr refresh
            veryMuch.setAutoDraw(True)
        # *rating* updates
        if rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating.frameNStart = frameN  # exact frame index
            rating.tStart = t  # local t and not account for scr refresh
            rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SpatialAnxietyScaleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SpatialAnxietyScale"-------
    for thisComponent in SpatialAnxietyScaleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('scenario1.started', scenario1.tStartRefresh)
    trials.addData('scenario1.stopped', scenario1.tStopRefresh)
    trials.addData('notAtAll.started', notAtAll.tStartRefresh)
    trials.addData('notAtAll.stopped', notAtAll.tStopRefresh)
    trials.addData('veryMuch.started', veryMuch.tStartRefresh)
    trials.addData('veryMuch.stopped', veryMuch.tStopRefresh)
    thisExp.addData('lastRating', ((rating.markerPlacedAt*0.20)))
    
    # store data for trials (TrialHandler)
    trials.addData('rating.response', rating.getRating())
    trials.addData('rating.rt', rating.getRT())
    trials.addData('rating.started', rating.tStart)
    trials.addData('rating.stopped', rating.tStop)
    # the Routine "SpatialAnxietyScale" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "SASEnd"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
SASEndComponents = [responseIndicator3, key_resp_9, SASendText]
for thisComponent in SASEndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SASEndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "SASEnd"-------
while continueRoutine:
    # get current time
    t = SASEndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SASEndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *responseIndicator3* updates
    if responseIndicator3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseIndicator3.frameNStart = frameN  # exact frame index
        responseIndicator3.tStart = t  # local t and not account for scr refresh
        responseIndicator3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseIndicator3, 'tStartRefresh')  # time at next scr refresh
        responseIndicator3.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=None, waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *SASendText* updates
    if SASendText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SASendText.frameNStart = frameN  # exact frame index
        SASendText.tStart = t  # local t and not account for scr refresh
        SASendText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SASendText, 'tStartRefresh')  # time at next scr refresh
        SASendText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SASEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SASEnd"-------
for thisComponent in SASEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('responseIndicator3.started', responseIndicator3.tStartRefresh)
thisExp.addData('responseIndicator3.stopped', responseIndicator3.tStopRefresh)
thisExp.addData('SASendText.started', SASendText.tStartRefresh)
thisExp.addData('SASendText.stopped', SASendText.tStopRefresh)
# the Routine "SASEnd" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "RiskBehaviorStart"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
RiskBehaviorStartComponents = [RiskBehaviorScaleStartText, responseIndicator4, key_resp_10]
for thisComponent in RiskBehaviorStartComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
RiskBehaviorStartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "RiskBehaviorStart"-------
while continueRoutine:
    # get current time
    t = RiskBehaviorStartClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=RiskBehaviorStartClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *RiskBehaviorScaleStartText* updates
    if RiskBehaviorScaleStartText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RiskBehaviorScaleStartText.frameNStart = frameN  # exact frame index
        RiskBehaviorScaleStartText.tStart = t  # local t and not account for scr refresh
        RiskBehaviorScaleStartText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RiskBehaviorScaleStartText, 'tStartRefresh')  # time at next scr refresh
        RiskBehaviorScaleStartText.setAutoDraw(True)
    
    # *responseIndicator4* updates
    if responseIndicator4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseIndicator4.frameNStart = frameN  # exact frame index
        responseIndicator4.tStart = t  # local t and not account for scr refresh
        responseIndicator4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseIndicator4, 'tStartRefresh')  # time at next scr refresh
        responseIndicator4.setAutoDraw(True)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=None, waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RiskBehaviorStartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "RiskBehaviorStart"-------
for thisComponent in RiskBehaviorStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('RiskBehaviorScaleStartText.started', RiskBehaviorScaleStartText.tStartRefresh)
thisExp.addData('RiskBehaviorScaleStartText.stopped', RiskBehaviorScaleStartText.tStopRefresh)
thisExp.addData('responseIndicator4.started', responseIndicator4.tStartRefresh)
thisExp.addData('responseIndicator4.stopped', responseIndicator4.tStopRefresh)
# the Routine "RiskBehaviorStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "RBSInstr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
RBSInstrComponents = [riskBehaviorInstrText, key_resp_4, responseIndicator5]
for thisComponent in RBSInstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
RBSInstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "RBSInstr"-------
while continueRoutine:
    # get current time
    t = RBSInstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=RBSInstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *riskBehaviorInstrText* updates
    if riskBehaviorInstrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        riskBehaviorInstrText.frameNStart = frameN  # exact frame index
        riskBehaviorInstrText.tStart = t  # local t and not account for scr refresh
        riskBehaviorInstrText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(riskBehaviorInstrText, 'tStartRefresh')  # time at next scr refresh
        riskBehaviorInstrText.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=None, waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *responseIndicator5* updates
    if responseIndicator5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseIndicator5.frameNStart = frameN  # exact frame index
        responseIndicator5.tStart = t  # local t and not account for scr refresh
        responseIndicator5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseIndicator5, 'tStartRefresh')  # time at next scr refresh
        responseIndicator5.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RBSInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "RBSInstr"-------
for thisComponent in RBSInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('riskBehaviorInstrText.started', riskBehaviorInstrText.tStartRefresh)
thisExp.addData('riskBehaviorInstrText.stopped', riskBehaviorInstrText.tStopRefresh)
thisExp.addData('responseIndicator5.started', responseIndicator5.tStartRefresh)
thisExp.addData('responseIndicator5.stopped', responseIndicator5.tStopRefresh)
# the Routine "RBSInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('activities.xlsx'),
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
    
    # ------Prepare to start Routine "RBS"-------
    continueRoutine = True
    # update component parameters for each repeat
    activity.setText(C)
    rating2.reset()
    # keep track of which components have finished
    RBSComponents = [activity, extremelyUnlikely, ExtremelyLikely, rating2, unlikely, neutral, Likely]
    for thisComponent in RBSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RBSClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "RBS"-------
    while continueRoutine:
        # get current time
        t = RBSClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RBSClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *activity* updates
        if activity.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            activity.frameNStart = frameN  # exact frame index
            activity.tStart = t  # local t and not account for scr refresh
            activity.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(activity, 'tStartRefresh')  # time at next scr refresh
            activity.setAutoDraw(True)
        
        # *extremelyUnlikely* updates
        if extremelyUnlikely.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            extremelyUnlikely.frameNStart = frameN  # exact frame index
            extremelyUnlikely.tStart = t  # local t and not account for scr refresh
            extremelyUnlikely.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(extremelyUnlikely, 'tStartRefresh')  # time at next scr refresh
            extremelyUnlikely.setAutoDraw(True)
        
        # *ExtremelyLikely* updates
        if ExtremelyLikely.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ExtremelyLikely.frameNStart = frameN  # exact frame index
            ExtremelyLikely.tStart = t  # local t and not account for scr refresh
            ExtremelyLikely.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExtremelyLikely, 'tStartRefresh')  # time at next scr refresh
            ExtremelyLikely.setAutoDraw(True)
        # *rating2* updates
        if rating2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating2.frameNStart = frameN  # exact frame index
            rating2.tStart = t  # local t and not account for scr refresh
            rating2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating2, 'tStartRefresh')  # time at next scr refresh
            rating2.setAutoDraw(True)
        continueRoutine &= rating2.noResponse  # a response ends the trial
        
        # *unlikely* updates
        if unlikely.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            unlikely.frameNStart = frameN  # exact frame index
            unlikely.tStart = t  # local t and not account for scr refresh
            unlikely.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(unlikely, 'tStartRefresh')  # time at next scr refresh
            unlikely.setAutoDraw(True)
        
        # *neutral* updates
        if neutral.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            neutral.frameNStart = frameN  # exact frame index
            neutral.tStart = t  # local t and not account for scr refresh
            neutral.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(neutral, 'tStartRefresh')  # time at next scr refresh
            neutral.setAutoDraw(True)
        
        # *Likely* updates
        if Likely.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Likely.frameNStart = frameN  # exact frame index
            Likely.tStart = t  # local t and not account for scr refresh
            Likely.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Likely, 'tStartRefresh')  # time at next scr refresh
            Likely.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RBSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "RBS"-------
    for thisComponent in RBSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('activity.started', activity.tStartRefresh)
    trials_2.addData('activity.stopped', activity.tStopRefresh)
    trials_2.addData('extremelyUnlikely.started', extremelyUnlikely.tStartRefresh)
    trials_2.addData('extremelyUnlikely.stopped', extremelyUnlikely.tStopRefresh)
    trials_2.addData('ExtremelyLikely.started', ExtremelyLikely.tStartRefresh)
    trials_2.addData('ExtremelyLikely.stopped', ExtremelyLikely.tStopRefresh)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('rating2.response', rating2.getRating())
    trials_2.addData('rating2.rt', rating2.getRT())
    trials_2.addData('rating2.started', rating2.tStart)
    trials_2.addData('rating2.stopped', rating2.tStop)
    thisExp.addData('Rating', rating2.markerPlacedAt)
    trials_2.addData('unlikely.started', unlikely.tStartRefresh)
    trials_2.addData('unlikely.stopped', unlikely.tStopRefresh)
    trials_2.addData('neutral.started', neutral.tStartRefresh)
    trials_2.addData('neutral.stopped', neutral.tStopRefresh)
    trials_2.addData('Likely.started', Likely.tStartRefresh)
    trials_2.addData('Likely.stopped', Likely.tStopRefresh)
    # the Routine "RBS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "RiskPerceptionStart"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
RiskPerceptionStartComponents = [riskPerceptionInstructions, key_resp_5, responseIndicator6]
for thisComponent in RiskPerceptionStartComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
RiskPerceptionStartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "RiskPerceptionStart"-------
while continueRoutine:
    # get current time
    t = RiskPerceptionStartClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=RiskPerceptionStartClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *riskPerceptionInstructions* updates
    if riskPerceptionInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        riskPerceptionInstructions.frameNStart = frameN  # exact frame index
        riskPerceptionInstructions.tStart = t  # local t and not account for scr refresh
        riskPerceptionInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(riskPerceptionInstructions, 'tStartRefresh')  # time at next scr refresh
        riskPerceptionInstructions.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=None, waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *responseIndicator6* updates
    if responseIndicator6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseIndicator6.frameNStart = frameN  # exact frame index
        responseIndicator6.tStart = t  # local t and not account for scr refresh
        responseIndicator6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseIndicator6, 'tStartRefresh')  # time at next scr refresh
        responseIndicator6.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RiskPerceptionStartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "RiskPerceptionStart"-------
for thisComponent in RiskPerceptionStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('riskPerceptionInstructions.started', riskPerceptionInstructions.tStartRefresh)
thisExp.addData('riskPerceptionInstructions.stopped', riskPerceptionInstructions.tStopRefresh)
thisExp.addData('responseIndicator6.started', responseIndicator6.tStartRefresh)
thisExp.addData('responseIndicator6.stopped', responseIndicator6.tStopRefresh)
# the Routine "RiskPerceptionStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "RPInstr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_11.keys = []
key_resp_11.rt = []
_key_resp_11_allKeys = []
# keep track of which components have finished
RPInstrComponents = [riskPerceptionInstrText, key_resp_11, responseIndicator7]
for thisComponent in RPInstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
RPInstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "RPInstr"-------
while continueRoutine:
    # get current time
    t = RPInstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=RPInstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *riskPerceptionInstrText* updates
    if riskPerceptionInstrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        riskPerceptionInstrText.frameNStart = frameN  # exact frame index
        riskPerceptionInstrText.tStart = t  # local t and not account for scr refresh
        riskPerceptionInstrText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(riskPerceptionInstrText, 'tStartRefresh')  # time at next scr refresh
        riskPerceptionInstrText.setAutoDraw(True)
    
    # *key_resp_11* updates
    waitOnFlip = False
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_11.getKeys(keyList=None, waitRelease=False)
        _key_resp_11_allKeys.extend(theseKeys)
        if len(_key_resp_11_allKeys):
            key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
            key_resp_11.rt = _key_resp_11_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *responseIndicator7* updates
    if responseIndicator7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseIndicator7.frameNStart = frameN  # exact frame index
        responseIndicator7.tStart = t  # local t and not account for scr refresh
        responseIndicator7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseIndicator7, 'tStartRefresh')  # time at next scr refresh
        responseIndicator7.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RPInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "RPInstr"-------
for thisComponent in RPInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('riskPerceptionInstrText.started', riskPerceptionInstrText.tStartRefresh)
thisExp.addData('riskPerceptionInstrText.stopped', riskPerceptionInstrText.tStopRefresh)
thisExp.addData('responseIndicator7.started', responseIndicator7.tStartRefresh)
thisExp.addData('responseIndicator7.stopped', responseIndicator7.tStopRefresh)
# the Routine "RPInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('activities.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "RP"-------
    continueRoutine = True
    # update component parameters for each repeat
    riskPerceptionActivity2.setText(C)
    rating3.reset()
    # keep track of which components have finished
    RPComponents = [riskPerceptionActivity2, rating3, notAtAllRisky, ModeratelyRisky, ExtremelyRisky]
    for thisComponent in RPComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RPClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "RP"-------
    while continueRoutine:
        # get current time
        t = RPClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RPClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *riskPerceptionActivity2* updates
        if riskPerceptionActivity2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            riskPerceptionActivity2.frameNStart = frameN  # exact frame index
            riskPerceptionActivity2.tStart = t  # local t and not account for scr refresh
            riskPerceptionActivity2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(riskPerceptionActivity2, 'tStartRefresh')  # time at next scr refresh
            riskPerceptionActivity2.setAutoDraw(True)
        # *rating3* updates
        if rating3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating3.frameNStart = frameN  # exact frame index
            rating3.tStart = t  # local t and not account for scr refresh
            rating3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating3, 'tStartRefresh')  # time at next scr refresh
            rating3.setAutoDraw(True)
        continueRoutine &= rating3.noResponse  # a response ends the trial
        
        # *notAtAllRisky* updates
        if notAtAllRisky.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            notAtAllRisky.frameNStart = frameN  # exact frame index
            notAtAllRisky.tStart = t  # local t and not account for scr refresh
            notAtAllRisky.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(notAtAllRisky, 'tStartRefresh')  # time at next scr refresh
            notAtAllRisky.setAutoDraw(True)
        
        # *ModeratelyRisky* updates
        if ModeratelyRisky.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ModeratelyRisky.frameNStart = frameN  # exact frame index
            ModeratelyRisky.tStart = t  # local t and not account for scr refresh
            ModeratelyRisky.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ModeratelyRisky, 'tStartRefresh')  # time at next scr refresh
            ModeratelyRisky.setAutoDraw(True)
        
        # *ExtremelyRisky* updates
        if ExtremelyRisky.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ExtremelyRisky.frameNStart = frameN  # exact frame index
            ExtremelyRisky.tStart = t  # local t and not account for scr refresh
            ExtremelyRisky.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExtremelyRisky, 'tStartRefresh')  # time at next scr refresh
            ExtremelyRisky.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RPComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "RP"-------
    for thisComponent in RPComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('riskPerceptionActivity2.started', riskPerceptionActivity2.tStartRefresh)
    trials_3.addData('riskPerceptionActivity2.stopped', riskPerceptionActivity2.tStopRefresh)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('rating3.response', rating3.getRating())
    trials_3.addData('rating3.rt', rating3.getRT())
    trials_3.addData('rating3.started', rating3.tStart)
    trials_3.addData('rating3.stopped', rating3.tStop)
    trials_3.addData('notAtAllRisky.started', notAtAllRisky.tStartRefresh)
    trials_3.addData('notAtAllRisky.stopped', notAtAllRisky.tStopRefresh)
    trials_3.addData('ModeratelyRisky.started', ModeratelyRisky.tStartRefresh)
    trials_3.addData('ModeratelyRisky.stopped', ModeratelyRisky.tStopRefresh)
    trials_3.addData('ExtremelyRisky.started', ExtremelyRisky.tStartRefresh)
    trials_3.addData('ExtremelyRisky.stopped', ExtremelyRisky.tStopRefresh)
    thisExp.addData('lastRating', rating3.markerPlacedAt*0.20)
    # the Routine "RP" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


# ------Prepare to start Routine "ExpectedBenefitsInstr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
ExpectedBenefitsInstrComponents = [expBenefitsInstrText, key_resp_6, responseIndicator8]
for thisComponent in ExpectedBenefitsInstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ExpectedBenefitsInstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ExpectedBenefitsInstr"-------
while continueRoutine:
    # get current time
    t = ExpectedBenefitsInstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ExpectedBenefitsInstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *expBenefitsInstrText* updates
    if expBenefitsInstrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        expBenefitsInstrText.frameNStart = frameN  # exact frame index
        expBenefitsInstrText.tStart = t  # local t and not account for scr refresh
        expBenefitsInstrText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(expBenefitsInstrText, 'tStartRefresh')  # time at next scr refresh
        expBenefitsInstrText.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=None, waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *responseIndicator8* updates
    if responseIndicator8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseIndicator8.frameNStart = frameN  # exact frame index
        responseIndicator8.tStart = t  # local t and not account for scr refresh
        responseIndicator8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseIndicator8, 'tStartRefresh')  # time at next scr refresh
        responseIndicator8.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ExpectedBenefitsInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ExpectedBenefitsInstr"-------
for thisComponent in ExpectedBenefitsInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('expBenefitsInstrText.started', expBenefitsInstrText.tStartRefresh)
thisExp.addData('expBenefitsInstrText.stopped', expBenefitsInstrText.tStopRefresh)
thisExp.addData('responseIndicator8.started', responseIndicator8.tStartRefresh)
thisExp.addData('responseIndicator8.stopped', responseIndicator8.tStopRefresh)
# the Routine "ExpectedBenefitsInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('activities.xlsx'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "EB"-------
    continueRoutine = True
    # update component parameters for each repeat
    riskBenefitsScale.setText(C)
    rating4.reset()
    # keep track of which components have finished
    EBComponents = [riskBenefitsScale, noBenefits, rating4, greatBenefits, moderateBenefits]
    for thisComponent in EBComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    EBClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "EB"-------
    while continueRoutine:
        # get current time
        t = EBClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=EBClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *riskBenefitsScale* updates
        if riskBenefitsScale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            riskBenefitsScale.frameNStart = frameN  # exact frame index
            riskBenefitsScale.tStart = t  # local t and not account for scr refresh
            riskBenefitsScale.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(riskBenefitsScale, 'tStartRefresh')  # time at next scr refresh
            riskBenefitsScale.setAutoDraw(True)
        
        # *noBenefits* updates
        if noBenefits.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            noBenefits.frameNStart = frameN  # exact frame index
            noBenefits.tStart = t  # local t and not account for scr refresh
            noBenefits.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noBenefits, 'tStartRefresh')  # time at next scr refresh
            noBenefits.setAutoDraw(True)
        # *rating4* updates
        if rating4.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating4.frameNStart = frameN  # exact frame index
            rating4.tStart = t  # local t and not account for scr refresh
            rating4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating4, 'tStartRefresh')  # time at next scr refresh
            rating4.setAutoDraw(True)
        continueRoutine &= rating4.noResponse  # a response ends the trial
        
        # *greatBenefits* updates
        if greatBenefits.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greatBenefits.frameNStart = frameN  # exact frame index
            greatBenefits.tStart = t  # local t and not account for scr refresh
            greatBenefits.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greatBenefits, 'tStartRefresh')  # time at next scr refresh
            greatBenefits.setAutoDraw(True)
        
        # *moderateBenefits* updates
        if moderateBenefits.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            moderateBenefits.frameNStart = frameN  # exact frame index
            moderateBenefits.tStart = t  # local t and not account for scr refresh
            moderateBenefits.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(moderateBenefits, 'tStartRefresh')  # time at next scr refresh
            moderateBenefits.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EBComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "EB"-------
    for thisComponent in EBComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_4.addData('riskBenefitsScale.started', riskBenefitsScale.tStartRefresh)
    trials_4.addData('riskBenefitsScale.stopped', riskBenefitsScale.tStopRefresh)
    trials_4.addData('noBenefits.started', noBenefits.tStartRefresh)
    trials_4.addData('noBenefits.stopped', noBenefits.tStopRefresh)
    # store data for trials_4 (TrialHandler)
    trials_4.addData('rating4.response', rating4.getRating())
    trials_4.addData('rating4.rt', rating4.getRT())
    trials_4.addData('rating4.started', rating4.tStart)
    trials_4.addData('rating4.stopped', rating4.tStop)
    trials_4.addData('greatBenefits.started', greatBenefits.tStartRefresh)
    trials_4.addData('greatBenefits.stopped', greatBenefits.tStopRefresh)
    trials_4.addData('moderateBenefits.started', moderateBenefits.tStartRefresh)
    trials_4.addData('moderateBenefits.stopped', moderateBenefits.tStopRefresh)
    thisExp.addData('lastRating', rating4.markerPlacedAt)
    # the Routine "EB" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_4'


# ------Prepare to start Routine "finishedEB"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_13.keys = []
key_resp_13.rt = []
_key_resp_13_allKeys = []
# keep track of which components have finished
finishedEBComponents = [end2, key_resp_13, responseIndicator9]
for thisComponent in finishedEBComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finishedEBClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "finishedEB"-------
while continueRoutine:
    # get current time
    t = finishedEBClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finishedEBClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end2* updates
    if end2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end2.frameNStart = frameN  # exact frame index
        end2.tStart = t  # local t and not account for scr refresh
        end2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end2, 'tStartRefresh')  # time at next scr refresh
        end2.setAutoDraw(True)
    
    # *key_resp_13* updates
    waitOnFlip = False
    if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.tStart = t  # local t and not account for scr refresh
        key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_13.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_13.getKeys(keyList=None, waitRelease=False)
        _key_resp_13_allKeys.extend(theseKeys)
        if len(_key_resp_13_allKeys):
            key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
            key_resp_13.rt = _key_resp_13_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *responseIndicator9* updates
    if responseIndicator9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseIndicator9.frameNStart = frameN  # exact frame index
        responseIndicator9.tStart = t  # local t and not account for scr refresh
        responseIndicator9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseIndicator9, 'tStartRefresh')  # time at next scr refresh
        responseIndicator9.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishedEBComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "finishedEB"-------
for thisComponent in finishedEBComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end2.started', end2.tStartRefresh)
thisExp.addData('end2.stopped', end2.tStopRefresh)
thisExp.addData('responseIndicator9.started', responseIndicator9.tStartRefresh)
thisExp.addData('responseIndicator9.stopped', responseIndicator9.tStopRefresh)
# the Routine "finishedEB" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "StartBig5"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_14.keys = []
key_resp_14.rt = []
_key_resp_14_allKeys = []
# keep track of which components have finished
StartBig5Components = [Big5StartText, key_resp_14, responseIndicator10]
for thisComponent in StartBig5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartBig5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "StartBig5"-------
while continueRoutine:
    # get current time
    t = StartBig5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartBig5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Big5StartText* updates
    if Big5StartText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Big5StartText.frameNStart = frameN  # exact frame index
        Big5StartText.tStart = t  # local t and not account for scr refresh
        Big5StartText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Big5StartText, 'tStartRefresh')  # time at next scr refresh
        Big5StartText.setAutoDraw(True)
    
    # *key_resp_14* updates
    waitOnFlip = False
    if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.tStart = t  # local t and not account for scr refresh
        key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_14.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_14.getKeys(keyList=None, waitRelease=False)
        _key_resp_14_allKeys.extend(theseKeys)
        if len(_key_resp_14_allKeys):
            key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
            key_resp_14.rt = _key_resp_14_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *responseIndicator10* updates
    if responseIndicator10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseIndicator10.frameNStart = frameN  # exact frame index
        responseIndicator10.tStart = t  # local t and not account for scr refresh
        responseIndicator10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseIndicator10, 'tStartRefresh')  # time at next scr refresh
        responseIndicator10.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartBig5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StartBig5"-------
for thisComponent in StartBig5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Big5StartText.started', Big5StartText.tStartRefresh)
thisExp.addData('Big5StartText.stopped', Big5StartText.tStopRefresh)
thisExp.addData('responseIndicator10.started', responseIndicator10.tStartRefresh)
thisExp.addData('responseIndicator10.stopped', responseIndicator10.tStopRefresh)
# the Routine "StartBig5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "B5Instr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
B5InstrComponents = [Big5InstrText, key_resp_7, responseIndicator11]
for thisComponent in B5InstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
B5InstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "B5Instr"-------
while continueRoutine:
    # get current time
    t = B5InstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=B5InstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Big5InstrText* updates
    if Big5InstrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Big5InstrText.frameNStart = frameN  # exact frame index
        Big5InstrText.tStart = t  # local t and not account for scr refresh
        Big5InstrText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Big5InstrText, 'tStartRefresh')  # time at next scr refresh
        Big5InstrText.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=None, waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *responseIndicator11* updates
    if responseIndicator11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseIndicator11.frameNStart = frameN  # exact frame index
        responseIndicator11.tStart = t  # local t and not account for scr refresh
        responseIndicator11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseIndicator11, 'tStartRefresh')  # time at next scr refresh
        responseIndicator11.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in B5InstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "B5Instr"-------
for thisComponent in B5InstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Big5InstrText.started', Big5InstrText.tStartRefresh)
thisExp.addData('Big5InstrText.stopped', Big5InstrText.tStopRefresh)
thisExp.addData('responseIndicator11.started', responseIndicator11.tStartRefresh)
thisExp.addData('responseIndicator11.stopped', responseIndicator11.tStopRefresh)
# the Routine "B5Instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "B5Instr2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
# keep track of which components have finished
B5Instr2Components = [Big5Instr2Text, key_resp_12, responseIndicator12]
for thisComponent in B5Instr2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
B5Instr2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "B5Instr2"-------
while continueRoutine:
    # get current time
    t = B5Instr2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=B5Instr2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Big5Instr2Text* updates
    if Big5Instr2Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Big5Instr2Text.frameNStart = frameN  # exact frame index
        Big5Instr2Text.tStart = t  # local t and not account for scr refresh
        Big5Instr2Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Big5Instr2Text, 'tStartRefresh')  # time at next scr refresh
        Big5Instr2Text.setAutoDraw(True)
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=None, waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *responseIndicator12* updates
    if responseIndicator12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseIndicator12.frameNStart = frameN  # exact frame index
        responseIndicator12.tStart = t  # local t and not account for scr refresh
        responseIndicator12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseIndicator12, 'tStartRefresh')  # time at next scr refresh
        responseIndicator12.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in B5Instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "B5Instr2"-------
for thisComponent in B5Instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Big5Instr2Text.started', Big5Instr2Text.tStartRefresh)
thisExp.addData('Big5Instr2Text.stopped', Big5Instr2Text.tStopRefresh)
thisExp.addData('responseIndicator12.started', responseIndicator12.tStartRefresh)
thisExp.addData('responseIndicator12.stopped', responseIndicator12.tStopRefresh)
# the Routine "B5Instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('charac.xlsx'),
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5:
        exec('{} = thisTrial_5[paramName]'.format(paramName))

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "B5"-------
    continueRoutine = True
    # update component parameters for each repeat
    rating5.reset()
    characText.setText(Charac)
    # keep track of which components have finished
    B5Components = [rating5, characText, Someone, disagreeStrongly, disagreeALittle, Neutral, AgreeALittle, AgreeStrongly]
    for thisComponent in B5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    B5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "B5"-------
    while continueRoutine:
        # get current time
        t = B5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=B5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *rating5* updates
        if rating5.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating5.frameNStart = frameN  # exact frame index
            rating5.tStart = t  # local t and not account for scr refresh
            rating5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating5, 'tStartRefresh')  # time at next scr refresh
            rating5.setAutoDraw(True)
        continueRoutine &= rating5.noResponse  # a response ends the trial
        
        # *characText* updates
        if characText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            characText.frameNStart = frameN  # exact frame index
            characText.tStart = t  # local t and not account for scr refresh
            characText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(characText, 'tStartRefresh')  # time at next scr refresh
            characText.setAutoDraw(True)
        
        # *Someone* updates
        if Someone.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Someone.frameNStart = frameN  # exact frame index
            Someone.tStart = t  # local t and not account for scr refresh
            Someone.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Someone, 'tStartRefresh')  # time at next scr refresh
            Someone.setAutoDraw(True)
        
        # *disagreeStrongly* updates
        if disagreeStrongly.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            disagreeStrongly.frameNStart = frameN  # exact frame index
            disagreeStrongly.tStart = t  # local t and not account for scr refresh
            disagreeStrongly.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(disagreeStrongly, 'tStartRefresh')  # time at next scr refresh
            disagreeStrongly.setAutoDraw(True)
        
        # *disagreeALittle* updates
        if disagreeALittle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            disagreeALittle.frameNStart = frameN  # exact frame index
            disagreeALittle.tStart = t  # local t and not account for scr refresh
            disagreeALittle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(disagreeALittle, 'tStartRefresh')  # time at next scr refresh
            disagreeALittle.setAutoDraw(True)
        
        # *Neutral* updates
        if Neutral.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Neutral.frameNStart = frameN  # exact frame index
            Neutral.tStart = t  # local t and not account for scr refresh
            Neutral.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Neutral, 'tStartRefresh')  # time at next scr refresh
            Neutral.setAutoDraw(True)
        
        # *AgreeALittle* updates
        if AgreeALittle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AgreeALittle.frameNStart = frameN  # exact frame index
            AgreeALittle.tStart = t  # local t and not account for scr refresh
            AgreeALittle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AgreeALittle, 'tStartRefresh')  # time at next scr refresh
            AgreeALittle.setAutoDraw(True)
        
        # *AgreeStrongly* updates
        if AgreeStrongly.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AgreeStrongly.frameNStart = frameN  # exact frame index
            AgreeStrongly.tStart = t  # local t and not account for scr refresh
            AgreeStrongly.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AgreeStrongly, 'tStartRefresh')  # time at next scr refresh
            AgreeStrongly.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in B5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "B5"-------
    for thisComponent in B5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_5 (TrialHandler)
    trials_5.addData('rating5.response', rating5.getRating())
    trials_5.addData('rating5.rt', rating5.getRT())
    trials_5.addData('rating5.started', rating5.tStart)
    trials_5.addData('rating5.stopped', rating5.tStop)
    trials_5.addData('characText.started', characText.tStartRefresh)
    trials_5.addData('characText.stopped', characText.tStopRefresh)
    trials_5.addData('Someone.started', Someone.tStartRefresh)
    trials_5.addData('Someone.stopped', Someone.tStopRefresh)
    trials_5.addData('disagreeStrongly.started', disagreeStrongly.tStartRefresh)
    trials_5.addData('disagreeStrongly.stopped', disagreeStrongly.tStopRefresh)
    trials_5.addData('disagreeALittle.started', disagreeALittle.tStartRefresh)
    trials_5.addData('disagreeALittle.stopped', disagreeALittle.tStopRefresh)
    trials_5.addData('Neutral.started', Neutral.tStartRefresh)
    trials_5.addData('Neutral.stopped', Neutral.tStopRefresh)
    trials_5.addData('AgreeALittle.started', AgreeALittle.tStartRefresh)
    trials_5.addData('AgreeALittle.stopped', AgreeALittle.tStopRefresh)
    trials_5.addData('AgreeStrongly.started', AgreeStrongly.tStartRefresh)
    trials_5.addData('AgreeStrongly.stopped', AgreeStrongly.tStopRefresh)
    thisExp.addData('lastRating', rating5.markerPlacedAt)
    # the Routine "B5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_5'


# ------Prepare to start Routine "End"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
EndComponents = [End3, key_resp_8]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *End3* updates
    if End3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        End3.frameNStart = frameN  # exact frame index
        End3.tStart = t  # local t and not account for scr refresh
        End3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(End3, 'tStartRefresh')  # time at next scr refresh
        End3.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=None, waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('End3.started', End3.tStartRefresh)
thisExp.addData('End3.stopped', End3.tStopRefresh)
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
