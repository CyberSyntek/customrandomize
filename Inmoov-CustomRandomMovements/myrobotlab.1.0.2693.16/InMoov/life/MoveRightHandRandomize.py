# ##############################################################################
#            *** ROBOT MOVE THE RIGHT HAND RANDOMLY ***
# ##############################################################################


if isRightHandActivated:
  RightHandRandom = Runtime.start("RightHandRandom","Clock")

  def MoveRightHand(timedata):
    #redefine next loop
    RightHandRandom.setInterval(random.randint(10,1500))
    if not i01.RobotIsSleeping:
          
      if isRightHandActivated:
        i01.setHandVelocity("right", random.randint(40,75), random.randint(15,35), random.randint(15,35), random.randint(15,35), random.randint(15,35), random.randint(10,60))
        if not rightHand.thumb.isMoving():rightHand.thumb.moveTo(random.uniform(12,49))
        if not rightHand.index.isMoving():rightHand.index.moveTo(random.uniform(31,48))
        if not rightHand.majeure.isMoving():rightHand.majeure.moveTo(random.uniform(8,27))
        if not rightHand.ringFinger.isMoving():rightHand.ringFinger.moveTo(random.uniform(18,44))
        if not rightHand.pinky.isMoving():rightHand.pinky.moveTo(random.uniform(23,52))
        if not rightHand.wrist.isMoving():rightHand.wrist.moveTo(random.uniform(140,180))

      else:
        RightHandRandom.stopClock()
  
    
  #initial function
  def MoveRightHandStart():
    if isRightHandActivated:
      print "moveRightHandStart"
      if not i01.RobotIsSleeping:
        RightHandRandom.startClock()
      else:RightHandRandom.stopClock()
      
  def MoveRightHandStop():
    
    if not i01.RobotIsSleeping:
      if isRightHandActivated:
        RightHandRandom.stopClock()
#        i01.halfSpeed()
#        i01.rest()

#  if RobotCanMoveRightHand==1:
#    MoveRightHandStart()
      
  RightHandRandom.addListener("pulse", python.name, "MoveRightHand")
  RightHandRandom.addListener("clockStarted", python.name, "MoveRightHandStart")
  RightHandRandom.addListener("clockStopped", python.name, "MoveRightHandStop")