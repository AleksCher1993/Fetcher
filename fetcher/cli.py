
import logging
from . import config
import typer

logger=logging.getLogger(config.settings.app_name)

def welcome(name:str,repeat:int):
    for i in range(repeat):
        logger.info(f"Hello {name} ({i+1} / {repeat})")
        typer.echo(f"Welcome {name}! I repeated that {i+1} / {repeat} times.")