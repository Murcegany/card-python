import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import io
import urllib.request
import numpy as np
from PIL import Image

# Function to open an image from a URL
def open_image_from_url(url):
    with urllib.request.urlopen(url) as response:
        img_data = response.read()  
    return Image.open(io.BytesIO(img_data)) 

# URL Icons
segment_icons = {
    'Government': 'https://cdn-icons-png.flaticon.com/512/4474/4474140.png',
    'Midmarket': 'https://static.thenounproject.com/png/1958256-200.png',
    'Enterprise': 'https://cdn-icons-png.flaticon.com/512/484/484573.png'
}

# Function to assign colors based on the segment type
def segment_color(segment):
    colors = {
        'Government': '#DFF2E1',  
        'Midmarket': '#FFE5CC',  
        'Enterprise': '#E0E5FF'  
    }
    return colors.get(segment, '#FFFFFF')  

# Function to create a business card layout
def create_card(ax, segment, country, product, discount_band, units_sold, sales):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off') 
    
    # Background color for the card based on the segment
    background_color = segment_color(segment)
    ax.add_patch(patches.Rectangle((0, 0), 1, 1, linewidth=2, edgecolor='black', facecolor=background_color))
    
    # Title with the segment name
    ax.text(0.5, 0.9, f'{segment}', ha='center', va='center', fontsize=30, fontweight='bold', color='black')
    
    # Display product and country information
    ax.text(0.5, 0.75, f'Product: {product}', ha='center', va='center', fontsize=20, color='black')
    ax.text(0.5, 0.65, f'Country: {country}', ha='center', va='center', fontsize=20, color='darkblue')
    
    # Display sales performance information (discount band, units sold, sales)
    info = [
        (0.5, 0.5, f'Discount Band: {discount_band}', 'black'),
        (0.5, 0.4, f'Units Sold: {units_sold}', 'darkblue'),
        (0.5, 0.3, f'Sales: ${sales:,.2f}', 'green') 
    ]
    # Loop through the information and add it to the card
    for x, y, text, color in info:
        ax.text(x, y, text, ha='center', va='center', fontsize=20, color=color)
    
    # Add an icon that represents the segment
    icon_url = segment_icons.get(segment, None)  
    if icon_url:
        icon = open_image_from_url(icon_url) 
        ax.imshow(icon, extent=(0.4, 0.65, 0.05, 0.2), aspect='auto', zorder=2)

data = {
    'Sales': [10000, 15000, 20000, 25000, 30000, 12000, 18000, 22000, 28000],
    'Country': ['USA', 'Canada', 'UK', 'Germany', 'Australia', 'USA', 'Canada', 'Germany', 'Australia'],
    'Product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E', 'Product F', 'Product G', 'Product H', 'Product I'],
    'Segment': ['Government', 'Midmarket', 'Enterprise', 'Government', 'Enterprise', 'Midmarket', 'Enterprise', 'Government', 'Midmarket'],
    'Units Sold': [100, 150, 200, 250, 300, 120, 180, 220, 290],
    'Discount Band': ['10%', '15%', '20%', '25%', '30%', '15%', '10%', '20%', '25%']
}

df = pd.DataFrame(data)

df = df.drop_duplicates()

# Parameters for the layout of the business cards
max_cards_per_row = 5
num_cards = len(df) 
num_rows = (num_cards // max_cards_per_row) + (1 if num_cards % max_cards_per_row != 0 else 0)  

# create a subplot with enough space for all cards
fig, axs = plt.subplots(num_rows, max_cards_per_row, figsize=(5 * max_cards_per_row, 6 * num_rows))
plt.subplots_adjust(wspace=0.4, hspace=0.4)  

# adjust axs to handle a single row or column layout if needed
if num_rows == 1:
    axs = np.expand_dims(axs, axis=0)

# business cards
for i, (idx, row) in enumerate(df.iterrows()):
    row_idx, col_idx = divmod(i, max_cards_per_row) 
    ax = axs[row_idx, col_idx]
    create_card(ax, row['Segment'], row['Country'], row['Product'], row['Discount Band'], row['Units Sold'], row['Sales'])

# Remove any extra axes if there are less than the maximum number of cards per row
if num_cards < max_cards_per_row * num_rows:
    for i in range(num_cards, max_cards_per_row * num_rows):
        fig.delaxes(axs.flatten()[i])

plt.tight_layout()  
plt.savefig('business_cards.png', bbox_inches='tight') 
plt.show()
