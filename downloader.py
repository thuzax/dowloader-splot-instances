import sys
import requests

if __name__ == "__main__":
    base_link = "http://52.32.1.180:8080/SPLOT/models/"

    if (len(sys.argv) < 2):
        print("Required links file")
        exit(0)

    if (len(sys.argv) < 3):
        print("Required output location")
        exit(0)
    
    file_name = sys.argv[1]
    output_location = sys.argv[2]

    if (output_location[-1] != "/"):
        output_location = output_location + "/"


    with open(file_name, "r") as links_file:
        links = links_file.read().splitlines()

        for file_id, link in enumerate(links):
            output_name = output_location
            output_name += "splot-instance-" + str(file_id) + ".xml"
            response = requests.get(base_link + link)
            with open(output_name, 'wb') as output:
                output.write(response.content)