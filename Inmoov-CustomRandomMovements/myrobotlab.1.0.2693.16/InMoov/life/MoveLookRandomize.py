# ##############################################################################
#            *** ROBOT LOOKS AROUND RANDOMLY ***
# ##############################################################################


if isHeadActivated:
  LookRandom = Runtime.start("LookRandom","Clock")

  def MoveLook(timedata):
    #redefine next loop
    LookRandom.setInterval(random.randint(200,1500))
    if not i01.RobotIsSleeping:
          
      if isHeadActivated:
        head.eyeX.setVelocity(random.randint(130,200))
        head.eyeY.setVelocity(random.randint(130,200))
        if not head.eyeX.isMoving():head.eyeX.moveTo(random.uniform(60,120))
        if not head.eyeY.isMoving():head.eyeY.moveTo(random.uniform(60,100))

      else:
        LookRandom.stopClock()
  
    
  #initial function
  def MoveLookStart():
    if isHeadActivated:
      print "moveLookStart"
      if not i01.RobotIsSleeping:
        LookRandom.startClock()
      else:LookRandom.stopClock()
      
  def MoveLookStop():
    
    if not i01.RobotIsSleeping:
      if isHeadActivated:
        LookRandom.stopClock()
#       i01.halfSpeed()
#       i01.rest()

#  if RobotCanMoveLook==1:
#    MoveLookStart()
      
  LookRandom.addListener("pulse", python.name, "MoveLook")
  LookRandom.addListener("clockStarted", python.name, "MoveLookStart")
  LookRandom.addListener("clockStopped", python.name, "MoveLookStop")