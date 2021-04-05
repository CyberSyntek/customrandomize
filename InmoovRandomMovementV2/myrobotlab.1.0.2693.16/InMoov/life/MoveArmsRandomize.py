# ##############################################################################
#            *** ROBOT MOVE THE Arms RANDOMLY ***
# ##############################################################################


if isLeftArmActivated and isRightArmActivated:
  BothArmsRandom = Runtime.start("BothArmsRandom","Clock")

  def MoveArms(timedata):
    #redefine next loop
    BothArmsRandom.setInterval(random.randint(100,3000))
    if not i01.RobotIsSleeping:
          
      if isLeftArmActivated:
        i01.setArmVelocity("left", random.randint(2,10), random.randint(2,15), random.randint(2,15), random.randint(2,5))
        if not leftArm.bicep.isMoving():leftArm.bicep.moveTo(random.uniform(0,5))
        if not leftArm.shoulder.isMoving():leftArm.shoulder.moveTo(random.uniform(30,36))
        if not leftArm.rotate.isMoving():leftArm.rotate.moveTo(random.uniform(85,95))
        if not leftArm.omoplate.isMoving():leftArm.omoplate.moveTo(random.uniform(10,13))
      if isRightArmActivated:
        i01.setArmVelocity("right", random.randint(2,10), random.randint(2,15), random.randint(2,15), random.randint(2,5))
        if not rightArm.bicep.isMoving():rightArm.bicep.moveTo(random.uniform(0,5))
        if not rightArm.shoulder.isMoving():rightArm.shoulder.moveTo(random.uniform(30,36))
        if not rightArm.rotate.isMoving():rightArm.rotate.moveTo(random.uniform(85,95))
        if not rightArm.omoplate.isMoving():rightArm.omoplate.moveTo(random.uniform(10,13))
        
      else:
        BothArmsRandom.stopClock()
  
    
  #initial function
  def MoveArmsStart():
    if isLeftArmActivated and isRightArmActivated:
      print "moveArmsStart"
      if not i01.RobotIsSleeping:
        BothArmsRandom.startClock()
      else:BothArmsRandom.stopClock()
      
  def MoveArmsStop():
    
    if not i01.RobotIsSleeping:
      if isLeftArmActivated and isRightArmActivated:
        BothArmsRandom.stopClock()
 #       i01.halfSpeed()
 #       i01.rest()

#  if RobotCanMoveArms==1:
#    MoveArmsStart()
      
  BothArmsRandom.addListener("pulse", python.name, "MoveArms")
  BothArmsRandom.addListener("clockStarted", python.name, "MoveArmsStart")
  BothArmsRandom.addListener("clockStopped", python.name, "MoveArmsStop")