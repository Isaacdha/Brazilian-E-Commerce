import streamlit as st
import pandas as pd
import seaborn as sns
import folium
import branca.colormap as cm
from streamlit_folium import st_folium
import plotly.express as px
sns.set_style('whitegrid')

# Set page config
st.set_page_config(
    page_title="E-Commerce Analysis Dashboard",
    page_icon="🛍️",
    layout="wide"
)

# Function to load data
@st.cache_data
def load_customers():
    customers_df = pd.read_csv('Data/customers_dataset.csv', skiprows=1)
    customers_df['customer_city'] = customers_df['customer_city'].str.title()
    return customers_df

@st.cache_data
def load_geolocation():
    geolocation_df = pd.read_csv('Data/geolocation_dataset.csv', low_memory=False, skiprows=1)
    geolocation_df['geolocation_city'] = geolocation_df['geolocation_city'].str.title()
    geolocation_df.drop_duplicates(inplace=True)
    return geolocation_df

@st.cache_data
def load_orders():
    orders_df = pd.read_csv('Data/orders_dataset.csv', skiprows=1)
    orders_df['order_purchase_timestamp'] = pd.to_datetime(orders_df['order_purchase_timestamp'])
    orders_df['order_approved_at'] = pd.to_datetime(orders_df['order_approved_at'])
    orders_df['order_delivered_carrier_date'] = pd.to_datetime(orders_df['order_delivered_carrier_date'])
    orders_df['order_delivered_customer_date'] = pd.to_datetime(orders_df['order_delivered_customer_date'])
    orders_df['order_estimated_delivery_date'] = pd.to_datetime(orders_df['order_estimated_delivery_date'])
    return orders_df

@st.cache_data
def load_order_items():
    order_items_df = pd.read_csv('Data/order_items_dataset.csv', skiprows=1)
    order_items_df['shipping_limit_date'] = pd.to_datetime(order_items_df['shipping_limit_date'])
    return order_items_df

@st.cache_data
def load_order_payments():
    return pd.read_csv('Data/order_payments_dataset.csv', skiprows=1)

@st.cache_data
def load_order_reviews():
    order_reviews_df = pd.read_csv('Data/order_reviews_dataset.csv', skiprows=1)
    order_reviews_df['review_creation_date'] = pd.to_datetime(order_reviews_df['review_creation_date'])
    order_reviews_df['review_answer_timestamp'] = pd.to_datetime(order_reviews_df['review_answer_timestamp'])
    order_reviews_df['review_comment_title'].fillna('No Comments', inplace=True)
    order_reviews_df['review_comment_message'].fillna('No Comments', inplace=True)
    return order_reviews_df

@st.cache_data
def load_products():
    products_df = pd.read_csv('Data/products_dataset.csv', skiprows=1)
    products_df['product_category_name'].fillna('Other Categories', inplace=True)
    return products_df

@st.cache_data
def load_product_category_trans():
    return pd.read_csv('Data/product_category_name_translation.csv', skiprows=1)

@st.cache_data
def load_seller():
    seller_df = pd.read_csv('Data/sellers_dataset.csv', skiprows=1)
    seller_df['seller_city'] = seller_df['seller_city'].str.title()
    return seller_df

# Load data with caching
customers_df = load_customers()
geolocation_df = load_geolocation()
orders_df = load_orders()
order_items_df = load_order_items()
order_payment_df = load_order_payments()
order_reviews_df = load_order_reviews()
products_df = load_products()
product_category_trans_df = load_product_category_trans()
seller_df = load_seller()

# Load data
try:
    customers_df = load_customers()
    geolocation_df = load_geolocation()
    orders_df = load_orders()
    order_items_df = load_order_items()
    order_payment_df = load_order_payments()
    order_reviews_df = load_order_reviews()
    products_df = load_products()
    product_category_trans_df = load_product_category_trans()
    seller_df = load_seller()
except FileNotFoundError as e:
    missing_file = str(e).split("'")[1]
    st.error(f'File not found: {missing_file}. Please ensure all dataset files are in the "Data" directory of this script.')
    st.stop()

with open('.streamlit/style.css') as f:
    st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
# Sidebar
st.sidebar.image(".streamlit/Banner.webp", use_column_width=True)
st.sidebar.title("Brazillian E-Commerce Data Analysis")
st.sidebar.title("Navigation")
st.logo(".streamlit/Logo_Small.png", icon_image=".streamlit/Logo_Small.png", size="small")
page = st.sidebar.radio(
    "Select a Page",
    ["🏠 Overview", 
     "🌍 Customer Distribution", 
     "🚚 Delivery Analysis",
     "⭐ Customer Reviews",
     "📦 Product Analysis",
     "💳 Payment Analysis"]
)

# Add disclaimer for Customer Distribution page
if page == "🌍 Customer Distribution":
    st.sidebar.warning("Note: Loading the Customer Distribution page may take a while due to extensive use of folium for mapping and visualization.")

# Add credits to the bottom right corner
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        right: 0;
        width: 100%;
        text-align: right;
        padding: 10px;
        font-size: 12px;
        color: #888;
    }
    </style>
    <div class="footer">
        Created by @Isaacdha2024
    </div>
    """,
    unsafe_allow_html=True
)

# Overview Page
if page == "🏠 Overview":
    st.title("E-Commerce Analysis Dashboard")
    st.markdown("""
    This dashboard provides insights into various aspects of the brazillian e-commerce business:
    * 🌍 Customer Distribution
    * 🚚 Delivery Performance
    * ⭐ Customer Reviews
    * 📦 Product Analysis
    * 💳 Payment Methods
    """)
    
    st.markdown("Use the navigation bar on the left to explore different aspects of the e-commerce data.")
    # Key Metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Total Customers", customers_df["customer_unique_id"].nunique())
    with col2:
        st.metric("Total Orders", orders_df["order_id"].nunique())
    with col3:
        st.metric("Total Products", products_df["product_id"].nunique())
    with col4:
        st.metric("Average Rating", f"{order_reviews_df['review_score'].mean():.2f}")
    with col5:
        st.metric("Average Order Value", 
                 f"${order_payment_df['payment_value'].mean():.2f}")

    # Button to show profile of the maker
    with st.popover("About the Maker"):
        st.subheader("Coder Profile")
        st.write("Name: Isaac Dwadattusyah Haikal Azziz")
        st.write("Email: isaacazziz@gmail.com")
        st.write("LinkedIn: [Isaac's LinkedIn](https://id.linkedin.com/in/isaacdha)")
        
# Customer Distribution Page
elif page == "🌍 Customer Distribution":
    st.title("Customer Distribution Analysis")
    st.image(".streamlit/Border_H.png", use_column_width=True)
    st.subheader(" Q. Where are the majority of our customers located in and Which city has the highest and lowest number of orders?")
    
    st.markdown("")
    st.markdown("Lets answer the first question by visualizing the customer distribution in a map")
    st.markdown("")
    
    with st.container(border=True):
        # Customer Location Map
        st.markdown("#### Customer Distribution Map")
        st.markdown("")

        # Display prerendered customer distribution map
        st.image(".streamlit/Prerendered_Customer_Map.JPG", use_column_width=True, caption="This map is pre-rendered due to folium and st.map crashing the app when rendering with all customer locations.")
        
        st.markdown("The map shows the distribution of customers across Brazil, with the highest concentration of customers in the southeast region, particularly around the city of Sao Paulo. The northeastern and northern regions have fewer customers, indicating potential areas for growth and expansion.")
        
    st.markdown("Now, lets answer the second question by visualizing 15 city with the highest and lowest number of orders") 
    st.markdown("")
    
    with st.container(border = True):
        st.markdown("#### Top 15 Cities with the Highest and Lowest Number of Orders")
        # Merge orders_df with customers_df to include customer_city
        orders_with_city_df = pd.merge(orders_df, customers_df[['customer_id', 'customer_city']], on='customer_id')

        # Aggregate the number of orders in each city
        city_order_counts = orders_with_city_df.groupby('customer_city').size().reset_index(name='order_count')

        # Sort the cities by order count
        sorted_city_order_counts = city_order_counts.sort_values(by='order_count', ascending=False)

        # Select the top 15 and bottom 15 cities
        top_15_cities = sorted_city_order_counts.head(15)
        bottom_15_cities = sorted_city_order_counts.tail(15)
        
        # Create a Folium map centered around Brazil
        map_center = [-14.2350, -51.9253]  # Coordinates of Brazil
        city_order_map = folium.Map(location=map_center, zoom_start=4)

        # Add top 15 cities to the map with green markers
        for idx, row in top_15_cities.iterrows():
            city_data = geolocation_df[geolocation_df['geolocation_city'] == row['customer_city']]
            if not city_data.empty:
                city_data = city_data.iloc[0]
                folium.CircleMarker(
                    location=[city_data['geolocation_lat'], city_data['geolocation_lng']],
                    radius=10,
                    color='green',
                    fill=True,
                    fill_color='green',
                    popup=f"{row['customer_city']}: {row['order_count']} orders"
                ).add_to(city_order_map)

        # Add bottom 15 cities to the map with orange markers
        for idx, row in bottom_15_cities.iterrows():
            city_data = geolocation_df[geolocation_df['geolocation_city'] == row['customer_city']]
            if not city_data.empty:
                city_data = city_data.iloc[0]
                folium.CircleMarker(
                    location=[city_data['geolocation_lat'], city_data['geolocation_lng']],
                    radius=10,
                    color='orange',
                    fill=True,
                    fill_color='orange',
                    popup=f"{row['customer_city']}: {row['order_count']} orders"
                ).add_to(city_order_map)

        # Display the map
        st.markdown("City with high number of orders are marked in green, while city with low number of orders are marked in orange")
        st_folium(city_order_map, width='100%')
        st.markdown("Again, the areas with the highest number of orders are concentrated in the southeast of Brazil, around the city of Sao Paulo. On the other hand, the areas with the lowest number of orders are in the northeast of Brazil and the outskirts of large cities, which need more attention and infrastructure support to grow the number of orders from these areas.")

# Delivery Analysis Page
elif page == "🚚 Delivery Analysis":
    st.title("Delivery Time Analysis")
    st.image(".streamlit/Border_H.png", use_column_width=True)
    st.subheader(" Q. Which city experiences the longest delivery times, and which areas might benefit from infrastructure improvements?")
    
    st.markdown("")
    st.markdown("Before answering the question, Lets see the distribution of delivery time first")
    
    with st.container(border = True):
        # Calculate delivery times
        orders_df['delivery_time'] = (orders_df['order_delivered_customer_date'].astype('datetime64[ns]') - 
                                    orders_df['order_purchase_timestamp'].astype('datetime64[ns]')).dt.days
        
        # Distribution of delivery times
        st.markdown("#### Distribution of Delivery Times (Days)")
        fig = px.histogram(orders_df[orders_df['delivery_time'].between(0, 180)],
                        x='delivery_time',
                        nbins=180,
                        labels={'delivery_time': 'Delivery Time (Days)'})
        st.plotly_chart(fig)
        st.markdown("As we can see, most deliveries are made within 10 days, with a few outliers taking up to 30 days. However, some cities may experience longer delivery times that reached 180 days due to infrastructure issues or seller location.")
    
    st.markdown("")
    st.markdown("Now, lets see the cities with the longest average delivery times in a map")
    st.markdown("")
    
    with st.container(border = True):
        st.markdown("#### 30 Cities with Longest Average Delivery Times")
        # Calculate delivery time in days
        orders_with_city_df = pd.merge(orders_df, customers_df[['customer_id', 'customer_city']], on='customer_id')
        orders_with_city_df['delivery_time_days'] = (orders_with_city_df['order_delivered_customer_date'] - orders_with_city_df['order_purchase_timestamp']).dt.days

        # Aggregate the average delivery time for each city
        city_delivery_times = orders_with_city_df.groupby('customer_city')['delivery_time_days'].mean().reset_index()

        # Calculate the average latitude and longitude for each city
        city_avg_coords = geolocation_df.groupby('geolocation_city').agg({
            'geolocation_lat': 'mean',
            'geolocation_lng': 'mean'
        }).reset_index()

        # Merge the average coordinates with the city delivery times
        city_delivery_times = pd.merge(city_delivery_times, city_avg_coords, left_on='customer_city', right_on='geolocation_city')

        # Drop the old latitude and longitude columns and rename the new ones
        city_delivery_times.drop(columns=['geolocation_city'], inplace=True)
        city_delivery_times.rename(columns={'geolocation_lat': 'geolocation_lat', 'geolocation_lng': 'geolocation_lng'}, inplace=True)

        # Filter to only choose the top 15 cities with the longest delivery time
        city_delivery_times = city_delivery_times.nlargest(30, 'delivery_time_days')

        # Create a Folium map centered around Brazil
        map_center = [-14.2350, -51.9253]  # Coordinates of Brazil
        delivery_time_map = folium.Map(location=map_center, zoom_start=4)

        # Create a color map
        colormap = cm.LinearColormap(colors=['yellow', 'red'], vmin=city_delivery_times['delivery_time_days'].min(), vmax=city_delivery_times['delivery_time_days'].max())
        colormap.caption = 'Average Delivery Time (days)'

        # Add city delivery times to the map with gradient markers
        for idx, row in city_delivery_times.iterrows():
            folium.CircleMarker(
                location=[row['geolocation_lat'], row['geolocation_lng']],
                radius=10,
                color=colormap(row['delivery_time_days']),
                fill=True,
                fill_color=colormap(row['delivery_time_days']),
                popup=f"{row['customer_city']}: {row['delivery_time_days']:.2f} days"
            ).add_to(delivery_time_map)
            
        # Add the colormap to the map
        delivery_time_map.add_child(colormap)
        
        st_folium(delivery_time_map, width='100%')
        st.markdown("From the map showing areas with its average delivery time, it can be seen that the eastern coast, northeastern, and inland areas of Brazil experience high average delivery time. If infrastructure is to be built or evaluated, the eastern coast between the cities of Salvador and Fortaleza would benefit greatly because the number of cases of delays and their severity occur around these two cities.")
    
    st.markdown("")
    st.markdown("How about specific cities with the longest average delivery times? Lets see it in a bar chart") 
    st.markdown("")
    
    with st.container(border = True):
        # Cities with longest delivery times
        st.markdown("#### Top 10 Cities with Longest Average Delivery Times")
        
        orders_with_city = pd.merge(orders_df, customers_df[['customer_id', 'customer_city']], on='customer_id')
        avg_delivery_times = orders_with_city.groupby('customer_city')['delivery_time'].mean()
        longest_delivery_times = avg_delivery_times.nlargest(10)
        
        fig = px.bar(
            x=longest_delivery_times.index, 
            y=longest_delivery_times.values,
            labels={'x': 'City', 'y': 'Average Delivery Time (Days)'},
            color=longest_delivery_times.values,
            color_continuous_scale=['yellow', 'orange']
        )
        st.plotly_chart(fig)
        st.markdown("From the bar chart shown, it can be seen that the longest average delivery time is in the city of Novo Brasil and followed by the cities of Capinzal Do Norte and Adhemar De Barros. These cities are recommended to be evaluated and given infrastructure support to make the delivery of goods more efficient.")

# Customer Reviews Page
elif page == "⭐ Customer Reviews":
    st.title("Customer Reviews Analysis")
    st.image(".streamlit/Border_H.png", use_column_width=True)
    st.subheader(" Q. Which cities have lowest review scores, indicating a need for service evaluation in those areas?")
    
    st.markdown("")
    st.markdown("Before answering the question, Lets see the distribution of review scores first")
        
    with st.container(border = True):
        # Overall rating distribution
        st.markdown("#### Distribution of Review Scores")
        review_dist = order_reviews_df['review_score'].value_counts().sort_index()
        fig = px.bar(x=review_dist.index, 
                 y=review_dist.values,
                 labels={'x': 'Review Score', 'y': 'Count'},
                 color=review_dist.index,
                 color_continuous_scale=['red', 'blue'])
        st.plotly_chart(fig)
        st.markdown("Rating 5 is the most common rating, signifying that most customers are satisfied with their purchases. But, does that can represent all cities?")
    
    st.markdown("")
    st.markdown("Now, lets see the cities with lowest average review scores in a map")
    st.markdown("")
    
    with st.container(border = True):
        st.markdown("#### 30 Cities with Lowest Average Review Scores")
        
        # Calculate the average latitude and longitude for each city
        city_avg_coords = geolocation_df.groupby('geolocation_city').agg({
            'geolocation_lat': 'mean',
            'geolocation_lng': 'mean'
        }).reset_index()

        # Merge order_reviews_df with orders_df to get customer_id and customer_city
        reviews_with_city_df = pd.merge(order_reviews_df, orders_df[['order_id', 'customer_id']], on='order_id')
        reviews_with_city_df = pd.merge(reviews_with_city_df, customers_df[['customer_id', 'customer_city']], on='customer_id')

        # Calculate the number of ratings for each city
        city_rating_counts = reviews_with_city_df.groupby('customer_city').size().reset_index(name='rating_count')

        # Filter cities with at least 5 ratings
        cities_with_min_ratings = city_rating_counts[city_rating_counts['rating_count'] >= 5]['customer_city']

        # Filter reviews_with_city_df to include only cities with at least 5 ratings
        filtered_reviews_with_city_df = reviews_with_city_df[reviews_with_city_df['customer_city'].isin(cities_with_min_ratings)]

        # Calculate the average review score for each city
        city_avg_ratings = filtered_reviews_with_city_df.groupby('customer_city')['review_score'].mean().reset_index()

        # Sort the cities by average review score in ascending order
        sorted_city_avg_ratings = city_avg_ratings.sort_values(by='review_score')

        # Select the bottom 20 cities with the worst average rating
        bottom_30_cities_ratings = sorted_city_avg_ratings.head(30)

        # Merge with city_avg_coords to get the coordinates for each city
        bottom_30_cities_ratings = pd.merge(bottom_30_cities_ratings, city_avg_coords, left_on='customer_city', right_on='geolocation_city')
        
        # Create a Folium map centered around Brazil
        map_center = [-14.2350, -51.9253]  # Coordinates of Brazil
        rating_map = folium.Map(location=map_center, zoom_start=4)

        # Create a color map
        colormap = cm.LinearColormap(colors=['red', 'yellow'], vmin=bottom_30_cities_ratings['review_score'].min(), vmax=bottom_30_cities_ratings['review_score'].max())
        colormap.caption = 'Average Review Score'

        # Add city average ratings to the map with gradient markers
        for idx, row in bottom_30_cities_ratings.iterrows():
            folium.CircleMarker(
                location=[row['geolocation_lat'], row['geolocation_lng']],
                radius=10,
                color=colormap(row['review_score']),
                fill=True,
                fill_color=colormap(row['review_score']),
                popup=f"{row['customer_city']}: {row['review_score']:.2f} average rating"
            ).add_to(rating_map)

        # Add the colormap to the map
        rating_map.add_child(colormap)

        # Display the map
        st_folium(rating_map, width='100%')
        
        st.markdown("This map illustrates cities with the worst average scores are dominated by cities located in the southeastern and western coastal areas. Interestingly, only a few cities in central and northeastern Brazil have low average scores despite minimal infrastructure and sellers.")
        
    st.markdown("")
    st.markdown("Now lets focus on the top 10 cities with lowest average review scores, which city is it?")
    st.markdown("")
    
    with st.container(border = True):
        # Cities with lowest average reviews
        st.markdown("#### 10 Cities with Lowest Average Review Scores (Minimum 5 Reviews)")
        
        reviews_with_city = pd.merge(
            order_reviews_df,
            pd.merge(orders_df[['order_id', 'customer_id']], 
                    customers_df[['customer_id', 'customer_city']], 
                    on='customer_id'),
            on='order_id'
        )
        
        city_reviews = reviews_with_city.groupby('customer_city').agg({
            'review_score': ['mean', 'count']
        }).reset_index()
        
        city_reviews.columns = ['city', 'avg_score', 'review_count']
        city_reviews = city_reviews[city_reviews['review_count'] >= 5]
        worst_reviewed_cities = city_reviews.nsmallest(10, 'avg_score')
        
        fig = px.bar(worst_reviewed_cities,
                    x='city',
                    y='avg_score',
                    labels={'city': 'City', 'avg_score': 'Average Review Score'},
                    color='avg_score',
                    color_continuous_scale=['red', 'orange'])
        st.plotly_chart(fig)
        
        st.markdown("The bar chart highlights the 10 cities with the lowest average customer ratings, with Prudente De Morais, Abelardo Luz, and Iguaba Grande at the bottom. These cities may face recurring issues affecting customer satisfaction, suggesting areas for targeted service improvements. Addressing specific concerns in these locations could help boost overall customer ratings.")

# Product Analysis Page
elif page == "📦 Product Analysis":
    st.title("Product Analysis")
    st.image(".streamlit/Border_H.png", use_column_width=True)
    st.subheader(" Q. Which product categories have the highest and lowest sales?")
    
    st.markdown("")
    st.markdown("Lets see the most popular product categories by number of orders")
    
    # Merge product data
    products_with_category = pd.merge(
        order_items_df,
        pd.merge(products_df, product_category_trans_df, on='product_category_name'),
        on='product_id'
    )
        
    with st.container(border = True):
        # Top product categories
        st.markdown("#### Top 10 Product Categories by Number of Orders")
        
        category_orders = products_with_category['product_category_name_english'].value_counts().head(10)
        fig = px.bar(x=category_orders.index,
                y=category_orders.values,
                labels={'x': 'Category', 'y': 'Number of Orders'},
                color=category_orders.values,
                color_continuous_scale=['lightgreen', 'green'])
        st.plotly_chart(fig)
        st.markdown('Top 5 Product Categories: The "Bed_Bath_Table" category has the highest number of orders, followed closely by "Health_Beauty," "Sports_Leisure," and "Furniture_Decor." These categories demonstrate higher consumer demand, with "Computers_Accessories" rounding out the top five.')
        st.markdown("if managed properly, these categories could drive significant revenue growth.")
        
    st.markdown("")
    st.markdown("Now, lets see the bottom 10 product categories by number of orders")
    st.markdown("")
    
    with st.container(border = True):
        # Bottom product categories
        st.markdown("#### Bottom 10 Product Categories by Number of Orders")
        
        category_orders = products_with_category['product_category_name_english'].value_counts().tail(10)
        fig = px.bar(x=category_orders.index,
                y=category_orders.values,
                labels={'x': 'Category', 'y': 'Number of Orders'},
                color=category_orders.values,
                color_continuous_scale=['red', 'orange'])
        st.plotly_chart(fig)
        st.markdown('Bottom 5 Product Categories: The "Security_and_Services" category has the lowest number of orders, followed by "Fashion_Children_s_Clothes," "La Cuisine," "CD DVD Musical," and "Art/Craftmanship". These categories may require further evaluation to determine why they have lower demand compared to other categories.')
        st.markdown("Improving product quality, marketing, or pricing strategies could help boost sales in these categories.")

# Payment Analysis Page
elif page == "💳 Payment Analysis":
    st.title("Payment Analysis")
    st.image(".streamlit/Border_H.png", use_column_width=True)
    st.subheader(" Q. What are the most common payment methods, and how do they compare in terms of average purchase size?")
    
    st.markdown("")
    st.markdown("Lets see the distribution of payment methods first")
    
    with st.container(border = True):
        # Payment method distribution
        st.markdown("#### Distribution of Payment Methods")
        
        payment_dist = order_payment_df['payment_type'].value_counts()
        payment_dist = payment_dist[payment_dist > 1000]
        fig = px.pie(values=payment_dist.values,
                names=payment_dist.index)
        st.plotly_chart(fig)
        
        st.markdown("The pie chart shows that the most common payment method is credit card, followed by boleto, voucher, and debit card. These payment methods are widely used by customers, indicating a preference for convenience and security.")
    
    st.markdown("")
    st.markdown("Now, lets see the average purchase size by payment method")
    st.markdown("")
    
    with st.container(border = True):
        # Average purchase size by payment method
        st.subheader("Average Purchase Size by Payment Method")
        
        avg_purchase = order_payment_df.groupby('payment_type')['payment_value'].mean()
        avg_purchase = avg_purchase[avg_purchase.index != 'not_defined']
        fig = px.bar(x=avg_purchase.index,
                    y=avg_purchase.values,
                    labels={'x': 'Payment Method', 'y': 'Average Purchase Value ($)'})
        st.plotly_chart(fig)
        
        st.markdown("The bar chart illustrates the average purchase size for each payment method, with credit card having the highest average purchase value. Boleto and voucher have similar average purchase values, while debit card has the lowest. These insights can help businesses tailor marketing strategies to encourage higher-value purchases and increase revenue.")


