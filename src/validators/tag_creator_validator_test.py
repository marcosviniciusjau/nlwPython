from .tag_creator_validator import tag_creator_validator

class MockRequest:
    def __init__(self,json) -> None:
        self.json= json

def test_tag_creator_validator(): 
    req= MockRequest(json={"product_code":12345})
    tag_creator_validator(req)

def test_tag_creator_validator_with_error():
    pass
