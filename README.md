# TOPSIS-102203313-Aryan_Chharia

## Description
This package implements the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) method. TOPSIS is a multi-criteria decision analysis method that helps in ranking alternatives based on multiple criteria.

## Installation
```bash
pip install Topsis-102203313-Aryan_Chharia
```

## Usage
The package can be used from the command line:

```bash
topsis-aryan <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

### Arguments:
1. `InputDataFile`: CSV file containing the decision matrix
   - First column: Object/Alternative names
   - Second column onwards: Criteria values (numeric)
2. `Weights`: Comma-separated weights for criteria (e.g., "1,1,1,2")
3. `Impacts`: Comma-separated impacts for criteria ('+' for benefit, '-' for cost) (e.g., "+,+,-,+")
4. `ResultFileName`: Name of the output CSV file

### Example:
```bash
topsis-aryan data.csv "1,1,1,2" "+,+,-,+" result.csv
```

### Input File Format:
The input CSV file should look like this:
```
Fund Name,P1,P2,P3,P4
M1,0.85,0.72,4.6,42
M2,0.65,0.66,4.8,53
M3,0.90,0.77,4.5,38
```

### Output:
The program will create a result CSV file with additional columns:
- Topsis Score
- Rank

## License
MIT License

## Author
Aryan Chharia