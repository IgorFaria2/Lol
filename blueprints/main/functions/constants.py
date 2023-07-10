import os
from dotenv import load_dotenv

load_dotenv()
DEV_KEY = os.environ.get("var_Key")
REGION_BR_KEY = os.environ.get("var_BR1")