import re

#1 Course Code Validator (Using basic string checks)
def is_valid_course_code(code):
    
    if len(code) == 5:
        letters = code[0:2]
        numbers = code[2:5]
    elif len(code) == 6:
        letters = code[0:3]
        numbers = code[3:6]
    else:
        return False 
    
    is_valid_letters = letters.isalpha() and letters.isupper()
    
    
    is_valid_numbers = numbers.isdigit()
    
    
    if is_valid_letters and is_valid_numbers:
        return True
    else:
        return False
#2 Hex Color Validator (Using basic loops)

def is_valid_hex_color(color):
    if len(color) != 7:
        return False
        
    if color[0] != '#':
        return False
        
    allowed_characters = "0123456789abcdefABCDEF"
    
    for char in color[1:7]:
        if char not in allowed_characters:
            return False 
    return True 
#3 Sum of Numbers in a Paragraph (Building numbers character by character)
def sum_numbers_in_paragraph(paragraph):
    total_sum = 0
    current_number = ""
    
    for char in paragraph:
        if char.isdigit():
            current_number = current_number + char
        else:
            if current_number != "":
                total_sum = total_sum + int(current_number)
                current_number = ""
                
    if current_number != "":
        total_sum = total_sum + int(current_number)
        
    return total_sum


#4 Redact Phone Numbers (Using re module)
def redact_phone_numbers(document):

    pattern = r'\+84\d+|\b\d{10}\b'
    redacted_document = re.sub(pattern, '[REDACTED]', document)
    
    return redacted_document


#5 Monte Carlo Pi Approximation
def approximate_pi():
    
    user_input = input("How many random points to generate? ")
    
    total_points = int(user_input)
    
    points_inside_circle = 0
    
    for _ in range(total_points):
        x = int.uniform(-1, 1)
        y = int.uniform(-1, 1)

        distance = (x * x) + (y * y)
        
        if distance < 1:
            points_inside_circle = points_inside_circle + 1

    pi_approx = 4 * (points_inside_circle / total_points)
    
    print("Approximated value of pi is:", pi_approx)


if __name__ == "__main__":
    print("--- Task 1 Tests ---")
    print("TEC001:", is_valid_course_code("TEC001")) 
    print("math101:", is_valid_course_code("math101")) 

    print("\n--- Task 2 Tests ---")
    print("#FF5733:", is_valid_hex_color("#FF5733")) 
    print("#ffg733:", is_valid_hex_color("#ffg733")) 

    print("\n--- Task 3 Test ---")
    para = "Today is January 16, 2025. The temperature is 11 degrees Celsius."
    print("Sum:", sum_numbers_in_paragraph(para)) 

    print("\n--- Task 4 Test ---")
    doc = "You may reach Mr. Atkinson through his office number: +842439999999 during work hours, or his cell phone number: 0987654321,"
    print(redact_phone_numbers(doc))

    print("\n--- Task 5 Execution ---")