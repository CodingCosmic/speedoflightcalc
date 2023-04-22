def calculate_speed_of_light(distance, speed):
    time = distance / speed
    return time

def main():
    speed_of_light = 299792458  # meters per second
    max_iterations = 5
    iteration = 0

    print("Welcome to the Speed of Light Calculator!")

    while iteration < max_iterations:
        # Get the user's desired constant speed
        constant_speed = float(input("Enter the desired constant speed (m/s): "))

        # Calculate the time it takes to travel the speed of light at the given constant speed
        time_to_travel = calculate_speed_of_light(speed_of_light, constant_speed)

        # Print the results
        print(f"Distance: {speed_of_light} meters")
        print(f"Constant speed: {constant_speed} m/s")
        print(f"Time to travel the speed of light: {time_to_travel} seconds")

        # Increment the iteration counter and ask if the user wants to calculate again
        iteration += 1
        if iteration < max_iterations:
            calculate_again = input("Would you like to calculate again? (y/n): ")
            if calculate_again.lower() != 'y':
                break

    print("Thank you for using the Speed of Light Calculator!")

if __name__ == "__main__":
    main()
