# Covid19-LatentCases

Code to estimate the total number of SARS-CoV-2 infections based on limited diagnostic tests. A blog post describing details of this project can be found [here](https://blog.ml.cmu.edu/2020/06/12/understanding-the-prevalence-of-sars-cov-2-with-limited-diagnostic-testing-capacity/).

This model uses a single free parameter *c* to model the relative propensity of testing SARS-CoV-2-infected individuals compared to non-infected individuals. We use two strategies to estimate this free parameter *c*:
- Seroprevalence studies
- Symptomatic Rates

All of the experiments can be found in [`estimate_total_cases.ipynb`](https://github.com/blengerich/Covid19-LatentCases/blob/master/estimate_total_cases.ipynb). This notebook automatically downloads new data every day, so you can re-run if the results in this repository are out of date.

A few representative plots are shown below; results for all 50 states can be found in the [`results/`](https://github.com/blengerich/Covid19-LatentCases/tree/master/results) directory or [`estimate_total_cases.ipynb`](https://github.com/blengerich/Covid19-LatentCases/blob/master/estimate_total_cases.ipynb) notebook.

<img src="https://github.com/blengerich/Covid19-LatentCases/raw/master/results/NY.png" width="400px" alt="New York"><img src="https://github.com/blengerich/Covid19-LatentCases/raw/master/results/PA.png" width="400px" alt="Pennsylvania">
<img src="https://github.com/blengerich/Covid19-LatentCases/raw/master/results/MN.png" width="400px" alt="Minnesota"><img src="https://github.com/blengerich/Covid19-LatentCases/raw/master/results/AK.png" width="400px" alt="Alaska">
<img src="https://github.com/blengerich/Covid19-LatentCases/raw/master/results/legend.png" width="350px" alt="Legend">
