#!/usr/bin/env python3

import sys

current_product = None
total_sales = 0.0
product_sales = []

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    parts = line.split('\t')

    if len(parts) != 2:
        continue

    product = parts[0]
    price = float(parts[1])

    if current_product == product:
        total_sales += price
    else:
        if current_product is not None:
            product_sales.append((total_sales, current_product))

        current_product = product
        total_sales = price

if current_product is not None:
    product_sales.append((total_sales, current_product))

product_sales.sort(reverse=True)

print("TOP 5 PRODUCTS BY SALES:")
print("=" * 40)

for i, (sales, product) in enumerate(product_sales[:5], start=1):
    print(f"{i}. {product}: ₹{sales:,.2f}")
