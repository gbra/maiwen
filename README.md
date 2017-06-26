# Maiwen
Modeling and Analysis Integration Workbench for the Engineering of embedded systems

## About
Maiwen enables to automatically analyse the properties of a system from a repository of multiple models and analyses. It supports:
1. Modeling languages AADL via Ocarina, and CPAL via the CPAL toolset 
2. Real-time scheduling analysis via the analysis module or through external tools (under development)
3. Orchestration of the analysis using contracts in Alloy

## Prerequisites
Python (developped and tested with Python 2.7.8)

For accessors: 
* Ocarina for AADL models (see https://github.com/OpenAADL/ocarina)
* cpal2x tool to generate CPAL models to the rt-format  (see https://www.designcps.com/binaries/)

To use the orchestration module:
* Alloy (see http://alloy.mit.edu/alloy/)

## Usage
1. Clone or download the repository

 ```
 git clone https://github.com/gbra/maiwen
 ```

2. Run the main script 

 ```
 python main.py
 ```

## Authors

* **Guillaume Brau** - *main developper* 

