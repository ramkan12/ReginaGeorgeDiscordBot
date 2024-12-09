# to run virtual environment: "source venv/bin/activate"
# to stop: "deactivate"

from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import getresponse

# STEP 0: LOAD OUR TOKEN FROM SOMEHWERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
print(TOKEN)