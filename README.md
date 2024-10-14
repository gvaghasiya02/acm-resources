# ACM Resources: Experiments & Analysis - Hash-Based vs. Sort-Based Group-By-Aggregate

This repository contains the supplemental material for the paper **"Hash-Based vs. Sort-Based Group-By-Aggregate: A Focused Empirical Study"** by Gaurav Vaghasiya and Shiva Jahangiri, presented at EDBT '25.

## Overview

This project provides the code, datasets, and configurations necessary to replicate the experiments and results discussed in the paper. It includes implementations of both hash-based and sort-based Group-By-Aggregate (GBA) query methods using Apache AsterixDB.

## Repository Structure

- `ACM/asterix-code.zip`: Contains the AsterixDB setup we used for the experiments. If it does not work use https://github.com/gvaghasiya02/asterixdb_gaurav/tree/Adaptivegroupby
- `ACM/Experiments/`: Scripts for loading data and running experiments.
- `ACM/32mb2nc2dpacmMetrics.csv`: Contains the results and metrics used in the paper.

## Prerequisites

- **Apache AsterixDB**: Installed and configured.
- A cluster setup with **2 NCs** (Node Controllers) and **2 IO devices** as described in the configuration.
- **Python 3.x**: Required for running the provided scripts and analyzing results.

## Data Generation

1. **Wisconsin Data Generation**:
   - Clone the repository [JSON-Wisconsin-Data-Generator](https://github.com/shivajah/JSON-Wisconsin-Data-Generator.git).
   - Use the configuration file `ACM/datagen/final.json` to generate datasets of sizes between 2 GB and 64 GB.
   - Scripts for running the data generation are included in the repository.

2. **TPC-H and TPC-DS Data**:
   - You can generate data from the official TPC-H and TPC-DS sites.
   - For **TPC-DS**, Apache AsterixDB provides an inbuilt way to build and load tables.
   - Use a **scale factor of 100** to generate the data for these benchmarks.

## Data Loading

The following scripts in the `ACM/Experiments/` directory will help load the respective datasets into AsterixDB. Be sure to adjust the file paths according to the data you have generated:

- **Wisconsin Cache Clear Dataset**:
  - Script: `ACM/Experiments/wisconfillerloadfinal.py`

- **Wisconsin Dataset Loading**:
  - Script: `ACM/Experiments/testopenload.py`

- **TPC-H Dataset Loading**:
  - Script: `ACM/Experiments/tpchload.py`

- **TPC-DS Dataset Loading**:
  - Script: `ACM/Experiments/tpcdsloadasterixdefault.py`

## Running Queries

You can run specific queries by configuring them in a `queries.txt` file and using the `query.py` script to execute them.

1. Select the queries from the **CSV file** provided.
2. Specify the queries in `queries.txt`.
3. Run the queries using:

   ```bash
   python query.py
