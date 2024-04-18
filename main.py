from product import Product
from cart import Cart
import streamlit as st

# Function to display product details
def add_to_cart(product, quantity):

    cart.add_item(product, quantity)
    st.success(f"{quantity} {product.name} added to cart!")

# Function to display cart details
def show_cart():
    st.header("Your Cart")
    for item in cart.items:
        st.write(f"{item['quantity']} * {item['product'].name} - {item['product'].price} each")

    total_price = cart.calculate_total_price()
    if cart.free_delivery():
        st.write(f"Total Price: {total_price} (Free Delivery)")
    else:
        st.write(f"Total Price: {total_price} (+ 50 Delivery Charge if total < 1000)")
    st.write(f"Tax (18%): {cart.tax()}")
    st.write(f"Final Price: {cart.final_price():.2f}")


# Main Streamlit UI
if __name__ == "__main__":
    st.title("Online Shopping E-commerce Shop")

    cart = Cart()

    # Adding Products
    products = [
        Product("Laptop", 800),
        Product("Headphones", 50),
        Product("Mouse", 20),
        Product("Keyboard", 50)
    ]

    st.header("Products")
    for product in products:
        col1, col2 = st.columns([1, 3])
        quantity = col1.number_input(f"Quantity for {product.name}", min_value=0, step=1, value=0)
        if quantity > 0:
            add_to_cart(product, quantity)
        with col2:
            st.write(f"!!!{product.name}!!!\nPrice: {product.price}")

    # Display Cart
    show_cart()





# shopping cart


# main
# connecting both files
# product
# #product , quantity, price
#
# cart
# total price
# discount
# free delivery tax


#adding to the cart -
# product, quantity
