# Function to calculate and display cost for slab 1
def costSlab1(matrix):
    unit_range = "0 to 100"
    unit_cost = 10
    data = matrix[0]
    total_cost = sum(data) * unit_cost
    print(f"Bill for Slab 1 ({unit_range}): Rs. {total_cost}")

# Function to calculate and display cost for slab 2
def costSlab2(matrix):
    unit_range = "101 to 200"
    unit_cost = 15
    data = matrix[1]
    total_cost = sum(data) * unit_cost
    print(f"Bill for Slab 2 ({unit_range}): Rs. {total_cost}")

# Function to calculate and display cost for slab 3
def costSlab3(matrix):
    unit_range = "201 to 300"
    unit_cost = 20
    data = matrix[2]
    total_cost = sum(data) * unit_cost
    print(f"Bill for Slab 3 ({unit_range}): Rs. {total_cost}")

# Main menu function
def main_menu(student_id, matrix):
    while True:
        print("\nMy Student ID is", student_id)
        print("Enter your choice")
        print("Press 1 to display the bill of slab 1 and slab 2.")
        print("Press 2 to display the bill of slab 3.")
        print("Press any other key to exit.")

        choice = input("")

        if choice == '1':
            costSlab1(matrix)
            costSlab2(matrix)
        elif choice == '2':
            costSlab3(matrix)
        else:
            print("\nExiting the program.")
            break

# Source data
source_matrix = [
    [55, 65, 75],
    [120, 150, 170],
    [210, 230, 240]
]

# Student ID
student_id = "YourStudentID"

# Run the program
main_menu(student_id, source_matrix)
