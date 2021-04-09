# introduction to python

# First Challenge
# Order App
# Calculate the total bill of given order

menu = {
    'SUMMER ROLLS': 13,
    'SPICY SALAD ROLLS': 14,
    'CRISPY BABY SQUID': 20,
    'SPRING ROLLS': 18,
    'SEAFOOD SPRING ROLL': 22,
    'CHICKEN WINGS': 19,
    'BEEF BETEL': 31,
    'PORK MEATBALLS': 28,
    'VIETNAMESE PANCAKE': 11,
}

def get_bill(orders): 
    # write your function that prints the total amount of the bill as 123$
    # Bonus if you can list all the items have been ordered with their cost before the total amount
        # eg: BEEF BETEL ......... 31 $
        #     CHICKEN WINGS ...... 19 $
        #     TOTAL .............. 50 $


# once function is ready, run it with following inputs
get_bill(['SUMMER ROLLS', 'SPRING ROLLS', 'BEEF BETEL'])
get_bill(['CHICKEN WINGS', 'SPRING ROLLS', 'BEEF BETEL', 'CHICKEN WINGS'])
get_bill(['SUMMER ROLLS', 'VIETNAMESE PANCAKE', 'PORK MEATBALLS'])
get_bill(['CHICKEN WINGS', 'SPICY SALAD ROLLS', 'BEEF BETEL', 'SEAFOOD SPRING ROLL', 'SPRING ROLLS'])