V2.0
- Updated the RandomFull file (both arms/both hards) > Right/Left side arms/hands) The both hands file was bugging out mostly due to I wasn't updating that file. :9
- Updated the main image with the sleep(0.1) is your friend info which will help you elimate strange movements if and when that happens. 
- Updated the random movement....movements for better ...movements. :D
- Updated the gesture stop files with velocity/speed settings in them so you don't have to readjust those after every randomstop used. 
- Updated strange audio file only bug info on this document.
-----------------------------------------------------------
HOW TO INSTALL CUSTOM RANDOM MOVEMENTS IN YOUR INMOOV ROBOT
-----------------------------------------------------------

1) - Open your InMoov folder and drag your "life" folder onto your desktop or somewhere safe as a backup while you test these. It will be removed from the folder.

2) - Copy the "life" folder from within this file into your InMoov folder.

3) - Open your InMoov/config folder and copy/move InMoovLife.config to save place. 

4) - With InMoovLife.config removed, Open the "config" folder from within this file and copy the new InMoovLife.config to the same location.

5) - Open the "gestures" folder from within this file and copy the files into your "InMoov/gestures" folder.
-----------------------------------------------------------------------------------------------------------
You should now be good to go! But perhaps reading the stuff below will help you understand when and how to use them. :)

- I believe the tabs will only show up in your MRL if you have those parts enabled for the robot. Otherwise they will show up when you have those parts enabled. :9

------------------------------------------------------------------------------------------
USING RANDOMIZATION - Python commands to use in gesture files or in the python tab in MRL.
------------------------------------------------------------------------------------------

- randomneck()   #Moves the neck randomly (Neck/Rotneck/Rollneck)
- randomneckstop()   #Stops the neck from moving randomly (Neck/Rotneck/Rollneck)

- randomlook()   #Moves the eyes randomly (EyeX/EyeY)
- randomlookstop()   #Stops the eyes from moving randomly (EyeX/EyeY)

- randomfullhead()   #Moves the fullhead randomly (This is just a bonus for lazy people: It is a combo of the above two.)       
- randomfullheadstop()    #Stops the full head from moving randomly. 

- randomarms() #Moves both arms randomly (bicep/rotate/omniplate)
- randomarmsstop() #Stops both arms from moving randomly.(bicep/rotate/omniplate)

- randomleftarm() #Moves the left arm randomly (bicep/rotate/omniplate)
- randomleftarmstop() #Stops the left arm from moving randomly.(bicep/rotate/omniplate)

- randomrightarm() #Moves the right arm randomly (bicep/rotate/omniplate)
- randomrightarmstop() #Stops the right arm from moving randomly.(bicep/rotate/omniplate)

- randomhands() #Moves both hands randomly (Thumb/Index/Majeure/Ring/Pinky/Wrist)
- randomhandsstop() #Stops both hands from moving randomly.    (Thumb/Index/Majeure/Ring/Pinky/Wrist)

- randomlefthand() #Moves the left hand randomly (Thumb/Index/Majeure/Ring/Pinky/Wrist)
- randomlefthandstop() #Stops the left hand from moving randomly.    (Thumb/Index/Majeure/Ring/Pinky/Wrist)

- randomrighthand() #Moves the right hand randomly (Thumb/Index/Majeure/Ring/Pinky/Wrist)
- randomrighthandstop() #Stops the right hand from moving randomly.    (Thumb/Index/Majeure/Ring/Pinky/Wrist)

- randomstomach() #Moves the stomach randomly (TopStom/MidStom)
- randomstomachstop() #Stops the stomach from moving randomly. (TopStom/MidStom)

- randomfull() #Moves the FULL robot randomly. (EVERYTHING!)
- randomfullstop() #Stops the full robot from moving randomly (EVERYTHING!)

----
TIPS
----
- Look at the RandomLife.jpg image file included to help understand how you can adjust and tune your random settings. 

- Play with the figures in the life folder files until you feel you have achieved the natural movement results you are wanting. Remember my settings are not perfect! If you get better results... please share them with me! XD

---------------
OTHER TAB INFO.
---------------
"MoveEyesTimer" and "MoveHeadTimer" looks odd being there. Those are Gael's original files which I left untouch due to I'm not sure just how tied into other services they are. I really don't want to dig through every file to find out. :D

"FullHeadRandom" really isn't needed as it is just a combo of "LookRandom" and "NeckRandom". I didn't bother to make the whole left/right arm tabs to try and avoid adding so many new tabs when this can already be achieved easily.

"MoveRandomTimer" is Gael's original move full robot file modified to work with "randomleftarm", "randomrightarm","randomlefthand", "randomrighthand","randomlook","randomneck" and "randomstomach" AKA Move the whole robot random with the customized settings. Just the name is unchanged. 

--------------
STRANGE ISSUE!
--------------
- This issue is relating to playing audio files ONLY. For some reason if you have random movements going and you add an audio file into your gesture, your random movements will pause for about 2 seconds. 
(This issue is relating to "mouthControlAudiofile=True" from within the InMoov/services/1_AudioFile.py file. If you change this to = False the pause will no longer occur, but in turn you should lose control of your jaw motor while playing audio. If you are running an audio servo driver... this won't matter as you aren't using that function anyway.) 

------------------
CONTACT IF NEEDED
------------------
You can reach me on the "Robotics Learning" discord or "InMoov Robot Builders" facebook page.

- Shido
