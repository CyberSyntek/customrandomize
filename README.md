# customrandomize
Your guide to customized randomized movement with your InMoov robot. 
===========================================================================


HOW TO INSTALL CUSTOM RANDOM MOVEMENTS IN YOUR INMOOV ROBOT


1) - Open your InMoov folder and drag your "life" folder onto your desktop or somewhere safe as a backup while you test these. It will be removed from the folder.

2) - Copy the "life" folder from within this file into your InMoov folder.

3) - Open your InMoov/config folder and copy/move InMoovLife.config to save place. 

4) - With InMoovLife.config removed, Open the "config" folder from within this file and copy the new InMoovLife.config to the same location.

5) - Open the "gestures" folder from within this file and copy the files into your "InMoov/gestures" folder.
-----------------------------------------------------------------------------------------------------------
You should now be good to go! But perhaps reading the stuff below will help you understand when and how to use them. :)
- I believe the tabs will only show up in your MRL if you have those parts enabled for the robot. Otherwise they will show up when you have those parts enabled. :9


USING RANDOMIZATION - Python commands to use in gesture files or in the python tab in MRL.

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


TIPS

- Look at the RandomLife.jpg image file included to help understand how you can adjust and tune your random settings. 

- It is important to note and drill into your brain that InMoov gesture movements will always follow the last set velocity/speed setting. Random movements are generally set to a lower setting so you will want to add in the needed speed/velocity settings after each random stop() you include or certain parts of your gesture might become slow or start skipping parts.

- Remember to use these accordingly. Often when writting gestures you will not want random movements of a limb functioning as it will cut short the desired movements you do want performed, or you leave out that limb and let random handle it. It will depend on your gesture!

- Play with the figures until you feel you have achieved the natural movement results you are wanting. Remember my settings are not perfect as I recently set this up and if you get better results than mine, please share them with me! :)


OTHER TAB INFO.

- "MoveEyesTimer" and "MoveHeadTimer" looks odd being there. Those are Gael's original files which I left untouch due to I'm not sure just how tied into other services they are. I really don't want to dig through every file to find out. :D

- "FullHeadRandom" really isn't needed as it is just a combo of "LookRandom" and "NeckRandom". I didn't bother to make the whole left/right arm tabs to try and avoid adding so many new tabs when this can already be achieved easily.

- "MoveRandomTimer" is Gael's original move full robot file modified to work with "BothArmsRandom", "BothHandsRandom","LookRandom","NeckRandom" and "StomachRandom" AKA Move the whole robot random with the customizes settings, name unchanged.

CONTACT IF NEEDED

- You can reach me on the "Robotics Learning" discord or "InMoov Robot Builders" facebook page.
