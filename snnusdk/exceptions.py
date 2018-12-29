__author__ = 'QiZhao'

'''
Created on Nov 29, 2018

@author: QiZhao
'''


class SnnuException(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, *args, **kwargs):
        super(SnnuException, self).__init__(*args, **kwargs)

class AuthenticationError(SnnuException):
    """An Authentication Exception occurred."""

class UnauthorizedError(SnnuException):
    """Not authorized Error"""

class TemporaryBannedError(SnnuException):
    """Temporary Banned by Server"""

class BuildingNotFoundError(SnnuException):
    """Building Not Found Error"""

class RoomNotFoundError(SnnuException):
    """Room Not Found Error"""
    
class YearNotExistError(SnnuException):
    """Year Not Exist Error"""
    
class DepartmentNotSupportedError(SnnuException):
    """Deparment Not Supported Error"""