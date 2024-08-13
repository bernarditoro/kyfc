# KYFC: Keep Your First Class

## Overview

`KYFC` is a Python script designed to help students calculate their GPA and CGPA based on their current grades, and generate all possible grade combinations for future semesters that would help maintain or achieve a specific degree class.

## Features

- **CGPA Calculation**: Calculate your cumulative GPA across multiple semesters.
- **GPA Calculation**: Calculate your GPA for a specific semester.
- **Grade Combinations**: Generate all possible grade combinations for the current semester that can help you achieve a specified CGPA or GPA.
- **Degree Classification**: Supports classification into First Class, Second Class Upper, Second Class Lower, Third Class, and Pass.
- **Customizable Inputs**: Use your current grades and desired future grades to tailor the calculations.

## Requirements

- Python 3.x
- `tabulate` module: Install with `pip install tabulate`

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/bernarditoro/kyfc.git
    ```
2. Navigate to the project directory:
    ```bash
    cd grades_combinations
    ```
3. Ensure you have the required Python modules installed:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Command-Line Arguments

You can run the script from the command line with the following options:

- `-c` or `--use_cgpa`: Use CGPA as the benchmark for generating grade combinations (default is GPA).
- `-d` or `--degree_class`: Specify the degree class you want to achieve or maintain. Options are:
  - `f`: First Class
  - `su`: Second Class Upper
  - `sl`: Second Class Lower
  - `t`: Third Class
  - `p`: Pass

### Example Usage

To generate grade combinations that will help you keep a First Class based on your CGPA:

```bash
python grades_combinations.py -c -d f
```

To generate grade combinations that will help you achieve a Second Class Upper based on your GPA:

```bash
python grades_combinations.py -d su
```

### Outputs

- **`cgpa.txt`**: This file will contain the GPA of past semesters and your overall CGPA.
- **`kyfc_grades.txt`**: This file will contain possible grade combinations for the current semester that can help you achieve the specified degree class.

## Customization

You can customize the script to use different courses, credit hours, or grades by modifying the respective variables in the script:

- `self.courses_list`: List of courses for each semester.
- `self.credit_hours`: Corresponding credit hours for the courses.
- `self.grades`: List of grades achieved or anticipated.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request.

## Author

- Github: [bernarditoro](https://github.com/bernarditoro)
- X: [bernarditoro_](https://x.com/bernarditoro_)

---