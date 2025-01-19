# main.py
"""
Main module for TOPSIS implementation.
Provides command-line interface for the TOPSIS analysis.
"""

import sys
from typing import List
from .utils import (
    validate_input_file,
    validate_weights_and_impacts,
    normalize_matrix,
    calculate_topsis,
)

def validate_arguments() -> List[str]:
    """
    Validate command-line arguments.

    Returns:
        List[str]: List of validated command-line arguments.

    Raises:
        SystemExit: If validation fails.
    """
    if len(sys.argv) != 5:
        print("Error: Incorrect number of arguments.")
        print("Usage: topsis-aryan <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)
    return sys.argv[1:]

def main() -> None:
    """
    Main function to execute TOPSIS analysis.
    
    Reads input data, performs TOPSIS analysis, and saves results to output file.
    """
    # Validate command-line arguments
    input_file, weights, impacts, output_file = validate_arguments()

    # Validate and read the input file
    df = validate_input_file(input_file)

    # Extract data and validate weights and impacts
    data = df.iloc[:, 1:].values
    weights_list, impacts_list = validate_weights_and_impacts(
        weights, impacts, data.shape[1]
    )

    # Normalize the decision matrix
    normalized_matrix = normalize_matrix(data)

    # Calculate TOPSIS score and rank
    topsis_score, rank = calculate_topsis(normalized_matrix, weights_list, impacts_list)

    # Add TOPSIS score and rank to the dataframe
    df['Topsis Score'] = topsis_score
    df['Rank'] = rank

    # Save the result to the output file
    try:
        df.to_csv(output_file, index=False)
        print(f"Output saved to '{output_file}'")
    except Exception as e:
        print(f"Error: Unable to save the output file. {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()