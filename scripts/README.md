# Marp Document Generator

## Overview

This Python script automatically generates Marp-formatted documents by parsing Markdown files within a specified root directory. The script is highly configurable, allowing you to specify the sections and levels to be included in the final document as well as the locale for the root directory.

## Requirements

- Python 3.x
- `argparse` library (built-in with Python)
- `re` library (built-in with Python)
- `os` library (built-in with Python)
- `yaml` library (can be installed via pip)

## Installation

1. Clone the repository to your local machine.
2. Navigate to the directory where the script resides.
3. Make sure you have all the required libraries installed.

## Usage

To run the script, navigate to its directory and run:

```bash
python generate-marp-slide.py
```

### Command-Line Options

You can customize the script's behavior through the following command-line arguments:

- `--sections`: Specifies which sections to include in the final document.
  
  Example:

  ```bash
  python scripts/generate-marp-slides.py --sections top description
  ```

  This will include only the 'top' and 'description' sections in the final document.

  Current options are top, description, example, exercise and checklist

- `--levels`: Specifies which levels to include in the final document.
  
  Example:

  ```bash
  python scripts/generate-marp-slides.py --levels lv0 lv1
  ```

  This will include content of levels 'lv0' and 'lv1' in the final document.

  Current options are lv0, lv1, lv2 and lv3

- `--locale`: Specifies the locale to set the root directory.
  
  Example:

  ```bash
  python scripts/generate-marp-slides.py --locale ja
  ```

  This will set the root directory to `'contents/ja'`.

### Combining Options

You can combine multiple options as follows:

```bash
python scripts/generate-marp-slides.py --sections top description example exercise checklist --levels lv1 lv2 lv3 --locale en
```

## Contributing

Feel free to fork the repository and submit pull requests.
