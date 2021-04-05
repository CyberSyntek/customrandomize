# ##############################################################################
#            *** ROBOT MOVE THE EYELIDS RANDOMLY ***
# ##############################################################################

if isEyeLidsActivated:
  MoveEyeLidsTimer = Runtime.start("MoveEyeLidsTimer","Clock")

  def MoveEyeLids(timedata):
    #redefine next loop
    MoveEyeLidsTimer.setInterval(random.randint(100,10000))
    if not i01.RobotIsSleeping and not i01.RobotIsTrackingSomething():
      
      if isEyeLidsActivated:
        i01.eyelids.setVelocity(-1,-1)
        #i01.setEyeLidsVelocity(random.randint(45,-1),random.randint(45,-1),random.randint(45,-1))
        #move the servo randomly
        i01.eyelids.moveToBlocking(random.uniform(85,140),random.uniform(85,140))
        sleep(0.2)
        i01.eyelids.moveTo(140,140)
      else:
        MoveEyeLidsTimer.stopClock()
    
  #initial function
  def MoveEyeLidsStart():
    if isEyeLidsActivated:
      print "moveEyeLidsStart"
      if not i01.RobotIsSleeping and not i01.RobotIsTrackingSomething():
        MoveEyeLidsTimer.startClock()
      else:MoveEyeLidsTimer.stopClock()
      
  def MoveEyeLidsStop():
    
    if not i01.RobotIsSleeping and not i01.RobotIsTrackingSomething():
      if isEyeLidsActivated:
        MoveEyeLidsTimer.stopClock()
        i01.eyelids.setVelocity(-1,-1)
        i01.eyelids.rest()

  if RobotCanMoveEyeLids==1:
    MoveEyeLidsStart()
      
  MoveEyeLidsTimer.addListener("pulse", python.name, "MoveEyeLids")
  MoveEyeLidsTimer.addListener("clockStarted", python.name, "MoveEyeLidsStart")
  MoveEyeLidsTimer.addListener("clockStopped", python.name, "MoveEyeLidsStop")