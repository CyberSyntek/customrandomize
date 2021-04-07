# ##############################################################################
#            *** ROBOT MOVE THE NECK RANDOMLY ***
# ##############################################################################


if isHeadActivated:
  NeckRandom = Runtime.start("NeckRandom","Clock")

  def MoveNeck(timedata):
    #redefine next loop
    NeckRandom.setInterval(random.randint(100,2700))
    if not i01.RobotIsSleeping:
          
      if isHeadActivated:
        i01.setHeadVelocity(random.randint(10,100),random.randint(8,40),random.randint(45,70))
        if not head.rothead.isMoving():head.rothead.moveTo(random.uniform(80,100))
        if not head.neck.isMoving():head.neck.moveTo(random.uniform(50,70))
        if not head.rollNeck.isMoving():head.rollNeck.moveTo(random.uniform(65,115))

      else:
        NeckRandom.stopClock()
  
    
  #initial function
  def MoveNeckStart():
    if isHeadActivated:
      print "moveNeckStart"
      if not i01.RobotIsSleeping:
        NeckRandom.startClock()
      else:NeckRandom.stopClock()
      
  def MoveNeckStop():
    
    if not i01.RobotIsSleeping:
      if isHeadActivated:
        NeckRandom.stopClock()
#       i01.halfSpeed()
#       i01.rest()

#  if RobotCanMoveNeck==1:
#    MoveNeckStart()
      
  NeckRandom.addListener("pulse", python.name, "MoveNeck")
  NeckRandom.addListener("clockStarted", python.name, "MoveNeckStart")
  NeckRandom.addListener("clockStopped", python.name, "MoveNeckStop")