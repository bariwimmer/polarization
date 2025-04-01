# Polarization Wave Calculator

A Python-based tool to simulate the behavior of polarized light interacting with optical elements using Jones calculus.

This program was developed as part of my undergraduate physics capstone at West Virginia University to aid in the planning and analysis of optics experiments. It allows users to input sequences of optical elements and view the resulting polarization state in various formats.

## ✨ Features

- User-friendly terminal interface
- Simulates the effect of:
  - Linear and circular polarizers
  - Quarter-wave and half-wave plates
  - Arbitrary wave plates and rotations
- Graphical outputs:
  - Polarization ellipse
  - Poincaré sphere
  - Stokes parameters
- Includes options to save visualizations as images

## 🛠 Tech Stack

- Python
- [Py-pol](https://pypi.org/project/py-pol/) library (MIT license)
- NumPy
- Matplotlib (for visual output)

## 📦 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/bariwimmer/polarization-wave-calculator.git
cd polarization-wave-calculator
pip install py-pol numpy matplotlib
