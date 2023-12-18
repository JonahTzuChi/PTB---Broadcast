# Load config files into the program

import yaml
import dotenv
from pathlib import Path

local_dir = Path(__file__).parent.parent.resolve() / "config"

config_env = dotenv.dotenv_values(local_dir / "config.env")
print(config_env.keys())
token = config_env["PUBLIC_BOT"]
mongodb_uri = f"mongodb://{config_env['MONGODB_HOST']}:{config_env['MONGODB_PORT']}"

with open(local_dir / "config.yml", "r") as f:
    config_yaml = yaml.safe_load(f)

ACCESS = dict()
ACCESS['ALLOWED_USERS'] : list = config_yaml['ALLOWED_USERS']
ACCESS['SYSTEM_ADMINS'] : list = config_yaml['SYSTEM_ADMINS']
 
BOTLINES = dict()
BOTLINES['GREETING'] : str = config_yaml['GREETING']
BOTLINES['FAREWELL'] : str = config_yaml['FAREWELL']