def randomhandsstop():
  BothHandsRandom.stopClock()
  randomlefthandstop()
  randomrighthandstop()
  sleep(0.1) 
  i01.setHandVelocity("left", 300, 300, 300, 300, 300, 300)
  i01.setHandVelocity("right", 300, 300, 300, 300, 300, 300)