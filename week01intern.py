# Task 1 - Setting up the system and ordering the main items

# Arrays to store item code, description, and price
case_items = ["A1", "A2"]
case_descriptions = ["Compact", "Tower"]
case_prices = [75.00, 150.00]

ram_items = ["B1", "B2", "B3"]
ram_descriptions = ["8 GB", "16 GB", "32 GB"]
ram_prices = [79.99, 149.99, 299.99]

hdd_items = ["C1", "C2", "C3"]
hdd_descriptions = ["1 TB HDD", "2 TB HDD", "4 TB HDD"]
hdd_prices = [49.99, 89.99, 129.99]

# Function to display items and get user input
def display_and_choose(items, descriptions, prices, category):
    print("\nChoose a", category, ":")
    for i in range(len(items)):
        print(f"{i + 1}. {descriptions[i]} - ${prices[i]:.2f}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(items):
                return items[choice - 1], descriptions[choice - 1], prices[choice - 1]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to calculate the total price of the computer
def calculate_price(basic_set_price, case_price, ram_price, hdd_price):
    return basic_set_price + case_price + ram_price + hdd_price

# Main program
basic_set_price = 200.00

# Choose case, RAM, and HDD
chosen_case, chosen_case_description, case_price = display_and_choose(case_items, case_descriptions, case_prices, "case")
chosen_ram, chosen_ram_description, ram_price = display_and_choose(ram_items, ram_descriptions, ram_prices, "RAM")
chosen_hdd, chosen_hdd_description, hdd_price = display_and_choose(hdd_items, hdd_descriptions, hdd_prices, "Main Hard Disk Drive")

# Calculate total price
total_price = calculate_price(basic_set_price, case_price, ram_price, hdd_price)

# Display chosen items and total price
print("\nChosen items:")
print(f"Case: {chosen_case_description} - ${case_price:.2f}")
print(f"RAM: {chosen_ram_description} - ${ram_price:.2f}")
print(f"Main Hard Disk Drive: {chosen_hdd_description} - ${hdd_price:.2f}")
print(f"\nTotal Price: ${total_price:.2f}")




# Task 2 - Ordering additional items (extension of Task 1)

# Arrays for additional items
ssd_items = ["D1", "D2"]
ssd_descriptions = ["240 GB SSD", "480 GB SSD"]
ssd_prices = [59.99, 119.99]

second_hdd_items = ["E1", "E2", "E3"]
second_hdd_descriptions = ["1 TB HDD", "2 TB HDD", "4 TB HDD"]
second_hdd_prices = [49.99, 89.99, 129.99]

optical_drive_items = ["F1", "F2"]
optical_drive_descriptions = ["DVD/Blu-Ray Player", "DVD/Blu-Ray Re-writer"]
optical_drive_prices = [50.00, 100.00]

os_items = ["G1", "G2"]
os_descriptions = ["Standard Version", "Professional Version"]
os_prices = [100.00, 175.00]

# Function to choose additional items
def choose_additional_items(category_items, category_descriptions, category_prices, category_name):
    print(f"\nDo you want to purchase any {category_name} items?")
    print("1. Yes")
    print("2. No")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if choice == 1:
                return display_and_choose(category_items, category_descriptions, category_prices, category_name)
            elif choice == 2:
                return None, None, 0.00
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Choose additional items
chosen_ssd, chosen_ssd_description, ssd_price = choose_additional_items(ssd_items, ssd_descriptions, ssd_prices, "Solid State Drive")
chosen_second_hdd, chosen_second_hdd_description, second_hdd_price = choose_additional_items(second_hdd_items, second_hdd_descriptions, second_hdd_prices, "Second Hard Disk Drive")
chosen_optical_drive, chosen_optical_drive_description, optical_drive_price = choose_additional_items(optical_drive_items, optical_drive_descriptions, optical_drive_prices, "Optical Drive")
chosen_os, chosen_os_description, os_price = choose_additional_items(os_items, os_descriptions, os_prices, "Operating System")

# Update total price
total_price += ssd_price + second_hdd_price + optical_drive_price + os_price

# Display chosen additional items and updated total price
print("\nChosen additional items:")
if chosen_ssd:
    print(f"Solid State Drive: {chosen_ssd_description} - ${ssd_price:.2f}")
if chosen_second_hdd:
    print(f"Second Hard Disk Drive: {chosen_second_hdd_description} - ${second_hdd_price:.2f}")
if chosen_optical_drive:
    print(f"Optical Drive: {chosen_optical_drive_description} - ${optical_drive_price:.2f}")
if chosen_os:
    print(f"Operating System: {chosen_os_description} - ${os_price:.2f}")
print(f"\nUpdated Total Price: ${total_price:.2f}")



# Task 3 - Offering discounts (extension of Task 2)

# Function to apply discounts
def apply_discount(total_price, num_additional_items):
    if num_additional_items == 1:
        discount = 0.05
    elif num_additional_items >= 2:
        discount = 0.10
    else:
        discount = 0.00

    discount_amount = total_price * discount
    discounted_price = total_price - discount_amount

    return discount_amount, discounted_price

# Get the number of additional items
num_additional_items = sum(1 for item in [chosen_ssd, chosen_second_hdd, chosen_optical_drive, chosen_os] if item[0])

# Apply discounts
discount_amount, discounted_price = apply_discount(total_price, num_additional_items)

# Display discount information and final price
print(f"\nNumber of additional items purchased: {num_additional_items}")
print(f"Discount applied: {discount_amount:.2f}")
print(f"Final Price after Discount: ${discounted_price:.2f}")
