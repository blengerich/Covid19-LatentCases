# Covid19-LatentCases

Code to estimate SARS-CoV-2 incidence based on changing numbers of diagnostic tests. Accompanies the manuscript:
["Disentangling Increased Testing from Covid-19 Epidemic Spread"](https://www.medrxiv.org/content/10.1101/2020.07.09.20141762v1.full.pdf).
A blog post describing details of this project can be found [here](https://blog.ml.cmu.edu/2020/06/12/understanding-the-prevalence-of-sars-cov-2-with-limited-diagnostic-testing-capacity/).

This model uses a single free parameter *c* to model the relative propensity of testing SARS-CoV-2-infected individuals compared to non-infected individuals. We use two strategies to estimate this free parameter *c*:
- Seroprevalence studies
- Symptomatic Rates

There are two sets of experiments: estimates of daily incidence can be found in ['estimate_daily_incidence.ipynb'](https://github.com/blengerich/Covid19-LatentCases/blob/master/estimate_daily_incidence.ipynb), while estimates of cumulative incidence can be found in [`estimate_total_cases.ipynb`](https://github.com/blengerich/Covid19-LatentCases/blob/master/estimate_total_cases.ipynb). These notebooks automatically download new data every day, so you can re-run if the results in this repository are out of date.

A few representative plots are shown below; results for all 50 states can be found in the [`results/`](https://github.com/blengerich/Covid19-LatentCases/tree/master/results) directory.

<img src="https://github.com/blengerich/Covid19-LatentCases/raw/master/results/NY.png" width="400px" alt="New York"><img src="https://github.com/blengerich/Covid19-LatentCases/raw/master/results/PA.png" width="400px" alt="Pennsylvania">
<img src="https://github.com/blengerich/Covid19-LatentCases/raw/master/results/MN.png" width="400px" alt="Minnesota"><img src="https://github.com/blengerich/Covid19-LatentCases/raw/master/results/AK.png" width="400px" alt="Alaska">
<img src="https://github.com/blengerich/Covid19-LatentCases/raw/master/results/legend.png" width="350px" alt="Legend">
