# Construction Project MIS Analysis — West Bengal Operations

**Author:** Sandip Bhattacharya  
**Tools:** Python · Pandas · NumPy · Matplotlib · Looker Studio  

---

## Project Overview

This project analyzes **100 construction projects** across West Bengal (2019–2024) to identify cost overrun patterns, delay drivers, and project performance trends. The goal is to support management decision-making through structured MIS reporting and interactive dashboards — exactly the kind of reporting done in real operational environments.

The dataset is based on realistic construction project parameters drawn from 6+ years of hands-on civil engineering and project management experience in West Bengal's construction industry.

---

## Business Problem

Construction projects in India consistently face two critical challenges:

- **Cost overruns** — actual spend exceeding planned budget
- **Schedule delays** — projects running beyond planned timelines

Without structured data tracking and reporting, project managers cannot identify which project types, locations, or phases are most at risk — leading to reactive rather than proactive decision-making.

**This analysis answers 5 key business questions:**

1. Which project types have the highest cost overrun?
2. Which locations consistently underperform on budget?
3. What are the primary causes of project delays?
4. How many projects are at high financial risk (>30% overrun)?
5. What is the overall project health across the portfolio?

---

## Dataset Description

| Column | Description | Type |
|---|---|---|
| Project_ID | Unique project identifier (PKC-1000 to PKC-1099) | String |
| Project_Type | Type of construction project | Categorical |
| Location | City in West Bengal | Categorical |
| Contractor | Contracting firm name | Categorical |
| Phase | Current project phase | Categorical |
| Start_Date | Project start date (YYYY-MM-DD) | Date |
| Planned_Duration_Months | Original planned duration | Integer |
| Actual_Duration_Months | Actual time taken | Integer |
| Delay_Months | Months delayed beyond plan | Integer |
| Delay_Reason | Primary cause of delay | Categorical |
| Planned_Cost_Lakhs | Original budget in INR Lakhs | Float |
| Actual_Cost_Lakhs | Final actual cost in INR Lakhs | Float |
| Cost_Overrun_Pct | % cost over or under budget | Float |
| Project_Status | Current project status | Categorical |
| Quality_Score | Quality assessment score (0–100) | Integer |

**Project Types:** Residential Building, Commercial Complex, Road Construction, Bridge, Industrial Plant, Government Infrastructure, Housing Colony

**Locations:** Kolkata, Asansol, Durgapur, Siliguri, Howrah, Bardhaman, Haldia

---

## Key Findings

### Cost Overrun
- Average cost overrun across all 100 projects: **20.3%**
- **Bridge projects** have the highest overrun at **26.3%**
- **Government Infrastructure** has the lowest at **14.6%**
- **38 projects** classified as high-risk with >30% cost overrun
- **Haldia** is the highest overrun location at **24.6%**
- **Bardhaman** performs best at only **6.5%** overrun

### Schedule Delays
- Average delay across all projects: **5.3 months**
- **Bridge** and **Road Construction** projects most delayed at **6.1 months** avg
- **Equipment Failure** and **Regulatory Approval** are top delay causes (20 projects each)
- Only **8 out of 100** projects completed with zero delay

### Project Health
- 36 projects Completed
- 34 projects On Track
- 23 projects Delayed
- 7 projects At Risk

---

## Dashboard

An interactive MIS dashboard was built in **Looker Studio** connected to this dataset, featuring:

- KPI scorecards: Total Budget vs Actual Spend vs Avg Delay
- Cost overrun by project type (bar chart)
- Delay reasons distribution (pie chart)
- Project status overview (bar chart)
- High risk projects table (sortable)
- Interactive filters: Date Range, Project Type, Location

![MIS_DASHBOARD] (images/Dashboard.png)
---

## How To Run

```python
# Step 1 — Clone or download this notebook
# Step 2 — Run all cells in order
# Step 3 — Outputs generated:
#   construction_mis_dataset.csv  ← dataset
#   construction_mis_charts.png   ← analysis charts

# All libraries used are standard Kaggle environment libraries
# No additional installation required
```

---

## AD HOC 
```
Ad hoc means answering unplanned business questions on the fly using your data without building a new dashboard every time.

Performed ad hoc analysis answering 5+ business queries including contractor performance, phase-wise delay patterns, and quality-cost correlation
reducing management reporting time.
```

## Libraries Used

```python
import pandas as pd        # Data manipulation and analysis
import numpy as np         # Numerical operations
import matplotlib.pyplot   # Data visualization
import warnings            # Suppress warnings
```




## About The Author

Sandip Bhattacharya is a data analyst with 6+ years of operational experience in construction project management and an MTech from IIT Patna in Big Data & Blockchain. This project bridges domain expertise in civil engineering with data analytics skills to solve real operational reporting challenges.
