# retirement savings model:
# given a certain income, savings and interest rate,
# how long will it take to accumulate a required amount to retire
import numpy_financial as nf
def retirement(r, income, srate, threshold):
    c = income*srate
    years = nf.nper(r,c,0,threshold,0)
    return years
print(retirement(0.05, 60000, 0.25, 1500000))