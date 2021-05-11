import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AUoYf3qdJu9BS-pYl_CdLi-3aow7X3NQk78Um2sOeP5f83QO45Q3C_-7w9T_SaxgM8bZdN2waDhIkuG-"
        self.client_secret = "EMnssmyCLEeKYzyNn2kKMLrMUPWsUQ8SZ1ERl5Q8GrGS0ZMPvseVOKay2DnZoTfkTsLtTMcPAXYh-Xq1"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)