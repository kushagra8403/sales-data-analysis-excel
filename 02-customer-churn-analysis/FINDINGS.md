# Findings Framework

Run `src/generate_data.py` and `src/analyze.py` to reproduce the analysis. The analysis reports overall churn, active MRR, revenue at risk, churn by plan and churn by tenure.

## Questions for a BI review

- Which plans have the highest churn rate?
- How much monthly recurring revenue is associated with churned customers?
- Does churn concentrate among newer customers?
- Are high support contacts and lower satisfaction associated with churn?

## Business actions to test

- Review onboarding for early-tenure customers.
- Segment retention outreach by plan and risk indicators.
- Investigate customers with repeated support contacts and low satisfaction.
- Measure retention campaigns against a control group before scaling them.

## Limitation

The dataset is synthetic. Patterns demonstrate analytical method rather than real customer behaviour.
