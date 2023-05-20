import numpy as np
import pandas as pd


def read_data(data):
    df = pd.read_csv('pizza-sales-data/' + data)
    return df

orders = read_data('orders.csv')
order_detail = read_data('order_details.csv')
pizza = read_data('pizzas.csv')
pizza_type = read_data('pizza_types.csv')

# merge_csv('orders.csv')
# data =DATA_PATH.joinpath('orders.csv').merge(DATA_PATH.joinpath('order_details.csv'), on= "order_id", how= "left")
print(orders)


