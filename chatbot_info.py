import re

def get_celebrity_info(celebrity_name, celebrity_data):
    match = None
    for entry in celebrity_data:
        if celebrity_name.lower() in entry['name'].lower():
            match = entry
            break

    if match:
        # Extract information using regular expressions
        date_of_birth = re.search(r'(?i)date\s*of\s*birth:\s*(\S+)', match['info'])        
        occupation = re.search(r'(?i)occupation:\s*(\S+)', match['info'])
        age = re.search(r'(?i)age:\s*(\S+)', match['info'])
        nationality = re.search(r'(?i)nationality:\s*(\S+)', match['info'])

        # Print the extracted information
        print(f'Date of Birth: {date_of_birth.group(1) if date_of_birth else "Invalid format"}')
        print(f'Occupation: {occupation.group(1) if occupation else "Invalid format"}')
        print(f'Age: {age.group(1) if age else "Invalid format"}')
        print(f'Nationality: {nationality.group(1) if nationality else "invalid format"}')
    else:
        print(f'Data not found')

# Example usage:
celebrity_data = [
    {'name': 'Bill Gates', 'info': 'Date of Birth: October 28, 1955\nOccupation: Businessman\nAge: 68\nNationality: American'},
    {'name': 'Ratan Tata', 'info': 'Date of Birth: December 28, 1937\nOccupation: Industrialist\nAge: 89\nNationality: Indian'},
    {'name': 'Narendra Modi', 'info': 'Date of Birth: September 17, 1950\nOccupation: Prime Minister\nAge: 73\nNationality: Indian'},
    {'name': 'Virat Kohli', 'info': 'Date of Birth: November 5, 1988\nOccupation: Cricketer\nAge: 35\nNationality: Indian'},
    {'name': 'Jeff Bejos', 'info': 'Date of Birth: January 12, 1964\nOccupation: Businessman\nAge: 59\nNationality: American'},
    # Add more celebrity data as needed
]

def main():
     print("Hi!, I am your chatbot\n")
     while True:
         user_input = input("Which celebrity information you need?, or type 'leave' to quit: ")
         if user_input.lower() == 'leave':
             print("Ok, Thank you")
             break
             
         else:
             celebrity_name = user_input
             print("Information of",(user_input))
             info =  get_celebrity_info(celebrity_name, celebrity_data)
             
if __name__ == "__main__":
    main()