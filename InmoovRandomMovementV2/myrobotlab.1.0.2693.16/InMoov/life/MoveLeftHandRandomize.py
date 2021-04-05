# ##############################################################################
#            *** ROBOT MOVE THE LEFT HAND RANDOMLY ***
# ##############################################################################


if isLeftHandActivated:
  LeftHandRandom = Runtime.start("LeftHandRandom","Clock")

  def MoveLeftHand(timedata):
    #redefine next loop
    LeftHandRandom.setInterval(random.randint(10,1500))
    if not i01.RobotIsSleeping:
          
      if isLeftHandActivated:
        i01.setHandVelocity("left", random.randint(40,75), random.randint(15,35), random.randint(15,35), random.randint(15,35), random.randint(15,35), random.randint(10,60))
        if not leftHand.thumb.isMoving():leftHand.thumb.moveTo(random.uniform(13,49))
        if not leftHand.index.isMoving():leftHand.index.moveTo(random.uniform(15,43))
        if not leftHand.majeure.isMoving():leftHand.majeure.moveTo(random.uniform(18,37))
        if not leftHand.ringFinger.isMoving():leftHand.ringFinger.moveTo(random.uniform(15,46))
        if not leftHand.pinky.isMoving():leftHand.pinky.moveTo(random.uniform(33,48))
        if not leftHand.wrist.isMoving():leftHand.wrist.moveTo(random.uniform(10,50))

      else:
        LeftHandRandom.stopClock()
  
    
  #initial function
  def MoveLeftHandStart():
    if isLeftHandActivated:
      print "moveLeftHandStart"
      if not i01.RobotIsSleeping:
        LeftHandRandom.startClock()
      else:LeftHandRandom.stopClock()
      
  def MoveLeftHandStop():
    
    if not i01.RobotIsSleeping:
      if isLeftHandActivated:
        LeftHandRandom.stopClock()
#        i01.halfSpeed()
#        i01.rest()

#  if RobotCanMoveLeftHand==1:
#    MoveLeftHandStart()
      
  LeftHandRandom.addListener("pulse", python.name, "MoveLeftHand")
  LeftHandRandom.addListener("clockStarted", python.name, "MoveLeftHandStart")
  LeftHandRandom.addListener("clockStopped", python.name, "MoveLeftHandStop")