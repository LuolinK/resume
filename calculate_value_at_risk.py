"""

This is the function to calculate the VaR.
It takes the data from yahoo finance.

Author: Kevin
Date； 2021-07-25

"""

import pandas_datareader.data as web


# Scarpping stock price from yahoo finance
def scrapping_data(company):
    df = web.DataReader(company, 'yahoo', start='2020-07-23', end='2021-07-23')
    return df


# Generate the daily return
def calc_daily_return(dataframe):
    daily_return = dataframe["Adj Close"].pct_change()
    return daily_return


# Generate daily return to a list
def generate_daily_return_list(daily_return):
    col_daily_return_list = daily_return.tolist()
    return col_daily_return_list


# Delete first figure
def get_new_list(col_daily_return_list):
    new_list = col_daily_return_list[1:]
    return new_list


# Sort list from smallest to biggest
def sort_list(new_list):
    sorted_list = sorted(new_list)
    return sorted_list


# Calculate VAR
def get_value_at_risk(company, quantile):
    scrapingdata = scrapping_data(company)
    daily_return = calc_daily_return(scrapingdata)
    col_daily_return_list = generate_daily_return_list(daily_return)
    new_list = get_new_list(col_daily_return_list)
    sorted_list = sort_list(new_list)
    var = sorted_list[int(round(quantile / 100 * len(sorted_list)))]
    return var


if __name__ == '__main__':
    example_var = get_value_at_risk("TSLA", 1)
    print(example_var)
