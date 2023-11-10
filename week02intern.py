# Task 1 - Start of the day

# Initialize data structures
train_journeys = {
    "09:00": {"up": {"available_seats": 480, "closed": False}, "down": {"available_seats": 480, "closed": False}},
    "11:00": {"up": {"available_seats": 480, "closed": False}, "down": {"available_seats": 480, "closed": False}},
    "13:00": {"up": {"available_seats": 480, "closed": False}, "down": {"available_seats": 480, "closed": False}},
    "15:00": {"up": {"available_seats": 480, "closed": False}, "down": {"available_seats": 480, "closed": False}},
}

# Constants
TICKET_PRICE = 25
GROUP_DISCOUNT_THRESHOLD = 10

# Display initial screen
def display_initial_screen():
    print("Welcome to the Electric Mountain Railway!")
    print("\nTrain Schedule:")
    for journey, directions in train_journeys.items():
        print(f"\n{journey}")
        for direction, details in directions.items():
            print(f"{direction.capitalize()} - Seats available: {details['available_seats']}")

# Call the function to display the initial screen
display_initial_screen()


# Task 2 - Purchasing tickets

# Function to get user input for ticket purchase
def get_ticket_input():
    # Get the number of passengers
    num_passengers = int(input("Enter the number of passengers: "))

    # Get the departure train journey
    print("Departure Train Schedule:")
    for i, (journey, directions) in enumerate(train_journeys.items(), start=1):
        print(f"{i}. {journey}")
    selected_departure_index = int(input("Select the departure train journey (1-4): ")) - 1

    # Get the return train journey
    print("Return Train Schedule:")
    for i, (journey, directions) in enumerate(train_journeys.items(), start=1):
        print(f"{i}. {journey}")
    selected_return_index = int(input("Select the return train journey (1-4): ")) - 1

    # Get the direction
    direction_options = ["up", "down"]
    print("Direction:")
    for i, direction in enumerate(direction_options, start=1):
        print(f"{i}. {direction.capitalize()}")
    selected_direction_index = int(input("Select the direction (1 for up, 2 for down): ")) - 1

    return num_passengers, list(train_journeys.keys())[selected_departure_index], list(train_journeys.keys())[selected_return_index], direction_options[selected_direction_index]

# Function to purchase tickets
def purchase_tickets():
    global train_journeys

    # Get user input
    num_passengers, selected_departure, selected_return, selected_direction = get_ticket_input()

    # Check if tickets are available for both departure and return journeys
    if (
        not train_journeys[selected_departure][selected_direction]["closed"]
        and not train_journeys[selected_return][selected_direction]["closed"]
        and train_journeys[selected_departure][selected_direction]["available_seats"] >= num_passengers
        and train_journeys[selected_return][selected_direction]["available_seats"] >= num_passengers
    ):
        # Calculate total price including group discount
        total_price = TICKET_PRICE * num_passengers
        num_groups = num_passengers // GROUP_DISCOUNT_THRESHOLD
        total_price -= TICKET_PRICE * num_groups

        # Update available seats and total money
        train_journeys[selected_departure][selected_direction]["available_seats"] -= num_passengers
        train_journeys[selected_return][selected_direction]["available_seats"] -= num_passengers
        total_money = total_price

        # Display updated screen
        print(f"\nTickets purchased for {num_passengers} passengers on the {selected_departure} {selected_direction} journey.")
        print(f"Return journey selected: {selected_return}")
        print(f"Total cost: ${total_price:.2f}")
        print(f"Seats available for {selected_departure} {selected_direction} journey: {train_journeys[selected_departure][selected_direction]['available_seats']}")
    else:
        print(f"\nTickets not available for {num_passengers} passengers on the chosen journeys.")

# Test the purchase_tickets function
purchase_tickets()


# Task 3 - End of the day

# Function to display end-of-day statistics
def display_end_of_day_stats():
    global train_journeys

    print("\nEnd of the day statistics:")
    for journey, directions in train_journeys.items():
        for direction, details in directions.items():
            passengers_traveled = 480 - details['available_seats']
            money_taken = 480 * TICKET_PRICE - details['available_seats'] * TICKET_PRICE
            print(f"{journey} {direction.capitalize()} - Passengers: {passengers_traveled}, Money taken: ${money_taken:.2f}")

    # Calculate and display total number of passengers and total amount of money taken for the day
    total_passengers_day = 1920 - sum(details['available_seats'] for directions in train_journeys.values() for details in directions.values())
    total_money_day = 1920 * TICKET_PRICE - sum(details['available_seats'] * TICKET_PRICE for directions in train_journeys.values() for details in directions.values())
    print("\nTotal passengers for the day:", total_passengers_day)
    print("Total money taken for the day: $", total_money_day)

    # Find and display the train journey with the most passengers
    max_passengers_journey = max(train_journeys, key=lambda journey: 480 - train_journeys[journey]["up"]["available_seats"])
    max_passengers_direction = "up" if (480 - train_journeys[max_passengers_journey]["up"]["available_seats"]) > (480 - train_journeys[max_passengers_journey]["down"]["available_seats"]) else "down"
    max_passengers = 480 - train_journeys[max_passengers_journey][max_passengers_direction]["available_seats"]
    print("\nTrain journey with the most passengers:", f"{max_passengers_journey} {max_passengers_direction.capitalize()} - Passengers: {max_passengers}")

# Test the display_end_of_day_stats function
display_end_of_day_stats()
