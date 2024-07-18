import csv
import matplotlib.pyplot as plt

# Define separate dictionaries for different categories
credit_card_services = {
    "OneCard": "CreditCard",
    "Simpl": "CreditCard",
    # Add more credit card services if needed
}

food_services = {
    "Zomato Private Limited": "Food",
    "shawrma": "Food",
    "dahi": "Food",
    "chips and Pepsi": "Food",
    "akshaj meal": "Food",
    "dahi": "Food",
    "paneer": "Food",
    "breakfast": "Food",
    "vv cake": "Food",
    "al Qureshi": "Food",
    "chaap": "Food",
    "ram laddu": "Food",
    "bread": "Food",
    "chaap": "Food",
    "juice": "Food",
    "gaane ka juice": "Food",
    "rajma chawal": "Food",
    "toast": "Food",
    "chicken": "Food",
    "chilli potato": "Food",
    "golle gappe": "Food",
    "food": "Food",
    "water": "Food",
    "bikaner party": "Food",
    "eggs": "Food",
    "meal": "Food",
    "shake": "Food",
    "shikanji": "Food",
    "kulche chole": "Food",
    "shake loan": "Food",
    "momo": "Food",
    "daksh subway": "Food",
    "Green Chick Cho": "Food"
    # Add more food services if needed
}

entertainment_services = {
    "outing sky jump": "Entertainment",
    "Mr PARTH KHARBA": "Entertainment",
    # Add more entertainment services if needed
}

sports_services = {
    "MEGA  SPORTS":"Sports",
    "grip and shuttl":"Sports",
    "badminton":"Sports",
    "cricket ke liye":"Sports",
    "box cricket":"Sports"
}

health_services = {
    "Kohat Medicos": "Health",
    "medicine":"Health",
    "SUKHCHAIN BAGGA":"Health",
    "dentist":"Health"
}

saving_services = {"savings":"Savings",
"sip":"Savings",
"monthly savings":"Savings",
"tata motors":"Savings",
"Savings":"Savings",
"kotak shares":"Savings",
"ipo investment":"Savings",
"groww invest lo":"Savings"
}

subscription_services = {
    "Google one":"Subscription"
}

travel_services = {
"Delhi Metro Rec":"Travel",
"Delhi Metro Rai":"Travel",
"metro recharge":"Travel",
"metro":"Travel",
"rapido":"Travel",
"Rapido":"Travel",
"ola bike":"Travel",
"parking":"Travel",
"ekta cab":"Travel",
"car parking":"Travel",
"UBER INDIA SYST":"Travel",
"UberRide":"Travel",
}

# Combine all dictionaries into one
service_categories = {**credit_card_services, **food_services, **entertainment_services, **sports_services, **health_services, **saving_services, **subscription_services, **travel_services}

def process_csv(file, service_categories):
    category_total = {}

    with open(file, mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # skip the header row
        for row in csv_reader:
            date = row[1]
            name = row[2]
            amount = float(row[3].replace("," , ""))  # convert to float
            category = "Misc"  # Default 

            for transaction in name.split("/"):  # Split the name
                if transaction in service_categories:
                    category = service_categories[transaction]
                    break
        
            if category in category_total:
                category_total[category] += amount
            else:
                category_total[category] = amount
    
    return category_total

def print_totals(category_total):
    for category, total in category_total.items():
        print(f"Total expenditure for {category} is {total}")
    print(f"Total Expenditure is {sum(category_total.values())}")

def plot_pie_chart(category_total):
    categories = list(category_total.keys())
    totals = list(category_total.values())

    plt.figure(figsize=(10, 6))
    plt.pie(totals, labels=categories, autopct='%1.1f%%', startangle=180)
    plt.title('Total Expenditure per Category')
    plt.axis('equal')
    plt.show()

file = "statement.csv"
category_total = process_csv(file, service_categories)
print_totals(category_total)
plot_pie_chart(category_total)
