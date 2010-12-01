#!/usr/bin/env python
########################################################################
# $HeadURL$
# File :    dirac-install-service
# Author :  Ricardo Graciani
########################################################################
"""
Do the initial installation and configuration of a DIRAC service
"""
__RCSID__ = "$Id$"
#
from DIRAC.Core.Utilities import InstallTools
from DIRAC.ConfigurationSystem.Client.Helpers import getCSExtensions
#
InstallTools.exitOnError = True
#
from DIRAC.Core.Base import Script
Script.setUsageMessage( '\n'.join( [ __doc__.split( '\n' )[1],
                                    'Usage:',
                                    '  %s [option|cfgfile] ... System Service|System/Agent' % Script.scriptName,
                                    'Arguments:',
                                    '  System:  Name of the DIRAC system (ie: WorkloadManagement)',
                                    '  Service: Name of the DIRAC service (ie: Matcher)'] ) )

Script.parseCommandLine()
args = Script.getPositionalArgs()

if len( args ) == 1:
  args = args[0].split( '/' )

if len( args ) != 2:
  Script.showHelp()
  exit( -1 )
#
system = args[0]
service = args[1]

InstallTools.addDefaultOptionsToCS( gConfig, 'service', system, service, getCSExtensions(), True )

InstallTools.installComponent( 'service', system, service, getCSExtensions() )
