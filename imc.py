# Create an algorithm that calculates a person's BMI (body mass index)

# IMC = weight (kg) / height squared (m²)


def calculate_imc(weight: float, height: float) -> float:
    """
    
    Calculates the body mass index (BMI) from the provided weight and height.

    The body mass index (BMI) is calculated using the formula:
    BMI = weight (kg) / (height (m) ^ 2)

    Parameters:
    weight (float): The person's weight in kilograms.
    height (float): The person's height in meters.

    Returns:
    float: The calculated BMI value.

    """
    imc = weight / (height ** 2) 
    print(f"Your body mass index is: {imc}")
    return imc
    
weight = float(input("Please enter your weight: ")) 
height = float(input("Please enter your height: ")) 


calculate_imc(weight,height)