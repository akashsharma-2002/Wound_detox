import random

def handle_conditions(letter_list):
    for i in letter_list:
        if i == "b":
            print("Detected: Bruise\n")
            print(random.choice([
                "1. Rest the injured part. \n2. Ice it with a cold pack or ice wrapped in a cloth. \n3. Compress the area with an elastic bandage to reduce swelling.",
                "1. Apply Arnica cream to reduce swelling and pain. \n2. Cover the area with a protective gauze bandage. \n3. Take over-the-counter pain medication, such as acetaminophen, to relieve discomfort.",
                "1. Apply Vitamin K ointment on the bruise to help speed up healing. \n2. Use Aloe Vera gel to soothe the skin. \n3. Ensure adequate rest and protection of the bruised area.",
                "1. Elevate the injured area to reduce swelling. \n2. Apply a cooling gel to soothe the area. \n3. Consult a doctor if swelling or pain persists after a few days.",
                "1. Avoid applying heat to the bruised area for the first 24 hours. \n2. Limit movement and strain on the bruised area. \n3. Seek medical advice if the bruise does not improve within a week."
            ]))
        elif i == "l":
            print("Detected: Laceration\n")
            print(random.choice([
                "1. Clean the wound using hydrogen peroxide or saline solution. \n2. Dress the wound by applying an antibiotic ointment and a non-stick sterile bandage. \n3. Change the dressing every 24 hours to prevent infection.",
                "1. Clean the wound using chlorhexidine solution. \n2. Get a tetanus shot if not updated. \n3. Consider suturing by a medical professional if the cut is deep or jagged.",
                "1. Clean the wound using betadine solution. \n2. Apply a Steri-Strip to hold the edges of the wound together. \n3. Start an antibiotic course as prescribed to prevent infection.",
                "1. Stop bleeding by applying direct pressure with a clean cloth. \n2. Clean with saline water. \n3. Apply a pressure bandage and elevate the area until medical help arrives.",
                "1. Seek immediate professional medical treatment to assess the need for stitches. \n2. Avoid using fluffy cotton directly on the wound as it may stick. \n3. Cover with a hydrocolloid dressing for faster healing."
            ]))
        elif i == "c":
            print("Detected: Cut wound\n")
            print(random.choice([
                "1. Wash the wound with sterile saline or chlorhexidine. \n2. Apply Candid B ointment to prevent fungal infections. \n3. Cover the wound with a sterile adhesive bandage. \n4. Clean and change the bandage daily.",
                "1. Clean the wound with iodine solution. \n2. Apply Vicco Turmeric cream to promote healing and prevent infection. \n3. Use a waterproof bandage to protect the cut.",
                "1. Rinse the cut under running water to remove debris. \n2. Use an antibacterial soap gently around the wound. \n3. Apply a thin layer of Neosporin or similar antibiotic ointment.",
                "1. Keep the wound clean and dry to prevent infection. \n2. Apply a new, clean bandage daily. \n3. Monitor the wound for signs of infection like increased redness, swelling, or pus."
            ]))
        elif i == "s":
            print("Detected: Stab wound\n")
            print(random.choice([
                "1. Check to ensure that there isn’t much blood loss. \n2. Stop the bleeding by applying direct pressure with a clean cloth. \n3. Dial Emergency Services for immediate medical attention.",
                "1. Assess the wound for excessive bleeding. \n2. If there's significant bleeding, apply pressure and rush to the nearest hospital immediately.",
                "1. Clean the wound with a gentle antiseptic if the bleeding is controlled. \n2. Apply an antibacterial ointment such as Neosporin. \n3. Cover with a sterile bandage and",
                "1. Clean the wound with a gentle antiseptic if the bleeding is controlled. \n2. Apply an antibacterial ointment such as Neosporin. \n3. Cover with a sterile bandage and change it every 24 hours.",
                "1. Apply direct pressure to the wound with a clean bandage or cloth to control bleeding. \n2. Keep the injured area elevated. \n3. Seek professional medical attention as soon as possible.",
                "1. Control bleeding by applying direct pressure with a sterile gauze pad. \n2. Avoid removing any embedded objects as this could cause more damage or increase bleeding. \n3. Call emergency services for immediate assistance and keep pressure on the wound until help arrives."
            ]))
        elif i == "a":
            print("Detected: Abrasion\n")
            print(random.choice([
                "1. Clean the abrasion using Povidone Iodine to disinfect the area. \n2. Apply an antibiotic ointment such as Neosporin to prevent infection. \n3. Cover with a sterile bandage and change it as needed to keep the area clean.",
                "1. Gently clean the abrasion with Bacitracin to remove any dirt or debris. \n2. Apply a non-stick dressing to protect the abrasion from friction and contaminants. \n3. Take Amoxicillin as prescribed if there's a risk of bacterial infection.",
                "1. Rinse the abrasion under cool running water to clean out any foreign materials. \n2. Apply a layer of Aloe Vera gel to soothe and reduce inflammation. \n3. Cover with a clean gauze bandage and secure it with medical tape.",
                "1. Wash the abrasion with clean water and mild soap. \n2. Apply a hydrocolloid dressing to promote moist healing. \n3. Change the dressing daily or as needed to ensure cleanliness."
            ]))



# import requests
#
# # Function to map the first letter to a wound type
# def map_letter_to_wound_type(first_letter):
#     mapping = {
#         'b': 'bruise',
#         'l': 'laceration',
#         'c': 'cut',
#         's': 'stab wound',
#         'a': 'abrasion'
#     }
#     return mapping.get(first_letter, 'unknown')  # Default to 'unknown' if no match
#
# # Function to get treatment advice from Gemini API
# def get_treatment_advice(wound_type, api_key):
#     url = "https://generativelanguage.googleapis.com/v1beta/models/gemini:generateContent"
#     headers = {
#         'Authorization': f'Bearer {AIzaSyD0DAXRJjrK7EQwZK37lE7Zxm8oNgiKSTk}',
#         'Content-Type': 'application/json'
#     }
#     payload = {
#         "contents": [{"parts": [{"text": f"Provide treatment steps for a {wound_type}"}]}]
#     }
#     response = requests.post(url, json=payload, headers=headers)
#     if response.status_code == 200:
#         data = response.json()
#         return data['generated_text']  # Assume the key in response JSON where the advice is stored
#     else:
#         return f"Error: {response.status_code} - {response.text}"
#
# # Main function to handle conditions based on letters
# def handle_conditions(letter_list, api_key):
#     for first_letter in letter_list:
#         wound_type = map_letter_to_wound_type(first_letter)
#         if wound_type != 'unknown':
#             advice = get_treatment_advice(wound_type, api_key)
#             print(f"Detected wound: {wound_type.capitalize()}\nRecommended Treatment:\n{advice}")
#         else:
#             print("Wound type unknown based on the first letter provided.")

# # Example use-case, this should be replaced with the actual API key and letter list received from main.py
# if __name__ == "__main__":
#     example_letters = ['b', 'l', 's']  # Example list of first letters
#     api_key = "YOUR_API_KEY"  # Replace YOUR_API_KEY with your actual API key
#     handle_conditions(example_letters, api_key)