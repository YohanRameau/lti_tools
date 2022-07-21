from email.message import Message
from platform import platform
import string
import uuid

from django.db import models
from urllib.request import Request
from wsgiref.validate import validator

from .utils import Validator


class KeySet(models.Model):
    id: models.UUIDField = models.UUIDField(primary_key=True)
    
class Key(models.Model):
    id: models.UUIDField = models.UUIDField(primary_key=True)
    key_set_id: "KeySet" = models.ForeignKey(KeySet)
    private_key: models.CharField = models.CharField()
    alg: models.CharField = models.CharField()
class Registration(models.Model):
    """Class corresponding to a LTI Registration

    Args:
        models (_type_): _description_
    """
    
    id: models.UUIDField = models.UUIDField(primary_key=True, default=uuid, editable=False)
    issuer: models.CharField = models.CharField()
    client_id: models.IntegerField()
    platform_login_auth_endpoint: models.CharField()
    platform_service_auth_endpoint: models.CharField()
    platform_jwks_endpoint: models.CharField()
    platform_auth_provider: models.CharField()
    key_set_id: models.ForeignKey()
    

    

class Deployment(models.Model):
    """Class corresponding to a LTI deployment.

    Args:
        models (_type_): _description_
    """
    deployment_id: models.UUIDField
    registration_id: models.UUIDField = models.ForeignKey(Registration)
    customer_id: models.CharField = models.CharField()
    
    
    
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
        
    
    
    
    

    
    
    