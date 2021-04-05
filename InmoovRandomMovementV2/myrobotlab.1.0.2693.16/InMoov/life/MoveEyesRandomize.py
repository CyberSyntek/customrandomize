# ##############################################################################
#            *** ROBOT MOVE THE EYES ( ex WHILE SPEAKIN ) ***
# ##############################################################################
  
MoveEyesTimer = Runtime.start("MoveEyesTimer","Clock")

def MoveEyes(timedata):
  #redefine next loop
  MoveEyesTimer.setInterval(random.randint(200,2000))
  if i01.RobotCanMoveEyesRandom and i01.RobotCanMoveRandom and not i01.RobotIsSleeping and not i01.RobotIsTrackingSomething():
    if isHeadActivated:
      head.eyeX.setVelocity(random.randint(130,200))
      head.eyeY.setVelocity(random.randint(130,200))
      #wait servo last move
      if not head.eyeX.isMoving():head.eyeX.moveTo(random.uniform(60,120))
      if not head.eyeY.isMoving():head.eyeY.moveTo(random.uniform(60,100))
    else:
      MoveEyesTimer.stopClock()
  
#initial function
def MoveEyesStart():
  if i01.RobotCanMoveEyesRandom and i01.RobotCanMoveRandom and not i01.RobotIsSleeping and not i01.RobotIsTrackingSomething():
    if not isHeadActivated:MoveEyesTimer.stopClock()
    
def MoveEyesStop():
  
  if i01.RobotCanMoveEyesRandom and i01.RobotCanMoveRandom and not i01.RobotIsSleeping and not i01.RobotIsTrackingSomething():
    if isHeadActivated:
      head.eyeX.rest()
      head.eyeY.rest()
    
MoveEyesTimer.addListener("pulse", python.name, "MoveEyes")
MoveEyesTimer.addListener("clockStarted", python.name, "MoveEyesStart")  
MoveEyesTimer.addListener("clockStopped", python.name, "MoveEyesStop")