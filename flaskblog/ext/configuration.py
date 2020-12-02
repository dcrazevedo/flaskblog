import os
from importlib import import_module
from ..config import Extensions

def load_extensions(app):
    for extension in getattr(Extensions, 'DEVELOPMENT'):
        
        ext = import_module(extension)
        
        ext.init_app(app)