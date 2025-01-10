def count_words_in_file(output_file):
    try:
        # Sample text directly in the script
        text = """Hello world! This is a test file.
        It contains multiple lines of text, and we want to count the words."""
        
        # Split the text into words
        words = text.split()

        # Count the number of words
        word_count = len(words)

        # Prepare the output message
        result_message = f"Total number of words: {word_count}\n"

        # Open the output file in write mode and save the result
        with open(output_file, 'w') as result_file:
            result_file.write(result_message)

        print(f"Word count has been written to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the output file name
output_filename = 'output.txt'  # Replace with your desired output file name

# Call the function to count words and write the result
count_words_in_file(output_filename)
