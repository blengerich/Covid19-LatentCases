# Covid19-LatentCases

Code to estimate the total number of SARS-CoV-2 infections based on limited diagnostic tests. 
This model uses a single free parameter to model the relative propensity of SARS-CoV-2-infected individuals to be tested compared to non-infected individuals. 

We use 2 strategies to estimate this free parameter:
- Seroprevalence studies
- Symptomatic Rates

All of the experiments can be found in `estimate_total_cases.ipynb`. This notebook automatically downloads new data every day, so you can re-run if the results in this repository are out of date.

A few representative plots are shown below; results for all 50 states can be found in the `results/` directory.

<img src="https://github.com/blengerich/Covid19-LatentCases/raw/master/results/NY.png" width="400px" alt="New York"><img src="https://github.com/blengerich/Covid19-LatentCases/raw/master/results/PA.png" width="400px" alt="Pennsylvania">
<img src="https://github.com/blengerich/Covid19-LatentCases/raw/master/results/MN.png" width="400px" alt="Minnesota"><img src="https://github.com/blengerich/Covid19-LatentCases/raw/master/results/AK.png" width="400px" alt="Alaska">
<img src="https://github.com/blengerich/Covid19-LatentCases/raw/master/results/legend.png" width="350px" alt="Legend">
