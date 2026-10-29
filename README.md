# Molecular Predissociation — Scientific Computing with Python

## Overview

This project explores molecular predissociation through a Python-based graphical application developed in the context of an undergraduate research project in theoretical chemistry.

The application provides an interactive environment for exploring molecular data and visualizing scientific results related to the electronic states of the nitrogen molecular ion, N₂⁺.

## Scientific Background

The project is related to research on the photoemission and predissociation rates of the C²Σᵤ⁺ electronic state of N₂⁺, including isotopic and temperature effects.

**Related scientific publication:**

Stemmle, C., Villabona, C. J., Forero, C., Paulus, B., & Pérez-Torres, J. F. (2020). *Isotopic and temperature effects on the photoemission and predissociation rates of N₂⁺(C²Σᵤ⁺).* Physical Review A, 102, 032802.

https://doi.org/10.1103/PhysRevA.102.032802

## Technologies

- Python
- NumPy — numerical data processing
- Matplotlib — scientific visualization
- Tkinter — graphical user interface

## Project Structure

- `Predis.py` — main Python application.
- `Data/` — numerical data files and graphical resources used by the application.

## Purpose

This repository documents the computational tools developed for a scientific research project and demonstrates the use of Python for numerical data handling, scientific visualization, and interactive application development.

## Data and Attribution

The project uses a combination of research data generated during the project and data provided by collaborators. Sources, permissions, and attribution requirements will be documented before public release.

## Status

Documentation and repository organization in progress.

## Installation and Usage

### Requirements

- Python 3
- NumPy
- Matplotlib
- Tkinter (usually included with Python on Windows)

### Setup

1. Download or clone this repository.
2. Make sure the `Data` directory is available in the project folder.
3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Run the application

Run the following command from the project root directory:

```bash
python Predis.py
```

**Note:** The application uses relative paths to load data files and graphical resources from the `Data` directory. The original directory structure must be preserved.
