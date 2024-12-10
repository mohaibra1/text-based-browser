import os
import sys

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created "soft" magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# Validate and format the filename from the URL
def format_filename(url):
    return url.split('.')[0]

# Save content to a file
def save_to_file(directory, filename, content):
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as file:
        file.write(content)

# Check if URL is valid
def is_valid_url(url):
    return '.' in url

# write your code here
def browser(directory):
    # Create directory if it doesn't exist
    if not os.access(directory, os.F_OK):
        os.mkdir(directory)
    else:
        pass # print(f"The directory '{directory}' already exists.")

    history_stack = []  # Stack to store browser history
    current_page = None  # Track the current page

    # User input loop
    while True:
        user_input = input().strip()

        if user_input == "exit":
            break

        # # Check if the input matches a saved file
        # filename = format_filename(user_input)
        # filepath = os.path.join(directory, filename)
        #
        # if os.path.isfile(filepath):
        #     with open(filepath, 'r') as file:
        #         print(file.read())

        elif user_input == "back":
            if history_stack:
                current_page = history_stack.pop()  # Go back to the previous page
                filename = format_filename(current_page)
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r') as file:
                    print(file.read())
            else:
                pass  # Notify user if stack is empty

        elif is_valid_url(user_input):
            if user_input == "bloomberg.com":
                content = bloomberg_com
            elif user_input == "nytimes.com":
                content = nytimes_com
            else:
                print("Invalid URL")
                continue

            # Save the current page to history before switching
            if current_page:
                history_stack.append(current_page)

            # Set new current page
            current_page = user_input
            filename = format_filename(user_input)
            save_to_file(directory, filename, content)
            print(content)

        else:
                print("Invalid URL")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python browser.py <directory_path>")
        sys.exit(1)
    else:
        browser(sys.argv[1])