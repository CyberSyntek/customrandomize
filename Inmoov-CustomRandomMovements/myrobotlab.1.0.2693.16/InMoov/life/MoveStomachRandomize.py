# ##############################################################################
#            *** ROBOT MOVE THE STOMACH RANDOMLY ***
# ##############################################################################


if isTorsoActivated:
  StomachRandom = Runtime.start("StomachRandom","Clock")

  def MoveStomach(timedata):
    #redefine next loop
    StomachRandom.setInterval(random.randint(100,10000))
    if not i01.RobotIsSleeping:
          
      if isTorsoActivated:
        i01.setTorsoVelocity(random.randint(2,30), random.randint(2,70), random.randint(2,100))
        if not torso.topStom.isMoving():torso.topStom.moveTo(random.uniform(87,93))
        if not torso.midStom.isMoving():torso.midStom.moveTo(random.uniform(75,105))

      else:
        StomachRandom.stopClock()
  
    
  #initial function
  def MoveStomachStart():
    if isTorsoActivated:
      print "moveStomachStart"
      if not i01.RobotIsSleeping:
        StomachRandom.startClock()
      else:StomachRandom.stopClock()
      
  def MoveStomachStop():
    
    if not i01.RobotIsSleeping:
      if isTorsoActivated:
        StomachRandom.stopClock()
#       i01.halfSpeed()
#       i01.rest()

#  if RobotCanMoveStomach==1:
#    MoveStomachStart()
      
  StomachRandom.addListener("pulse", python.name, "MoveStomach")
  StomachRandom.addListener("clockStarted", python.name, "MoveStomachStart")
  StomachRandom.addListener("clockStopped", python.name, "MoveStomachStop")