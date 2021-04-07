V0.3 (Update: 04-07-2021)
- Removed all custom commands triggering InMoov/life/MoveRandomize.py which was causing erratic movements at times when used within the same gesture as the individual triggers.

- The gesture commands remain the same as written below, just the way they function was simplied and produce the same results, without the erratic movement bug.  
-----------------------------------------------------------
HOW TO INSTALL CUSTOM RANDOM MOVEMENTS IN YOUR INMOOV ROBOT
-----------------------------------------------------------
1) - Open your InMoov folder and drag your "life" folder onto your desktop or somewhere safe. (AKA make a backup) and then delete folder.

2) - Copy the "life" folder from within this file into your InMoov folder. (If you have not modified anything previously with your own settings)

3) - Open your InMoov/config folder and copy/move "InMoovLife.config" to safe place. (AKA, Make a backup) and then delete file.

4) - Copy the InMoovLife.config file from within this file to the same location.

5) - Open the "gestures" folder from within this file and copy the files into your "InMoov/gestures" folder.

You should now be good to go! But perhaps reading the stuff below will help you understand when and how to use them. :)

------------------------------------------------------------------------------------------
Python commands to use in gesture files or in the python tab in MRL.
------------------------------------------------------------------------------------------
randomneck()   #Moves the neck randomly (Neck/Rotneck/Rollneck)
randomneckstop()   #Stops the neck from moving randomly (Neck/Rotneck/Rollneck)

randomlook()   #Moves the eyes randomly (EyeX/EyeY)
randomlookstop()   #Stops the eyes from moving randomly (EyeX/EyeY)

randomfullhead()   #Moves the fullhead randomly (Above two combo: Triggers both randomneck and randomlook)   
randomfullheadstop()    #Stops the full head from moving randomly. (Above two combo: Stops both randomneck and randomlook)   

randomleftarm()   #Moves the left arm randomly (bicep/rotate/omniplate)
randomleftarmstop()   #Stops the left arm from moving randomly.(bicep/rotate/omniplate)

randomrightarm()   #Moves the right arm randomly (bicep/rotate/omniplate)
randomrightarmstop()   #Stops the right arm from moving randomly.(bicep/rotate/omniplate)

randomarms()   #Moves both arms randomly (Above two combo: Triggers both randomleftarm and randomrightarm)   
randomarmsstop()   #Stops both arms from moving randomly.(Above two combo: Stops both randomleftarm and randomrightarm)   

randomlefthand()   #Moves the left hand randomly (Thumb/Index/Majeure/Ring/Pinky/Wrist)
randomlefthandstop()   #Stops the left hand from moving randomly.    (Thumb/Index/Majeure/Ring/Pinky/Wrist)

randomrighthand()   #Moves the right hand randomly (Thumb/Index/Majeure/Ring/Pinky/Wrist)
randomrighthandstop()   #Stops the right hand from moving randomly.    (Thumb/Index/Majeure/Ring/Pinky/Wrist)

randomhands()   #Moves both hands randomly (Above two combo: Triggers both randomlefthand and randomrighthand)  
randomhandsstop()   #Stops both hands from moving randomly.    (Above two combo: Stops both randomlefthand and randomrighthand)  

randomstomach()   #Moves the stomach randomly (TopStom/MidStom)
randomstomachstop()   #Stops the stomach from moving randomly. (TopStom/MidStom)

randomfull()   #Moves the FULL robot randomly. (FULL BODY COMBO:Triggers randomneck / randomlook / randomleftarm / randomrightarm / randomlefthand / randomrighthand / randomstomach)
randomfullstop()   #Stops the full robot from moving randomly (FULL BODY COMBO:Stops randomneck / randomlook / randomleftarm / randomrightarm / randomlefthand / randomrighthand / randomstomach)

----------
IMPORTANT!
----------
- Do NOT run the above new timers at the same time or from within the same gesture as the original files. They will overlap and cause erratic movements. 

----
TIPS
----
- Look at the RandomLife.jpg image file included to help understand how you can adjust and tune your random settings. 

- Play with the figures in the life folder files until you feel you have achieved the natural looking random movement results you are wanting.

- I believe the tabs will only show up in your MRL if you have those parts enabled for the robot. Otherwise they will show up when you have those parts enabled. I didn't test this. :9

-----
NOTES
-----
- I have not touched InMoov's original random files in place. (MoveHeadRandomize.py / MoveEyesRandomize.py / MoveRandomize.py / MoveBodyRandomize.py)

- "MoveEyesTimer" and "MoveHeadTimer" looks a bit odd in MRL with the addition of "LookRandom" and "NeckRandom" as they do close to the same things. (Note: Don't run them at the same time. haha)

-------------------------------------
STRANGE AUDIO FILE RANDOM PAUSE ISSUE
-------------------------------------
- This issue is relating to playing audio files ONLY. For some reason if you have random movements going and you add an audio file into your gesture, your random movements will pause for about 2 seconds. 
(This issue is relating to "mouthControlAudiofile=True" from within the InMoov/services/1_AudioFile.py file. If you change this to "mouthControlAudiofile=False" the pause will no longer occur. (BUT in turn you should lose control of your jaw motor while playing audio. If you are running an audio servo driver... this won't matter as you aren't using that function anyway.) 

-----------------
CONTACT IF NEEDED
-----------------
You can reach me on the "Robotics Learning" discord or "InMoov Robot Builders" facebook page if you need further help. 

- Shido
