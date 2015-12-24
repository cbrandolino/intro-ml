#!/usr/bin/python

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []
    tuples_list = map(lambda x: (x[1][0], x[2][0], abs(x[0][0] - x[2][0])), zip(predictions, ages, net_worths))
    tuples_list.sort(lambda x, y: cmp(x[2], y[2]))
    cleaned_data = tuples_list[:81]
    
    return cleaned_data

