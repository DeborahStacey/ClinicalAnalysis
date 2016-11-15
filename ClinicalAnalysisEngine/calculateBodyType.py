## process_request.py
# Primary Owner: Cole Hoffele

import sys

#circumference of ribcage, and length of lower back leg, from knee to ankle
#Calculates the Feline Body Mass Index (FBMI) for a cat.
#ribcage and legLength (cm)
def calculateBodyType(ribcage, legLength):

    percentage = round(((((ribcage/0.7062) - legLength)/0.9156 ) - legLength),2)

    if percentage <= 25:
        bodyType = "Low"
    elif percentage > 25 and percentage <= 35:
        bodyType = "Moderate"
    elif percentage > 36 and percentage <= 45:
        bodyType = "High"
    elif percentage > 45 and percentage <= 55:
        bodyType = "Serious"
    elif percentage > 55 and percentage <= 65:
        bodyType = "Severe"
    elif percentage > 65
        bodyType = "Extreme"

    return bodyType



 #To learn her BMI, measure the circumference of her rib cage and then measure the length of her lower back leg,
 #from the knee to her ankle. Divide the rib cage number by 0.7062. Subtract the length of the leg.
 #Divide the result by 0.9156. Subtract the total by leg length.

 #According to VetInfo, a cat with a BMI of 42 or higher needs to lose weight.
