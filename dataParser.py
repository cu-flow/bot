import datetime

class DataParser: 

    #takes in a string of the course title and return a dictionary
    def parse_section_information(self, section_information=""):
        
        # Split into list of words
        words = section_information.split()

        # If there is no list of words, meaning empty string was passed in
        if (not words):
            raise ValueError("Empty string passed")
        
        # If there is only one word, meaning either not the full string was passed in or the string had no
        if (len(words) <= 1):
            raise ValueError("No spaces in string passed")

        keys = ["faculty", "course_code", "section", "tut_id"]
        values = {}

        for i in range(len(words)):
            if (i == 2 and len(words[i]) >= 2):
                values["section"] = words[i][0]
                values["tut_id"] = words[i][1]
            elif (i == 2 and len(words[i]) == 1):
                values["section"] = words[i][0]
                values["tut_id"] = None
            else:
                values[keys[i]] = words[i]

        # If section or tut_id not set, set them to None
        if ("section" not in values):
            values["section"] = None 
        if ("tut_id" not in values):
            values["tut_id"] = None               
            
        return values
    
    def parse_time(self, time=""):
        
        # If there is no list of words, meaning empty string was passed in
        if (time == ""):
            raise ValueError("Empty string passed")
        
        times = time.split("-")

        # If there is an invalid amount of '-'s
        if (len(times) != 2):
            raise TypeError("Invalid format: requires one and only one '-'")
        
        times = [time.strip() for time in times]

        values = {}
        values["start_time"] = datetime.time(int(times[0].split(":")[0]), int(times[0].split(":")[1]), 0, 0)
        values["end_time"] = datetime.time(int(times[1].split(":")[0]), int(times[1].split(":")[1]), 0, 0)
        
        
        return values
    
p = DataParser()

print(p.parse_time(""))