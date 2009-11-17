""" ReplicationPlacementHandler is the service interface to the ReplicationPlacementDB.
"""

from types import *
from DIRAC.Core.DISET.RequestHandler import RequestHandler
from DIRAC import gLogger, gMonitor, gConfig, S_OK, S_ERROR
from DIRAC.DataManagementSystem.DB.ReplicationPlacementDB import ReplicationPlacementDB
from DIRAC.TransformationSystem.Service.TransformationHandler import TransformationHandler

# This is a global instance of the ReplicationPlacementDB class
placementDB = False

def initializeReplicationPlacementHandler(serviceInfo):
  global placementDB
  placementDB = ReplicationPlacementDB()
  return S_OK()

class ReplicationPlacementHandler(TransformationHandler):

  def __init__(self,*args,**kargs):

    self.setDatabase(placementDB)
    TransformationHandler.__init__(self,*args,**kargs)
