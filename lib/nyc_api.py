import requests

class GetPrograms:

    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        response = requests.get(URL)
        return response.json()  # This will parse the JSON response into Python data structures

    def program_agencies(self):
        programs_list = []
        programs = self.get_programs()  # This will already be a list of dictionaries
        for program in programs:
            if 'agency' in program:  # Make sure 'agency' key exists in the dictionary
                programs_list.append(program['agency'])
        return programs_list

# Example usage:
programs = GetPrograms()
agencies = programs.program_agencies()

for agency in set(agencies):
    print(agency)
  