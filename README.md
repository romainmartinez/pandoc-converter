# Baby Shower Invitation Generator

This project automates the creation of personalized baby shower invitations using a Markdown template. Each invitation is generated as a PDF file from a list of guests in a CSV file.

## Features

- Reads guest information from a CSV file.
- Uses a Markdown template for easy customization of the invitation text.
- Generates a personalized PDF invitation for each guest using Pandoc.

## Prerequisites

- [Conda](https://docs.conda.io/en/latest/) for managing the project environment.

## Setting Up the Environment

```bash
conda env create
conda activate pandoc-converter
```

## Usage

1. Update the `guests.csv` file with the names and addresses of your guests.

2. Customize the invitation template in `templates/template.md` as needed.

3. Run the script to generate invitations:

```bash
python src/generator.py
```


