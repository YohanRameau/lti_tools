from email.message import Message
import string
from urllib.request import Request
from wsgiref.validate import validator
from django.db import models

from .utils import Validator


class Deployment():
    """Class corresponding to a LTI deployment.

    Args:
        models (_type_): _description_
    """
    deployment_id: int
    
class MessageLaunch():
    """Class corresponding to a LTI message launch. 

    Args:
        models (_type_): _description_
    """
    request: Request
    jwt: "jwt"
    registration: string
    launch_id: int
    validator: Validator
    
    @classmethod
    def generate(cls, request) -> "MessageLaunch":
        """factory method generate a LTI Message Launch object from a provider request  

        :param Request request: a HTTP request receive by the tool server
        
        :returns: a validate MessageLaunch object
        :rtype: str 
        
        :raises LTIException: This method raise a LTIException if the Message Launch cannot be validate.  
        """
        pass
        
    
    
    
    

    
    
    