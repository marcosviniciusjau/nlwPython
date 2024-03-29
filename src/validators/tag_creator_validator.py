from cerberus import Validator
from src.errors.error_types.http_unprocessed_entity import HttpUnprocessedEntityError

def tag_creator_validator(request : any)-> None:
    body_validator= Validator({
        "product_code":{"type":"string", "required":True, "empty": False}
    })
    
    response= body_validator.validate(request.json)
    if response is False:
        raise HttpUnprocessedEntityError(body_validator.errors)
