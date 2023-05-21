import numpy as np
import pandas as pd


def read_data(data):
    df = pd.read_csv('pizza-sales-data/' + data, encoding='latin1')
    return df

order = read_data('orders.csv')
order_detail = read_data('order_details.csv')
pizza = read_data('pizzas.csv')
pizza_type = read_data('pizza_types.csv')

orders_detail_merge = order.merge(order_detail, on = "order_id", how = "left")
pizza_merge = orders_detail_merge.merge(pizza, on = "pizza_id", how = "left")
pizza_type_merge = pizza_merge .merge(pizza_type, on = "pizza_type_id", how = "left")

pizza_type_merge.to_csv('pizza-sales.csv', index=False)