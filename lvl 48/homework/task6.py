def bmi(weight, height):
    # Calculate BMI
    bmi_value = weight / (height ** 2)
    
    # Return the appropriate category based on the BMI value
    if bmi_value <= 18.5:
        return "Underweight"
    elif bmi_value <= 25.0:
        return "Normal"
    elif bmi_value <= 30.0:
        return "Overweight"
    else:
        return "Obese"
