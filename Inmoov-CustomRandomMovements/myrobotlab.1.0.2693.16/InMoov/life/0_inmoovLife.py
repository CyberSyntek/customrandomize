# ##############################################################################
#            *** INMOOV LIFE ***
# ##############################################################################



  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  

#read current skeleton part config
inmoovLifeConfigFile=RuningFolder+'config/InMoovLife'

###############################################################################
#                 webgui sync
getInmoovFrParameter('inmoovlife',inmoovLifeConfigFile+'.config')
###############################################################################

CheckFileExist(inmoovLifeConfigFile)
inmoovLifeConfig = ConfigParser.ConfigParser()
inmoovLifeConfig.read(inmoovLifeConfigFile+'.config')

HealthCheckActivated=inmoovLifeConfig.getboolean('HEALTHCHECK', 'Activated')
HealthCheckTimerValue=inmoovLifeConfig.getint('HEALTHCHECK', 'TimerValue')
RobotCanMoveEyeLids=inmoovLifeConfig.getboolean('MOVEEYELIDSRANDOM', 'RobotCanMoveEyeLids')
RobotCanLeftHand=inmoovLifeConfig.getboolean('LEFTHANDRANDOM', 'RobotCanLeftHand')
RobotCanRightHand=inmoovLifeConfig.getboolean('RIGHTHANDRANDOM', 'RobotCanRightHand')
RobotCanNeck=inmoovLifeConfig.getboolean('NECKRANDOM', 'RobotCanNeck')
RobotCanLook=inmoovLifeConfig.getboolean('LOOKRANDOM', 'RobotCanLook')
RobotCanLeftArm=inmoovLifeConfig.getboolean('LEFTARMRANDOM', 'RobotCanLeftArm')
RobotCanRightArm=inmoovLifeConfig.getboolean('RIGHTARMRANDOM', 'RobotCanRightArm')
RobotCanStomach=inmoovLifeConfig.getboolean('STOMACHRANDOM', 'RobotCanStomach')

i01.RobotCanMoveHeadRandom=inmoovLifeConfig.getboolean('MOVEHEADRANDOM', 'RobotCanMoveHeadWhileSpeaking')
try:
  SleepTimeout=inmoovLifeConfig.getint('SLEEPMODE', 'SleepTimeout')
except:
  inmoovLifeConfig.set('SLEEPMODE', 'SleepTimeout', '300000')
  inmoovLifeConfig.set('SLEEPMODE', 'TrackingTimeout', '60000')
  inmoovLifeConfig.set('SLEEPMODE', 'UsePirToActivateTracking', True)
  with open(inmoovLifeConfigFile+'.config', 'wb') as f:
    inmoovLifeConfig.write(f)
  inmoovLifeConfig.read(inmoovLifeConfigFile+'.config')
  pass
SleepTimeout=inmoovLifeConfig.getint('SLEEPMODE', 'SleepTimeout')
TrackingTimeout=inmoovLifeConfig.getint('SLEEPMODE', 'TrackingTimeout')
UsePirToActivateTracking=inmoovLifeConfig.getboolean('SLEEPMODE', 'UsePirToActivateTracking')
