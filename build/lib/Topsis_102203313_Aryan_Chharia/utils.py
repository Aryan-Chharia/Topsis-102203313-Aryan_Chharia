# utils.py
"""Utility functions for TOPSIS implementation."""

import pandas as pd
import numpy as np
from typing import List, Tuple, Union
import sys

def validate_input_file(input_file: str) -> pd.DataFrame:
    """
    Validate and read the input CSV file.

    Args:
        input_file (str): Path to the input CSV file.

    Returns:
        pd.DataFrame: Validated DataFrame containing the decision matrix.

    Raises:
        SystemExit: If validation fails.
    """
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: Unable to read the file '{input_file}'. {str(e)}")
        sys.exit(1)

    if df.shape[1] < 3:
        print("Error: Input file must have at least three columns.")
        sys.exit(1)

    for col in df.columns[1:]:
        if not pd.api.types.is_numeric_dtype(df[col]):
            print("Error: All columns from the second to last must contain numeric values only.")
            sys.exit(1)

    return df

def validate_weights_and_impacts(
    weights: str, 
    impacts: str, 
    num_criteria: int
) -> Tuple[List[float], List[str]]:
    """
    Validate weights and impacts strings.

    Args:
        weights (str): Comma-separated string of weights.
        impacts (str): Comma-separated string of impacts ('+' or '-').
        num_criteria (int): Number of criteria in the decision matrix.

    Returns:
        Tuple[List[float], List[str]]: Validated weights and impacts lists.

    Raises:
        SystemExit: If validation fails.
    """
    try:
        weights_list = [float(w) for w in weights.split(',')]
    except ValueError:
        print("Error: Weights must be numeric and separated by commas.")
        sys.exit(1)

    impacts_list = impacts.split(',')
    if not all(i in ['+', '-'] for i in impacts_list):
        print("Error: Impacts must be '+' or '-' and separated by commas.")
        sys.exit(1)

    if len(weights_list) != num_criteria or len(impacts_list) != num_criteria:
        print("Error: Number of weights and impacts must match the number of criteria.")
        sys.exit(1)

    return weights_list, impacts_list

def normalize_matrix(matrix: np.ndarray) -> np.ndarray:
    """
    Normalize the decision matrix using vector normalization.

    Args:
        matrix (np.ndarray): Decision matrix to normalize.

    Returns:
        np.ndarray: Normalized decision matrix.
    """
    return matrix / np.sqrt((matrix**2).sum(axis=0))

def calculate_topsis(
    matrix: np.ndarray,
    weights: List[float],
    impacts: List[str]
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Calculate TOPSIS scores and rankings.

    Args:
        matrix (np.ndarray): Normalized decision matrix.
        weights (List[float]): List of criteria weights.
        impacts (List[str]): List of criteria impacts ('+' or '-').

    Returns:
        Tuple[np.ndarray, np.ndarray]: TOPSIS scores and rankings.
    """
    weighted_matrix = matrix * weights

    ideal_best = []
    ideal_worst = []
    for i, impact in enumerate(impacts):
        if impact == '+':
            ideal_best.append(np.max(weighted_matrix[:, i]))
            ideal_worst.append(np.min(weighted_matrix[:, i]))
        else:
            ideal_best.append(np.min(weighted_matrix[:, i]))
            ideal_worst.append(np.max(weighted_matrix[:, i]))

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    distance_to_best = np.sqrt(((weighted_matrix - ideal_best)**2).sum(axis=1))
    distance_to_worst = np.sqrt(((weighted_matrix - ideal_worst)**2).sum(axis=1))

    topsis_score = distance_to_worst / (distance_to_best + distance_to_worst)
    rank = topsis_score.argsort()[::-1] + 1

    return topsis_score, rank
