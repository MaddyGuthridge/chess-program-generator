"""
# Chess program generator

A tool for generating chess programs
"""
__version__ = '1.0.0'
__all__ = [
    'generate',
    'main',
]
from .generator import generate
from .__main__ import main
