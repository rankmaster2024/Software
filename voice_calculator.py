import androidhelper


qa_pairs = {}
# Define question-answer pairs
qa_pairs.update({
    # Class 1-3 Math Questions
    "what is addition": "Addition is the process of combining two or more numbers to get their total. For example, 2 + 3 = 5.",
    "what is subtraction": "Subtraction is the process of taking one number away from another. For example, 5 - 3 = 2.",
    "what is multiplication": "Multiplication is the process of finding the total of one number taken multiple times. For example, 3 times 2 equals 6.",
    "what is division": "Division is the process of splitting a number into equal parts. For example, 6 divided by 2 equals 3.",
    "what is a fraction": "A fraction represents a part of a whole. For example, 1/2 is a fraction representing one part out of two equal parts.",
    "what are shapes": "Shapes are forms such as circles, squares, triangles, and rectangles, each having different properties.",
    "what is counting": "Counting is the action of finding the total number of items in a group, such as 1, 2, 3, 4, and so on.",
    "what is zero": "Zero is a number that represents nothing or no quantity. It is the starting point in the number system.",
    "what is greater than": "Greater than means one number is larger than another. For example, 5 is greater than 3.",
    "what is smaller than": "Smaller than means one number is less than another. For example, 3 is smaller than 5.",

    # Class 4-6 Math Questions
    "what is a fraction and a decimal": "A fraction is a part of a whole, and a decimal is a number that represents a fraction in a different form. For example, 1/2 is 0.5 as a decimal.",
    "what is perimeter": "Perimeter is the total length of all sides of a shape. For example, the perimeter of a square is 4 times the length of one side.",
    "what is area": "Area is the amount of space inside a shape. For example, the area of a rectangle is its length times its width.",
    "what is a bar graph": "A bar graph is a way of showing data using rectangular bars to compare different categories or groups.",
    "what is a line graph": "A line graph is a type of chart used to show information that changes over time by connecting data points with a line.",
    "what is an average": "The average is the sum of a group of numbers divided by the total number of values. For example, the average of 3, 6, and 9 is 6.",
    "what is a fraction of a number": "To find a fraction of a number, you multiply the fraction by that number. For example, 1/2 of 10 is 5.",

    # Class 7-9 Math Questions
    "what is algebra": "Algebra is a branch of mathematics where symbols and letters represent numbers in equations. For example, in x + 2 = 5, x equals 3.",
    "what is an equation": "An equation is a statement that shows the equality of two expressions using an equals sign. For example, 2 + 3 = 5.",
    "what is a linear equation": "A linear equation is an equation between two variables that gives a straight line when plotted on a graph, like y = 2x + 3.",
    "what is a ratio": "A ratio compares two quantities, showing how many times one value contains or is contained within the other. For example, the ratio 3:1 means 3 for every 1.",
    "what is a percentage": "A percentage is a number or ratio expressed as a fraction of 100. For example, 50% means half of a whole.",
    "what is the circumference of a circle": "The circumference of a circle is the distance around it, given by the formula 2πr, where r is the radius.",
    "what is a square root": "The square root of a number is a value that, when multiplied by itself, gives the original number. For example, the square root of 9 is 3.",
    "what is probability": "Probability is the measure of how likely an event is to occur, expressed as a number between 0 and 1.",
    "what is a parallelogram": "A parallelogram is a four-sided shape where opposite sides are parallel and equal in length.",
    "what is a triangle": "A triangle is a shape with three sides and three angles. The sum of its interior angles is always 180 degrees.",

    # Class 10-12 Math Questions
    "what is trigonometry": "Trigonometry is the study of triangles, focusing on the relationships between their angles and sides. It deals with functions like sine, cosine, and tangent.",
    "what is a sine": "In trigonometry, sine is a function that relates the angle of a right-angled triangle to the ratio of the opposite side to the hypotenuse.",
    "what is a cosine": "In trigonometry, cosine is a function that relates the angle of a right-angled triangle to the ratio of the adjacent side to the hypotenuse.",
    "what is a tangent": "In trigonometry, tangent is a function that relates the angle of a right-angled triangle to the ratio of the opposite side to the adjacent side.",
    "what is calculus": "Calculus is the study of how things change, dealing with concepts such as limits, derivatives, and integrals.",
    "what is differentiation": "Differentiation is a concept in calculus that deals with finding the rate at which a quantity changes. For example, the derivative of x² is 2x.",
    "what is integration": "Integration is the inverse of differentiation in calculus. It finds the total accumulation of quantities, such as areas under curves.",
    "what is a quadratic equation": "A quadratic equation is an equation where the highest exponent of a variable is 2. It is written as ax² + bx + c = 0.",
    "what is the binomial theorem": "The binomial theorem gives a formula for expanding expressions that are raised to a power, like (x + y)ⁿ.",
    "what is a matrix": "A matrix is a rectangular array of numbers or symbols arranged in rows and columns, used in linear algebra.",
    "what is a logarithm": "A logarithm is the inverse of exponentiation. For example, if 2³ = 8, then the logarithm of 8 with base 2 is 3.",

    # Additional Miscellaneous Math Concepts
    "what is a polynomial": "A polynomial is a mathematical expression made up of variables and constants combined using addition, subtraction, and multiplication. For example, x² + 3x + 2 is a polynomial.",
    "what is a sequence": "A sequence is an ordered list of numbers that follow a specific pattern or rule. For example, 2, 4, 6, 8, 10 is a sequence of even numbers.",
    "what is a function": "A function is a relationship between inputs and outputs where each input has exactly one output. For example, f(x) = x + 2 is a function.",
    "what is a cubic equation": "A cubic equation is an equation in which the highest power of the variable is 3, such as x³ - 2x² + 3x - 1 = 0.",
    "what is the pythagorean theorem": "The Pythagorean theorem states that in a right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides.",
    "what is coordinate geometry": "Coordinate geometry, or analytic geometry, studies geometry using a coordinate system. It involves points, lines, and curves plotted on a graph.",
    "what is a hyperbola": "A hyperbola is a type of smooth curve lying in a plane, defined by its geometric properties or equations that relate to a fixed point and line.",
    "what is a prime number": "A prime number is a number greater than 1 that has no divisors other than 1 and itself.",
    "what is the fibonacci sequence": "The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.",
    "what is pi": "Pi, often represented as 3.14159, is the ratio of a circle's circumference to its diameter.",
    "what is the pythagorean theorem": "The Pythagorean theorem states that in a right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides.",
    "what is an algebraic expression": "An algebraic expression is a combination of numbers, variables, and arithmetic operations like addition, subtraction, multiplication, and division.",
    "what is calculus": "Calculus is the branch of mathematics that studies how things change, focusing on rates of change and the accumulation of quantities.",
    "what is a square number": "A square number is a number multiplied by itself. For example, 4 is a square number because it is 2 times 2.",
    "what is a factorial": "A factorial, denoted as n!, is the product of all positive integers less than or equal to n. For example, 5! is 5 × 4 × 3 × 2 × 1 = 120.",
    "what is the area of a circle": "The area of a circle is given by the formula pi times the radius squared, or A = πr².",
    "what is an even number": "An even number is any integer that is divisible by 2 without a remainder. Examples include 2, 4, 6, and so on.",
    "what is an odd number": "An odd number is any integer that is not divisible by 2, such as 1, 3, 5, and so on.",
    "what is a linear equation": "A linear equation is an equation between two variables that gives a straight line when plotted on a graph, like y = 2x + 3.",
    "what is the volume of a cylinder": "The volume of a cylinder is given by the formula V = πr²h, where r is the radius of the base and h is the height.",
    "what is a rational number": "A rational number is any number that can be expressed as the quotient or fraction of two integers, like 1/2 or 3/4.",
    "what is a polynomial": "A polynomial is a mathematical expression consisting of variables, coefficients, and exponents, combined using addition, subtraction, and multiplication.",
    "what is a matrix": "A matrix is a rectangular array of numbers or symbols arranged in rows and columns, used in linear algebra.",
    "what is trigonometry": "Trigonometry is the study of triangles, focusing on the relationships between their angles and sides. It deals with functions like sine, cosine, and tangent.",
    "what is a quadratic equation": "A quadratic equation is a second-degree equation in the form ax² + bx + c = 0, where a, b, and c are constants.",
    "what is probability": "Probability is the measure of how likely an event is to occur, expressed as a number between 0 and 1.",

    # Self-Referential Questions
    "who created you": "I was created by Deepak Mathur.",
    "who is deepak mathur": "Deepak Mathur is my creator, a developer passionate about creating intelligent systems like me.",
    "what is your purpose": "I am here to assist you with calculations, answering questions, and providing helpful responses.",
    "are you a real person": "No, I am not a person. I am a voice assistant created by Deepak Mathur to help with math and general queries.",
    "can you learn": "I can provide answers and help based on the information I was programmed with, but I don’t learn like humans.",
    "what can you do": "I can help with math problems, answer general knowledge questions, and assist with various tasks.",
    "what is your name": "I don't have a specific name, but you can call me anything you'd like.",
    "can you solve word problems": "I can solve some word problems related to math, but complex ones might require additional information or clarification.",
    "are you intelligent": "I am designed to provide helpful answers and calculations, but my intelligence is limited to the tasks I was programmed to perform.",
    "what languages do you speak": "I currently understand and communicate in English, but I can also handle simple mathematical symbols and terms.",
    "how do you work": "I take input, process it according to the information I was given, and provide an appropriate response based on my programming.",
    "can you talk to other machines": "I don’t directly interact with other machines, but I can help with questions about how machines work."

})

def speak_and_wait(droid, message):
    droid.ttsSpeak(message)
    while droid.ttsIsSpeaking().result:
        pass

def get_speech_input(droid):
    speak_and_wait(droid, "Speak your calculation.")
    result = droid.recognizeSpeech().result
    return result.lower() if result else None

def print_result(droid, result):
    speak_and_wait(droid, f"The result is {result}")

def replace_keywords(calculation):
    keywords_mapping = {
        "times": "*",
        "into": "*",
        "x": "*", 
        "multiply": "*",
        "square root of": "sqrt",
        "square": "**2",
        "cube": "**3",
        "factorial of": "factorial",
    }
    
    for keyword, replacement in keywords_mapping.items():
        calculation = calculation.replace(keyword, f"{replacement}")
    
    # Explicitly replace '√' with 'sqrt'
    calculation = calculation.replace("√", "sqrt")
    
    return calculation

def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def sqrt(x):
    return x ** 0.5


def check_if_question(input_text):
    for question in qa_pairs:
        if question in input_text:
            return qa_pairs[question]
    return None

def voice_calculator():
    droid = androidhelper.Android()

    speak_and_wait(droid, "Welcome to Voice Calculator. Please speak your calculation. Say 'exit' to end.")

    while True:
        result = get_speech_input(droid)
        
        if result == "exit":
            speak_and_wait(droid, "Exiting Voice Calculator. Goodbye!")
            break
        
        # Check if it's a question
        question_answer = check_if_question(result)
        if question_answer:
            speak_and_wait(droid, question_answer)
            continue
        
        # Handle calculation
        calculation = replace_keywords(result)

        try:
            if 'factorial' in calculation:
                n = int(calculation.split("factorial")[1])
                if n < 0:
                    speak_and_wait(droid, "Error: Factorial input must be a non-negative integer. Please try again.")
                    continue
                result = calculate_factorial(n)
            elif 'sqrt' in calculation:
                number = float(calculation.split("sqrt")[1])
                result = sqrt(number)
            else:
                result = eval(calculation)
            
            print_result(droid, result)
        except ZeroDivisionError:
            speak_and_wait(droid, "Error: Division by zero is not allowed. Please try again.")
        except (ValueError, SyntaxError):
            speak_and_wait(droid, "Error: Invalid input. Please try again.")
        except Exception as e:
            speak_and_wait(droid, f"An unexpected error occurred: {str(e)}. Please try again.")

if __name__ == "__main__":
    voice_calculator()