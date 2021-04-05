# ##############################################################################
#            *** MOVES LEFT ARM RANDOMLY ***
# ##############################################################################


if isRightArmActivated:
  RightArmRandom = Runtime.start("RightArmRandom","Clock")

  def MoveRightArmRandom(timedata):    ######
    #redefine next loop
    RightArmRandom.setInterval(random.randint(400,2200))
    if not i01.RobotIsSleeping:
          
      if isRightArmActivated:
        i01.setArmVelocity("right", random.randint(10,50), random.randint(15,30), random.randint(10,40), random.randint(2,20))
        if not rightArm.bicep.isMoving():rightArm.bicep.moveTo(random.uniform(0,9))
        if not rightArm.shoulder.isMoving():rightArm.shoulder.moveTo(random.uniform(24,36))
        if not rightArm.rotate.isMoving():rightArm.rotate.moveTo(random.uniform(80,96))
        if not rightArm.omoplate.isMoving():rightArm.omoplate.moveTo(random.uniform(10,14))
        
      else:
        RightArmRandom.stopClock()
  
    
  #initial function
  def MoveRightArmRandomStart():           ######
    if isRightArmActivated:
      print "MoveRightArmRandomStart"         ######
      if not i01.RobotIsSleeping:
        RightArmRandom.startClock()
      else:RightArmRandom.stopClock()
      
  def MoveRightArmRandomStop():     ######
    
    if not i01.RobotIsSleeping:
      if isRightArmActivated:
        RightArmRandom.stopClock()
 #       i01.halfSpeed()
 #       i01.rest()

#  if RobotCanRightArmRandom==1:
#    RightArmRandomStart()
      
  RightArmRandom.addListener("pulse", python.name, "MoveRightArmRandom")    ###### END    MoveRightArmRandom
  RightArmRandom.addListener("clockStarted", python.name, "MoveRightArmRandomStart")    ###### END
  RightArmRandom.addListener("clockStopped", python.name, "MoveRightArmRandomStop")    ###### END 