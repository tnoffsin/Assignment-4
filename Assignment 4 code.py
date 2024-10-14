
def calculate_home_ownership_percentages(data):
    # Split the data into lines
    lines = data.strip().split('\n')
    
    # Extract the header and data rows
    header = lines[0].split(',')
    rows = [line.split(',') for line in lines[1:]]
    
    # Find the index of the home_ownership column
    home_ownership_index = header.index('home_ownership')
    
    # Initialize counters for each home ownership type
    ownership_counts = {'RENT': 0, 'OWN': 0, 'MORTGAGE': 0}
    total_customers = len(rows)
    
    # Count occurrences of each home ownership type
    for row in rows:
        home_ownership = row[home_ownership_index]
        if home_ownership in ownership_counts:
            ownership_counts[home_ownership] += 1
    
    # Calculate percentages
    ownership_percentages = {key: (value / total_customers) * 100 for key, value in ownership_counts.items()}
    
    return ownership_percentages

# Example usage
data = """customer_id,customer_age,customer_income,home_ownership,employment_duration,loan_intent,loan_grade,loan_amnt,loan_int_rate,term_years,historical_default,cred_hist_length,Current_loan_status
1,22,59000,RENT,123,PERSONAL,C,"£35,000.00",16.02,10,Y,3,DEFAULT
2,21,9600,OWN,5,EDUCATION,A,"£1,000.00",11.14,1,,2,NO DEFAULT
3,25,9600,MORTGAGE,1,MEDICAL,B,"£5,500.00",12.87,5,N,3,DEFAULT
4,23,65500,RENT,4,MEDICAL,B,"£35,000.00",15.23,10,N,2,DEFAULT
5,24,54400,RENT,8,MEDICAL,B,"£35,000.00",14.27,10,Y,4,DEFAULT
6,21,9900,OWN,2,VENTURE,A,"£2,500.00",7.14,1,N,2,DEFAULT
7,26,77100,RENT,8,EDUCATION,A,"£35,000.00",12.42,10,,3,NO DEFAULT
8,24,78956,RENT,5,MEDICAL,A,"£35,000.00",11.11,10,,4,NO DEFAULT
9,24,83000,RENT,8,PERSONAL,A,"£35,000.00",8.9,10,,2,NO DEFAULT
10,21,10000,OWN,6,VENTURE,C,"£1,600.00",14.74,1,N,3,DEFAULT
11,22,85000,RENT,6,VENTURE,A,"£35,000.00",10.37,10,,4,NO DEFAULT
12,21,10000,OWN,2,HOMEIMPROVEMENT,A,"£4,500.00",8.63,1,N,2,DEFAULT
13,23,95000,RENT,2,VENTURE,A,"£35,000.00",7.9,10,,2,NO DEFAULT
14,26,108160,RENT,4,EDUCATION,D,"£35,000.00",18.39,10,N,4,DEFAULT
15,23,115000,RENT,2,EDUCATION,A,"£35,000.00",7.9,10,,4,NO DEFAULT
16,23,500000,MORTGAGE,7,DEBTCONSOLIDATION,A,"£30,000.00",10.65,10,,3,NO DEFAULT
17,23,120000,RENT,0,EDUCATION,A,"£35,000.00",7.9,10,,4,NO DEFAULT
18,23,92111,RENT,7,MEDICAL,E,"£35,000.00",20.25,10,N,4,DEFAULT
19,23,113000,RENT,8,DEBTCONSOLIDATION,C,"£35,000.00",18.25,10,N,4,DEFAULT
20,24,10800,MORTGAGE,8,EDUCATION,A,"£1,750.00",10.99,4,N,2,DEFAULT
21,25,162500,RENT,2,VENTURE,A,"£35,000.00",7.49,10,,4,NO DEFAULT
22,25,137000,RENT,9,PERSONAL,D,"£34,800.00",16.77,10,Y,2,NO DEFAULT
23,22,65000,RENT,4,EDUCATION,C,"£34,000.00",17.58,10,N,4,DEFAULT
24,24,10980,OWN,0,PERSONAL,A,"£1,500.00",7.29,4,Y,3,NO DEFAULT
25,22,80000,RENT,3,PERSONAL,C,"£33,950.00",14.54,10,Y,4,DEFAULT"""

percentages = calculate_home_ownership_percentages(data)
print(percentages)


