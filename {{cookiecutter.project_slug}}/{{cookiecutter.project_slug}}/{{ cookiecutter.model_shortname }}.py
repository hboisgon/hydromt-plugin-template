import logging
from hydromt.models import {{cookiecutter.model_type}}

from pathlib import Path
from os.path import join
from typing import Optional, Dict, Any, Union, List

from . import DATADIR, workflows

__all__ = ["{{cookiecutter.model_classname}}"]

logger = logging.getLogger(__name__)


class {{cookiecutter.model_classname}}({{cookiecutter.model_type}}):
    """This is the {{cookiecutter.model_shortname}} class"""

    # Any global class variables your model should have go here
    _NAME: str = "{{cookiecutter.model_classname}}"
    _CONF: str = "model.yaml"
    _DATADIR: Path = DATADIR

    # Dictionnary of hydromt model components mapping
    # Can be used for example to rename variables in the different objects from
    # hydromt convention name to the model specific name.
    _GEOMS: Dict[str, Any] = {}
    _MAPS: Dict[str, Any] = {}
    _FORCINGS: Dict[str, Any] = {}
    _STATES: Dict[str, Any] = {}
    _RESULTS: Dict[str, Any] = {}

    # Name of default folders to create in the model directory
    _FOLDERS: List[str] = []

    # Name of defaults catalogs to include when initialising the model
    # For example to include model specific parameter data or mapping
    # These default catalogs can be placed in the _DATADIR folder.
    _CATALOGS: List[str] = [join(_DATADIR, "parameters_data.yml")]

    def __init__(
        self,
        root: Optional[str] = None,
        mode: str = "w",
        config_fn: Optional[str] = None,
        data_libs: Optional[Union[List[str], str]] = None,
        logger: logging.Logger = logger,
    ):
        """
        The {{cookiecutter.model_shortname}} model class {{cookiecutter.model_classname}}.

        Contains methods to read, write, setup and update {{cookiecutter.model_shortname}} models.

        Parameters
        ----------
        root : str, Path, optional
            Path to the model folder
        mode : {'w', 'w+', 'r', 'r+'}, optional
            Mode to open the model, by default 'w'
        config_fn : str, Path, optional
            Path to the model configuration file, by default None to read
            from template in build mode or default name in update mode.
        data_libs : list of str, optional
            List of data catalogs to use, by default None.
        logger : logging.Logger, optional
            Logger to use, by default logger
        """
        # Add model _CATALOGS to the data_libs
        if self._CATALOGS:
            if isinstance(data_libs, str):
                data_libs = [data_libs]
            data_libs = data_libs + self._CATALOGS

        super().__init__(
            root=root,
            mode=mode,
            config_fn=config_fn,
            data_libs=data_libs,
            logger=logger,
        )
        # If your model needs any extra specific initialisation add them here

    # SETUP METHODS
    # Write here specific methods to add or update model data components

    # I/O METHODS
    # Write here specific methods to read or write model data components or overwrite the ones from HydroMT CORE

    # MODEL COMPONENTS AND PROPERTIES
    # Write here specific model properties and components not available in HydroMT CORE
