# ##############################################################################
#            *** WHOLE ROBOT MOVE RANDOM ***
# ##############################################################################
  
MoveRandomTimer = Runtime.start("MoveRandomTimer","Clock")

def MoveRandom(timedata):

  MoveRandomTimer.setInterval(random.randint(10,100))




def MoveRandomStart():
#  MoveBodyTimer.startClock()
#  MoveEyesTimer.startClock()
#  MoveHeadTimer.startClock()
  NeckRandom.startClock()
  LookRandom.startClock()
  LeftHandRandom.startClock()
  RightHandRandom.startClock()
  LeftArmRandom.startClock()
  RightArmRandom.startClock()
  StomachRandom.startClock()
    
def MoveRandomStop():
#  MoveBodyTimer.stopClock()
#  MoveEyesTimer.stopClock()
#  MoveHeadTimer.stopClock()
  NeckRandom.stopClock()
  LookRandom.stopClock()
  LeftHandRandom.stopClock()
  RightHandRandom.stopClock()
  LeftArmRandom.stopClock()
  RightArmRandom.stopClock()
  StomachRandom.stopClock()
#  i01.RobotCanMoveHeadRandom=True
#  i01.RobotCanMoveBodyRandom=True
#  i01.RobotCanMoveEyesRandom=True
#  relax()
  i01.waitTargetPos()    
    
MoveRandomTimer.addListener("pulse", python.name, "MoveRandom")
MoveRandomTimer.addListener("clockStopped", python.name, "MoveRandomStop")
MoveRandomTimer.addListener("clockStarted", python.name, "MoveRandomStart")
