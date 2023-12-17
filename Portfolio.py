import sys
print(f"Operating System Platform: {sys.platform}")
if __name__ == '__main__':
    import sys

    if __name__ == "__main__":
        num_arguments = len(sys.argv) - 1
        print(f"Number of arguments provided: {num_arguments}")
if __name__ == "__main__":
    import sys

    if __name__ == "__main__":
        arguments = sys.argv[1:]

        if not arguments:
            print("No arguments provided.")
        else:
            shortest_argument = min(arguments, key=len)
            print("Shortest argument:", shortest_argument)
import sys
import requests

def check_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"The website at {url} is working.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to {url}. Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_website.py <URL>")
    else:
        url = sys.argv[1]
        check_website(url)
if __name__ == "__main__":
    import sys


    def process_temperatures(temperatures):
        if not temperatures:
            print("No temperatures provided.")
            return

        temperatures = list(map(float, temperatures))
        print(f"Maximum Temperature: {max(temperatures)}")
        print(f"Minimum Temperature: {min(temperatures)}")
        print(f"Mean Temperature: {sum(temperatures) / len(temperatures)}")


    if __name__ == "__main__":
        arguments = sys.argv[1:]

        if not arguments:
            print("Usage: python temperature_stats.py <temperature1> <temperature2> ...")
        else:
            process_temperatures(arguments)
if __name__ == "__main__":
    import sys
    import shutil
    def create_backup(original_file):
        try:
            shutil.copy2(original_file, f"{original_file}.bak")
            print(f"Backup created successfully: {original_file}.bak")
        except FileNotFoundError:
            print(f"Error: File not found - {original_file}")
        except Exception as e:
            print(f"An error occurred: {e}")


    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: python backup_file.py <filename>")
        else:
            filename = sys.argv[1]
            create_backup(filename)