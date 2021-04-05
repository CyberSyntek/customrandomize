# ##############################################################################
#            *** FULL HEAD MOVE RANDOM ***
# ##############################################################################
  
FullHeadRandom = Runtime.start("FullHeadRandom","Clock")

def MoveRandomFullHead(timedata):

  FullHeadRandom.setInterval(random.randint(10,100))




def MoveRandomFullHeadStart():
#  MoveBodyTimer.startClock()
  LookRandom.startClock()
  NeckRandom.startClock()
#  MoveStomachTimer.startClock()
    
def MoveRandomFullHeadStop():
#  MoveBodyTimer.stopClock()
  LookRandom.stopClock()
  NeckRandom.stopClock()
#  MoveStomachTimer.stopClock()
#  i01.RobotCanMoveHeadRandom=True
#  i01.RobotCanMoveBodyRandom=True
#  i01.RobotCanMoveEyesRandom=True
#  relax()
  i01.waitTargetPos()    
    
FullHeadRandom.addListener("pulse", python.name, "MoveRandomFullHead")
FullHeadRandom.addListener("clockStopped", python.name, "MoveRandomFullHeadStop")
FullHeadRandom.addListener("clockStarted", python.name, "MoveRandomFullHeadStart")
