#  all my system function here.
import yaml 

def OfficeConfig():
    # Read the configuration from the config.yaml file
    with open('office_config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    
    # Return the configuration
    return config