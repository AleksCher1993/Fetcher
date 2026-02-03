import logging
import typer
from . import cli
from . import logger
from . import config


def main(name:str=typer.Option("John",help="Enter your name!",prompt="Enter your name: "),
         repeat:int=typer.Option(...,help="Enter count of iteration!",prompt="Enter count of iteration: ",min=1,max=20)):
    logger.log_manager()
    log=logging.getLogger(config.settings.app_name)
    
    log.info(f"Starting {config.settings.app_name}")

    cli.welcome(name,repeat)

typer.run(main)