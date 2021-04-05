# ##############################################################################
#            *** ROBOT MOVE THE Fingers RANDOMLY ***
# ##############################################################################


if isLeftHandActivated and isRightHandActivated:
  BothHandsRandom = Runtime.start("BothHandsRandom","Clock")

  def MoveHands(timedata):
    #redefine next loop
    BothHandsRandom.setInterval(random.randint(100,1800))
    if not i01.RobotIsSleeping:
          
      if isLeftHandActivated:
        i01.setHandVelocity("left", random.randint(10,100), random.randint(10,100), random.randint(10,100), random.randint(10,100), random.randint(10,100), random.randint(8,40))
        if not leftHand.thumb.isMoving():leftHand.thumb.moveTo(random.uniform(30,90))
        if not leftHand.index.isMoving():leftHand.index.moveTo(random.uniform(50,65))
        if not leftHand.majeure.isMoving():leftHand.majeure.moveTo(random.uniform(55,70))
        if not leftHand.ringFinger.isMoving():leftHand.ringFinger.moveTo(random.uniform(45,60))
        if not leftHand.pinky.isMoving():leftHand.pinky.moveTo(random.uniform(60,75))
        if not leftHand.wrist.isMoving():leftHand.wrist.moveTo(random.uniform(10,50))
      if isRightHandActivated:
        i01.setHandVelocity("right", random.randint(10,100), random.randint(10,100), random.randint(10,100), random.randint(10,100), random.randint(10,100), random.randint(8,40))
        if not rightHand.thumb.isMoving():rightHand.thumb.moveTo(random.uniform(30,90))
        if not rightHand.index.isMoving():rightHand.index.moveTo(random.uniform(60,75))
        if not rightHand.majeure.isMoving():rightHand.majeure.moveTo(random.uniform(35,50))
        if not rightHand.ringFinger.isMoving():rightHand.ringFinger.moveTo(random.uniform(35,45))
        if not rightHand.pinky.isMoving():rightHand.pinky.moveTo(random.uniform(50,70))
        if not rightHand.wrist.isMoving():rightHand.wrist.moveTo(random.uniform(140,180))

      else:
        BothHandsRandom.stopClock()
  
    
  #initial function
  def MoveHandsStart():
    if isLeftHandActivated and isRightHandActivated:
      print "moveFingersStart"
      if not i01.RobotIsSleeping:
        BothHandsRandom.startClock()
      else:BothHandsRandom.stopClock()
      
  def MoveHandsStop():
    
    if not i01.RobotIsSleeping:
      if isLeftHandActivated and isRightHandActivated:
        BothHandsRandom.stopClock()
#        i01.halfSpeed()
#        i01.rest()

#  if RobotCanMoveHands==1:
#    MoveHandsStart()
      
  BothHandsRandom.addListener("pulse", python.name, "MoveHands")
  BothHandsRandom.addListener("clockStarted", python.name, "MoveHandsStart")
  BothHandsRandom.addListener("clockStopped", python.name, "MoveHandsStop")