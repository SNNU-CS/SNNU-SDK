'''
Created on Nov 29, 2018

@author: QiZhao
'''


class SnnuException(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, *args, **kwargs):
        super(SnnuException, self).__init__(*args, **kwargs)


class AuthenticationException(SnnuException):
    """An Authentication Exception occurred."""


class UnauthorizedError(SnnuException):
    """Not authorized Error"""


class TemporaryBannedException(SnnuException):
    """Temporary Banned by Server"""
