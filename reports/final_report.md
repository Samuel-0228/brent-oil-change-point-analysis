# Interim Report – Brent Oil Change Point Analysis

**Birhan Energies – Week 11 Challenge**  
**Date:** February 08, 2026  
**Author:** [Your Name / Team Name]

## 1. Business Understanding & Objective

The objective of this analysis is to detect structural breaks (change points) in historical Brent crude oil daily prices using Bayesian methods (PyMC), and to associate these breaks with major geopolitical, economic, and OPEC-related events from approximately 2012–2022.

**Target stakeholders:**

- Investors → better risk assessment and scenario planning
- Policymakers → energy security and economic stability insights
- Energy companies → operational planning, hedging, supply chain decisions

**Core question:**  
Which major events caused statistically detectable shifts in Brent oil price levels, and what was the approximate magnitude of these shifts?

## 2. Planned Analysis Workflow

1. **Business & Data Understanding**
   - Define problem and success criteria
   - Collect and explore Brent daily price data (1987–2022)
   - Curate list of 12–15 major events (2014–2022 focus)

2. **Data Preparation**
   - Parse dates, handle missing values
   - Compute log prices and daily log returns
   - Subset to most relevant period: 2012–2022
   - Save clean versions for modeling

3. **Exploratory Data Analysis (EDA)**
   - Visualize long-term trend and volatility patterns
   - Check for stationarity (ADF test planned)
   - Identify periods of extreme volatility clustering

4. **Modeling – Bayesian Change Point Detection**
   - Implement single change point model (Normal likelihood, switched means)
   - Extend to 2–3 change points if convergence allows
   - Use informative priors based on historical price ranges
   - MCMC sampling with diagnostics (trace plots, r̂, ESS)

5. **Interpretation & Causal Association**
   - Posterior distribution of change point locations (τ)
   - Compare detected dates with curated event list
   - Quantify mean shifts and credible intervals
   - Calculate approximate % price changes around events

6. **Communication & Dashboard**
   - Static report with key visuals and quantified statements
   - Interactive dashboard (Plotly Dash planned) showing prices, detected change points, and event markers
   - Executive summary suitable for policymakers/investors

## 3. Curated Key Events Dataset

A preliminary list of 12 major events (2014–2022) has been compiled in `data/external/events.csv`.  
Focus on well-documented supply shocks, demand collapses, OPEC decisions, and geopolitical crises.

| Date       | Event Description                                 | Category          | Expected Direction | Notes / Approx Move         |
| ---------- | ------------------------------------------------- | ----------------- | ------------------ | --------------------------- |
| 2014-11-27 | OPEC refuses production cut → price war begins    | OPEC policy       | ↓ strong           | $100+ → ~$30–50 by 2016     |
| 2016-01    | Price bottom after 2014–2015 glut                 | Supply glut       | Bottom             | ~$27–30 low                 |
| 2016-11-30 | First OPEC+ production cut agreement (~1.8 mb/d)  | OPEC+ cut         | ↑ recovery         | Start of multi-year rebound |
| 2018-05-08 | US withdraws from Iran deal + sanctions           | Sanctions         | ↑ risk premium     | Supported $70–80 range      |
| 2020-03-06 | Russia–Saudi price war begins                     | Price war         | ↓ sharp            | Precursor to April crash    |
| 2020-04-12 | Historic OPEC+ mega-cut (~9.7 mb/d)               | OPEC+ cut         | Stabilisation      | Recovery from lows          |
| 2020-04-20 | WTI briefly negative (storage crisis + COVID)     | Demand collapse   | Extreme ↓          | Brent ~$20–25 low           |
| 2021       | COVID demand recovery + OPEC+ discipline          | Demand rebound    | ↑ strong           | $20 → $80+ by late 2021     |
| 2022-02-24 | Russia invades Ukraine → sanctions & supply fears | Geopolitics / war | ↑ sharp spike      | $100 → $130–139 peak        |
| 2022-03    | Western sanctions intensify on Russian oil        | Sanctions         | ↑ risk premium     | Peak ~$133–139              |
| 2022-10-05 | OPEC+ announces 2 mb/d cut                        | OPEC+ cut         | ↑ support          | Prices supported in Q4 2022 |

(This list will be expanded/refined during full analysis.)

## 4. Initial EDA Findings (from notebooks 00_EDA & 01_data_prep)

- **Data coverage:** 1987-05-20 to 2022-09-30 (daily closing prices)
- **Modeling subset:** 2012-01-01 to 2022-09-30 (~2,700–2,800 observations)
- Long-term trend: strong upward movement 2010–2014, multi-year bear market 2014–2016, recovery 2016–2018, extreme volatility 2020, sharp spike 2022
- Volatility clustering clearly visible in log returns (high vol periods: 2008–09, 2014–16, 2020, 2022)
- Several extreme single-day moves visible around known crisis dates (March–April 2020, February–March 2022)

**Key visual observations (screenshots attached / described):**

- Raw price series shows non-stationary behavior with clear level shifts
- Log returns exhibit fat tails and volatility clustering → suggests potential benefit from modeling variance changes or using Student-t likelihood in future
- Preliminary event lines (2020-04, 2022-02) align with visible structural breaks in the series

## 5. Assumptions & Limitations (interim)

**Main assumptions:**

- Price segments can be approximated by normal distributions (or at least central tendency changes are meaningful)
- Change points are abrupt (no gradual transitions modeled yet)
- Major events are among the dominant drivers of large shifts

**Important limitations:**

- Statistical change point detection shows **correlation in time**, **not causation**
- Many confounding factors exist (USD strength, global demand, shale production, interest rates, etc.)
- Single change point model likely underfits (multiple regimes expected)
- Daily data is noisy → possible benefit from weekly/monthly aggregation in robustness checks
- MCMC convergence may be challenging with large N and weak priors on tau

## 6. Next Steps (until Feb 10 final submission)

- Complete & diagnose Bayesian single change point model
- Attempt 2–3 change point version
- Produce posterior plots and associate τ with event dates
- Quantify impacts with credible intervals
- Build minimal Plotly Dash dashboard
- Write full report with executive summary & policy-relevant insights

**GitHub link (main branch):** [insert your repo URL here]

**Prepared by:** [Your Name]  
**Submission status:** Interim – Task 1 + initial EDA complete
