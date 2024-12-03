# File Integrity Checker

## Project Overview
This project is a Python-based tool to ensure file integrity by generating, storing, and verifying SHA-256 hashes for files. It helps detect unauthorized file modifications.

## File Structure
- `src/file_scanner.py`: Scans directories and generates file hashes.
- `src/file_checker.py`: Verifies file integrity using stored hashes.
- `src/hash_util.py`: Utility functions for hash generation and comparison.
- `data/stored_hashes.json`: Stores generated file hashes in JSON format.
- `tests/test_file_scanner.py`: Unit tests for the file scanner.
- `tests/test_file_checker.py`: Unit tests for the file checker.
- `README.md`: Project documentation.
- `setup.py`: Setup script for installation.

## Installation and Setup

### Clone the repository
```bash
git clone https://github.com/MustcodeQ/FileIntegrityChecker.git
cd FileIntegrityChecker
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Install the package
```bash
pip install .
```

## Usage

### Scanning Files and Saving Hashes
Run the `file_scanner` command:
```bash
file_scanner --directory <directory_path> --output <output_file>
```

**Example:**
```bash
file_scanner --directory ./test_dir --output ./data/stored_hashes.json
```

### Verifying File Integrity
Run the `file_checker` command:
```bash
file_checker --input <stored_hashes_file>
```

**Example:**
```bash
file_checker --input ./data/stored_hashes.json
```

### Running Tests
Run unit tests to verify functionality:
```bash
python -m unittest discover -s tests
```

## Configuration
Modify the `stored_hashes.json` file in the `data/` folder to add or update stored file hashes.

**Example:**
```json
{
  "file1.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "file2.txt": "a3c9c11362c1d149dfbf2c7b928dfae4629a7e11e594b634ea525391b7e2a222"
}
```

## License
This project is licensed under the MIT License.
