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
- `requirements.txt` — required Python packages.
- GitHub Releases — standalone Windows executable.

## Purpose

This repository documents the computational tools developed for a scientific research project and demonstrates the use of Python for numerical data handling, scientific visualization, and interactive application development.

## Data and Attribution

The repository does not include the original scientific data files or external research resources used by the application.

These materials are excluded from the public distribution of the project.

## Installation and Usage

### Option 1: Standalone Windows Application

A Windows executable is available in the [GitHub Releases](https://github.com/JuliVillabona9/molecular-predissociation/releases) section.

Download the latest release and run the executable.

### Option 2: Run from Python Source Code

**Requirements**

- Python 3
- NumPy
- Matplotlib
- Tkinter (usually included with Python on Windows)

**Setup**

1. Download or clone this repository.
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Make sure the required data files and graphical resources are available in the expected `Data` directory.

**Run the application**

```bash
python Predis.py
```

**Note:** The Python source code requires external data files and graphical resources that are not included in this repository.

## Status

The source code and standalone Windows executable are available. Scientific data files are not distributed with this repository.
