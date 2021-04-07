# ##############################################################################
#            *** MOVES LEFT ARM RANDOMLY ***
# ##############################################################################


if isLeftArmActivated:
  LeftArmRandom = Runtime.start("LeftArmRandom","Clock")

  def MoveLeftArmRandom(timedata):    ######
    #redefine next loop
    LeftArmRandom.setInterval(random.randint(400,2300))
    if not i01.RobotIsSleeping:
          
      if isLeftArmActivated:
        i01.setArmVelocity("left", random.randint(10,50), random.randint(15,30), random.randint(10,40), random.randint(2,20))
        if not leftArm.bicep.isMoving():leftArm.bicep.moveTo(random.uniform(5,14))
        if not leftArm.shoulder.isMoving():leftArm.shoulder.moveTo(random.uniform(24,36))
        if not leftArm.rotate.isMoving():leftArm.rotate.moveTo(random.uniform(80,96))
        if not leftArm.omoplate.isMoving():leftArm.omoplate.moveTo(random.uniform(10,14))
        
      else:
        LeftArmRandom.stopClock()
  
    
  #initial function
  def MoveLeftArmRandomStart():           ######
    if isLeftArmActivated:
      print "MoveLeftArmRandomStart"         ######
      if not i01.RobotIsSleeping:
        LeftArmRandom.startClock()
      else:LeftArmRandom.stopClock()
      
  def MoveLeftArmRandomStop():     ######
    
    if not i01.RobotIsSleeping:
      if isLeftArmActivated:
        LeftArmRandom.stopClock()
 #       i01.halfSpeed()
 #       i01.rest()

#  if RobotCanLeftArmRandom==1:
#    LeftArmRandomStart()
      
  LeftArmRandom.addListener("pulse", python.name, "MoveLeftArmRandom")    ###### END    MoveLeftArmRandom
  LeftArmRandom.addListener("clockStarted", python.name, "MoveLeftArmRandomStart")    ###### END
  LeftArmRandom.addListener("clockStopped", python.name, "MoveLeftArmRandomStop")    ###### END 