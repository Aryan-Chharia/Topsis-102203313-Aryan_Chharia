# __init__.py
"""
TOPSIS Implementation Package

This package implements the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS).
TOPSIS is a multi-criteria decision analysis method for ranking alternatives based on multiple criteria.
"""

from .main import main
from .utils import (
    validate_input_file,
    validate_weights_and_impacts,
    normalize_matrix,
    calculate_topsis,
)

__version__ = "1.0.0"
__author__ = "Aryan Chharia"