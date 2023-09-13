import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[['product_id']][(products['low_fats']=='Y') & (products['recyclable']=='Y')]