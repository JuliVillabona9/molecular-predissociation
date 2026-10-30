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

## Data Availability and Copyright

The scientific data files and graphical resources required to run the application are not included in this repository due to copyright and intellectual property restrictions.

**Important:** The application cannot run without these external files. Both the Python source code and the standalone Windows executable depend on the original data files and resources stored in the `Data` directory.

The omission of these files is intentional and does not reflect a limitation of the application itself.

For further information regarding data availability, academic collaboration, or questions about the project, please feel free to contact me.

## Installation and Usage

### Source Code

The repository provides the Python source code for reference and review.

**Requirements**

- Python 3
- NumPy
- Matplotlib
- Tkinter

To install the required packages:

```bash
pip install -r requirements.txt
```

To run the application:

```bash
python Predis.py
```

**Note:** Running the application requires the original `Data` directory, which is not publicly distributed.

### Standalone Windows Executable

A standalone Windows executable is available in the [GitHub Releases](https://github.com/JuliVillabona9/molecular-predissociation/releases) section.

The executable does not require a separate Python installation. However, it still depends on the external data files and graphical resources required by the application.

These files must be available in the expected directory structure for the application to run correctly.
