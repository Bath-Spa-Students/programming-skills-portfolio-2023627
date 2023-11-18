def make_shirt(size="large", message="I love Python"):
    print(f"Making a {size}-sized shirt with the message: '{message}'")

# Call the function with the default values
make_shirt()  # Large shirt with default message

# Call the function with a medium shirt and default message
make_shirt("medium")

# Call the function with a custom size and message
make_shirt(size="small", message="Programming is fun!")
