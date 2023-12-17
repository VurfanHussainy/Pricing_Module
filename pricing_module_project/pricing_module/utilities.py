from .models import PricingConfig


# # Example usage
# distance = 4  # Example distance in KMs
# time = 90  # Example time in minutes
# waiting_time = 210  # Example waiting time in seconds
# day_of_week = 'Tue'  # Example day of the week

# price = calculate_price(distance, time, waiting_time, day_of_week)
# print(f'The total price is: Rs {price}')

# def calculate_price(pricing_config, distance, time):
#     if pricing_config:
#         # Implement your pricing calculation logic using the provided formula
#         # For now, a simple calculation based on distace and time
#         return (pricing_config.dbp + (distance * pricing_config.dap)) + (time * pricing_config.tmf) + pricing_config.wc
#     else:
#         return None