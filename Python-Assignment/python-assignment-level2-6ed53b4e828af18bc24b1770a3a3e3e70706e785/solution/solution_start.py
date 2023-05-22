import argparse
import os
import json
import csv
import pandas as pd


def get_params() -> dict:
    parser = argparse.ArgumentParser(description='DataTest')
    parser.add_argument('--customers_location', required=False, default="./input_data/starter/customers.csv")
    parser.add_argument('--products_location', required=False, default="./input_data/starter/products.csv")
    parser.add_argument('--transactions_location', required=False, default="./input_data/starter/transactions/")
    parser.add_argument('--output_location', required=False, default="./output_data/outputs/")
    return vars(parser.parse_args())


def read_customers(customers_location: str) -> pd.DataFrame:
    customers_df = pd.read_csv(customers_location)
    return customers_df


def read_products(products_location: str) -> pd.DataFrame:
    products_df = pd.read_csv(products_location)
    return products_df


def read_transactions(transactions_location: str) -> pd.DataFrame:
    transactions=[]
    for root, dirs, files in os.walk(transactions_location):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as json_file:
                    data = json_file.readlines()
                    for line in data:
                        transaction = json.loads(line)
                        customer_id = transaction['customer_id']
                        date_of_purchase = transaction['date_of_purchase']
                        basket = transaction['basket']
                        for item in basket:
                            product_id = item['product_id']
                            price = item['price']
                            transactions.append({
                                'customer_id': customer_id,
                                'date_of_purchase': date_of_purchase,
                                'product_id': product_id,
                                'price': price
                            })

    transactions_df = pd.DataFrame(transactions)
    return transactions_df


def process_data(params: dict):
    customers_df = read_customers(params['customers_location'])
    products_df = read_products(params['products_location'])
    transactions_df = read_transactions(params['transactions_location'])
    
    merged_df = transactions_df.merge(customers_df, on='customer_id')
    merged_df = merged_df.merge(products_df, on='product_id')

    result_df = merged_df.groupby(['customer_id', 'loyalty_score', 'product_id', 'product_category']).size().reset_index()
    result_df.columns = ['customer_id', 'loyalty_score', 'product_id', 'product_category', 'purchase_count']

    output_location = params['output_location']
    os.makedirs(output_location, exist_ok=True)

    result_df.to_csv(os.path.join(output_location, 'result.csv'), index=False)
    result_df.to_json(os.path.join(output_location, 'result.json'), orient='records')
    result_df.to_parquet(os.path.join(output_location, 'result.parquet'), index=False)

def main():
    params = get_params()
    process_data(params)


if __name__ == "__main__":
    main()
