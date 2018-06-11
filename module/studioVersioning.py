
'''
Studio Versioning 0.0.1
Date : March 17, 2018
Last modified: March 17, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
	Semantic Versioning
	https://semver.org/

	Given a version number MAJOR.MINOR.PATCH, increment the:
	
	    MAJOR version when you make incompatible API changes,
	    MINOR version when you add functionality in a backwards-compatible manner, and
	    PATCH version when you make backwards-compatible bug fixes.
	

	 "Semantic Versioning" Under this scheme, version numbers and the way they change convey meaning about 
	 the underlying code and what has been mdified from one version to the next.
'''	 

import os
import warnings
import getpass
import pprint
import py_compile
import shutil
import time
import threading

from PyQt4 import QtGui

from module import jsonManager


class Versioning (object):	
	
	'''
	Description
		This Class can manage Semantic Versioning.
		:param	source <str>	 example '/home/subin-g/Package'
		:param	target <str>	 example '/home/subin-g/backup'
		:param	versionType <str>	 example 'patch' or 'minor' or 'major'
		:param	excludeFolders <list>	 example ['resources', 'plugins', 'bin', 'icons']
		:param	progressBar <QtGui Class>	 example QtGui.progressBar
		
		
		:example to execute		
			source = 'Z:/packagesTest'
			target = 'Z:/backup' 
			versionType = 'patch'
			excludeFolders = [ 	'resources',
								'plugins',
								'bin',
								'icons']
			progressBar = QtGui.progressBar
			
			versionType = 'patch'
			abc = Versioning (source=source, target=target, excludeFolders=excludeFolders, versionType=versionType, progressBar=QtGui.progressBar)
			abc.createVersion () 

	'''
	
	def __init__(self, **kwargs):
		
		self.sourcePath = None
		self.targetPath = None		
		self.versionType = None
		self.excludeFolders = None
		
		if 'source' in kwargs:
			self.sourcePath = kwargs['source']
			
		if 'target' in kwargs:
			self.targetPath = kwargs['target']
			
		if 'versionType' in kwargs:
			self.versionType = kwargs['versionType']
			
		if 'excludeFolders' in kwargs:
			self.excludeFolders = kwargs['excludeFolders']
			
		if 'progressBar' in kwargs:
			self.progressBar =  kwargs['progressBar']			 
			
		self.version = 'version.json'        
		self.initialVersion = '0.0.0'

		self.versionLogFile = os.path.join (self.targetPath, self.version)	
		
		
	def hasValid (self, path):
		
		'''
		Description
			Function set for check the valid python code in the directories.
						
			:Type - class function (method)
			
			:param	path <str>	 example '/home/subin-g/Package'
			
			:example to execute		
				source = 'Z:/packagesTest'
				target = 'Z:/backup' 
				versionType = 'patch'
				excludeFolders = [ 	'resources',
									'plugins',
									'bin',
									'icons']
				
				versionType = 'patch'
				abc = Versioning (source=source, target=target, excludeFolders=excludeFolders)
				abc.hasValid ()
				print abc._isValid	<bool>
				print abc._unValid	<str>
	
		'''			
		
		result = getSouceValid (path, self.excludeFolders, self.progressBar) 		
				
		#=======================================================================
		# thread = threading.Thread(target=getSouceValid, args=(path, self.excludeFolders, self.progressBar,))
		# thread.start()				
		# result = thread.join()		
		#=======================================================================

		self._isValid = True
		self._unvalid = None 
		
		#if 'unvalid' in result :
		if  result['unvalid'] :			
			self._isValid = False
			self._unvalid = result['unvalid']

			
	def createVersion (self):
		'''
		Description
			Function set create the new version of source directories.
						
			:Type - class function (method)
			
			:param	None
			
			:example to execute		
				source = 'Z:/packagesTest'
				target = 'Z:/backup' 
				versionType = 'patch'
				excludeFolders = [ 	'resources',
									'plugins',
									'bin',
									'icons']
				
				versionType = 'patch'
				abc = Versioning (source=source, target=target, excludeFolders=excludeFolders)
				abc.createVersion () 
		'''			
	
		self.hasValid (self.sourcePath)		
				
		print '\n', self.sourcePath, '\t', self._isValid
				
		if not self._isValid :
			print '\nunvalid files\n' 
			pprint.pprint (self._unvalid)          
			return self._unvalid    
		
		currentTime = time.time () 		
		
		nextVersion = self.initialVersion
		
		if os.path.isfile(self.versionLogFile) :		
			jm = jsonManager.JManager (file=self.versionLogFile)		
			jm.getJsonData()
		
			if not jm._pythonObject:
				nextVersion = self.initialVersion
			
			if 'version' not in jm._pythonObject:
				nextVersion = self.initialVersion 
				
			if 'version' in jm._pythonObject:
				nextVersion = getNextVersion (jm._pythonObject['version'], self.versionType)

		print '\nnext version',  nextVersion
			
		destination = os.path.join (self.targetPath, nextVersion)	
		copyingFiles (self.sourcePath, destination, currentTime, self.progressBar)		
		
		#create version lof file		
		data = {'version': nextVersion}
		comment = 'Package to make new version'
		description = 'Package Semantic Version'
		dataType = 'SemanticVersion'		
		
		jm = jsonManager.JManager (	file=self.versionLogFile, 
									data=data, 
									comment=comment,
									description=description,
									dataType=dataType,
									currentTime=currentTime
									)			
		jm.setJsonData()	
		
		shutil.copy2 (self.versionLogFile, destination) # duplicate version log file to current version folder 


def getSouceValid (path, excludeFolders, progressBar):

	'''
	Description			
		Function for check the valid python code in the directories.
		
		:Type - standalone function
		
		:param	path <str>	 example '/home/subin-g/Package'
		:param  excludeFolders	<list> example ['resources', 'plugins', 'bin', 'icons']
		
		:return results	<dict>	example	{results: {'valid': {currentFile: True}},  {'unvalid': {currentFile: error message}}}
		
		:example to execute		
			path = 'Z:/packagesTest'
			excludeFolders = [ 	'resources',
								'plugins',
								'bin',
								'icons']
			import studioVersioning	
			studioVersioning.getSouceValid (path, excludeFolders)		
	'''	

	if not path:
		warnings.warn('getSouceValid argument <path> None')
		
	if not os.path.isdir(path):
		warnings.warn('getSouceValid no such path \"{}\"'.format(path))
		
	results = {}
	results['valid'] = {}
	results['unvalid'] = {}	
	
	ing = 0		
	for root, dir, files in os.walk(path):                  
		for eachFile in files : 
			
			if progressBar :			
				progressBar.setValue (ing)
				progressBar.setMaximum ((ing+100))
				#progressBar.setFormat('souce code validation')			

			currentFile = os.path.abspath(os.path.join(root, eachFile))

			exists = True			
			for eachExclude in excludeFolders:
				if currentFile.startswith (os.path.abspath(os.path.join(path, eachExclude))) :
					exists = False
					continue
			
			if not exists :
				continue			
			if os.path.isdir(currentFile) :
				continue              
			if not currentFile.endswith('.py') :
				continue
			
			try :
				py_compile.compile(currentFile, doraise=True)            
				found = {currentFile: True}            
				results['valid'].update (found)    
			except py_compile.PyCompileError, error:
				found = {currentFile: error}
				results['unvalid'].update (found)
				
			try : # remove pyc files
				os.chmod (currentFile, 0777)
				os.remove (currentFile.replace('.py', '.pyc'))
			except Exception as removeResult :
				pass
						
			ing+=1
			
	if progressBar :
		progressBar.setMaximum (100)
		progressBar.setValue (100)
			
	return results


	
def getNextVersion (currentVersion, versionType):

	'''
	Description			
		Function for return next semantic version.
		
		:Type - standalone function
		
		:param	currentVersion <str>	 example '0.0.0'
		:param  versionType	<str> example 'patch' or 'minor' or 'major'
		
		:return nextVersion	<str>	example	'0.0.1' or '0.1.0' or '1.0.0' 
		
		:example to execute		
			currentVersion = '0.0.0'
			versionType ='patch'
			
			import studioVersioning	
			studioVersioning.getNextVersion (path, versionType)		
	'''	

	major, minor, patch = currentVersion.split('.')         
	
	nextVersion = currentVersion
	
	if versionType=='patch':
		nextVersion = '{}.{}.{}'.format (major, minor, int (patch) + 1)
	
	if versionType=='minor':
		nextVersion = '{}.{}.{}'.format (major, int (minor) + 1, 0)
	
	if versionType=='major':
		nextVersion = '{}.{}.{}'.format (int (major) + 1, 0, 0)
	
	return nextVersion
	
	
def copyingFiles (source, destination, currentTime, progressBar):
	
	'''
	Description			
		Function for duplicate the directory (copying).
		
		:Type - standalone function
		
		:param	source <str>	 '/home/subin-g/Package'
		:param  destination	<str> example '/home/subin-g/backup'
		:param  currentTime	<float> example time.time () 
		
		:return None
		
		:example to execute		
# 			source = '/home/subin-g/Package'
			destination = '/home/subin-g/backup'
			currentTime = time.time () 
			
			import studioVersioning	
			studioVersioning.copyingFiles (path, versionType)		
	'''			
	progressBar.setValue (0)
	ing = 0
	for root, dirs, files in os.walk(source):
		if not os.path.isdir(root):
			os.makedirs(root)
			os.utime(root, (currentTime, currentTime))    
		
		for eachFile in files:
			destinationSuffix = root.replace(source, '').lstrip(os.sep)
			destinationPath = os.path.join(destination, destinationSuffix)
			
			if progressBar :			
				progressBar.setValue (ing)
				progressBar.setMaximum ((ing+100))
				#progressBar.setFormat('souce code versioning')			
		
			if not os.path.isdir(destinationPath):
				
				os.makedirs(destinationPath)
				os.utime(destinationPath, (currentTime, currentTime))    
		
				sourceFile = os.path.join(root, eachFile)
				destinationFile = os.path.join(destinationPath, eachFile)
		
				shutil.copy2 (sourceFile, destinationFile)            
				os.utime(destinationFile, (currentTime, currentTime)) 

			ing+=1
			
	if progressBar :
		progressBar.setMaximum (100)
		progressBar.setValue (100)

#End##############################################################################################################