# Card Python Power BI Example

## Overview

This script is designed to generate business card layouts representing sales information for different segments (Government, Midmarket, Enterprise). The generated cards include product details, sales data, and segment icons, all displayed in a visually appealing layout. The script can be used within **Power BI** as a "Python script" to generate customized business cards based on the specific sales data from the Power BI dataset.

## How It Works

The script takes in sales data, including:

- **Sales**: The sales amount for the product.
- **Country**: The country associated with the sales.
- **Product**: The product sold.
- **Segment**: The segment the product belongs to (Government, Midmarket, Enterprise).
- **Units Sold**: The quantity of units sold.
- **Discount Band**: The discount given on the product.

For each record, the script generates a card that:

- Displays the segment name as the title.
- Shows the product name, country, and sales performance details (units sold, discount band, sales value).
- Adds an icon representing the segment type (Government, Midmarket, Enterprise).

The layout dynamically adjusts to accommodate all records in the dataset, arranging the cards in a grid with a maximum of 5 cards per row.

### Features:
- Customizable card layout.
- Includes icons for each segment.
- Display of sales data, units sold, and product information.
- Automatically adjusts to the number of records.
- Can be used directly in Power BI as a Python script for visualization.

## Prerequisites

To use the Python script, you need install python.
link: https://www.python.org/downloads/

