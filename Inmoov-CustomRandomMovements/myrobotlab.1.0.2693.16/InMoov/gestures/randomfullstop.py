def randomfullstop():
  randomneckstop()
  randomlookstop()
  randomstomachstop()
  randomlefthandstop()
  randomrighthandstop()
  randomleftarmstop()
  randomrightarmstop()
  sleep(0.1)
  i01.setHeadVelocity(35,35,150,150,35,200)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)  #change to velocity
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0) #change to velocity
  i01.setTorsoSpeed(1.0, 1.0, 1.0) #change to velocity
  i01.setHandVelocity("left", 250, 270, 270, 240, 240, 240)
  i01.setHandVelocity("right", 250, 270, 270, 240, 240, 240)