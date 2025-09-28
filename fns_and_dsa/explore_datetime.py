from datetime import datetime, timedelta

# --- Part 1: Display Current Date and Time ---


def display_current_datetime():
  """
  Gets the current date and time and prints it in a formatted string.
  """
  # Get the current datetime object
  current_date = datetime.now()

  # Format the datetime into "YYYY-MM-DD HH:MM:SS"
  formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")

  # Print the formatted string
  print(f"Current date and time: {formatted_datetime}")


# --- Part 2: Calculate a Future Date ---

def calculate_future_date():
  """
  Prompts for a number of days and calculates the date in the future.
  """
  try:
    # Prompt the user for the number of days
    days_to_add_str = input(
        "Enter the number of days to add to the current date: ")
    number_of_days = int(days_to_add_str)

    # Get the current date
    current_date = datetime.now()

    # Calculate the future date by adding a timedelta
    future_date = current_date + timedelta(days=number_of_days)

    # Format the future date into "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    # Print the result
    print(f"Future date: {formatted_future_date}")

  except ValueError:
    print("Invalid input. Please enter a valid integer.")


# --- Main Execution ---

if __name__ == "__main__":
  display_current_datetime()
  calculate_future_date()
