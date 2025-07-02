# FinMark Data Pipeline – Milestone 2 (Data Analytics Track)
                    Refined Project Prototype (Draft 1)

## Overview

This project implements a basic data pipeline for FinMark with a focus on cleaning and validating raw financial transaction data.

##Folder Structure

```
finmark_pipeline/
├── data/
│   ├── raw/               # Raw dataset
│   └── processed/         # Cleaned dataset
├── scripts/               # Cleaning and schema validation scripts
├── config/                # YAML configuration
├── requirements.txt       # Dependencies
└── README.md              # Project summary
```

##  Key Features
- Raw CSV data cleaned and saved as processed CSV
- Schema validation using Pandera
- Configurable setup using YAML

##  Scripts
- `scripts/clean_data.py` – Cleans raw data using config rules
- `scripts/validate_schema.py` – Validates cleaned dataset schema

## What Worked
- Data was cleaned and saved correctly
- Schema validation passed

## Challenges
- Handling invalid dates and missing values
- Ensuring all types matched schema requirements

## Requirements
See `requirements.txt` for package dependencies.

## Team
**Track**: Data Analytics  
**Milestone**: 2  
**Project**: FinMark – Refined Data Pipeline  
-----------------------------------------------------
## Milestone 2 – Refined Project Prototype (Draft 2)

To strengthen the pipeline against missing or corrupted critical columns (like `transaction_amount`), we implemented:

- Schema checks for required columns (`user_id`, `transaction_amount`, `created_at`)
- Fallback logging that records issues in `logs/fallback_log.txt`
- Graceful skipping of bad files to keep the system running

This improves pipeline robustness and supports continuous ingestion without halting for isolated data issues.
