import csv
import pandas as pd
import matplotlib.pyplot as plt

def getNextNotNumericIndex(start_index, line): 
    end_index = start_index
    for char in line[start_index + 1:]:
        if not char.isnumeric() and char != ',':
            return end_index+1
        end_index += 1

# Specify the path to your CSV file
csv_file_path = '../db/job_postings.csv'

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(csv_file_path, encoding='utf-8')
df = df.dropna(subset=['salary'])

def apply_salary_logic(salary):
    if "day" in salary:
        start_index = salary.find('€')
        end_index = getNextNotNumericIndex(start_index, salary)
        return float(salary[start_index + 1:end_index].strip().replace(',', '')) *5 * 4
    if "hour" in salary:
        start_index = salary.find('€')
        end_index = getNextNotNumericIndex(start_index, salary)
        return float(salary[start_index + 1:end_index].strip().replace(',', ''))*8 *5 * 4
    if "year" in salary:
        start_index = salary.find('€')
        end_index = getNextNotNumericIndex(start_index, salary)
        return float(salary[start_index + 1:end_index].strip().replace(',', ''))/12


# Apply the custom logic to each salary
df['salary'] = df['salary'].apply(apply_salary_logic)

result_df = df.groupby('company_industry')['salary'].mean().reset_index()

# Display the result
print(result_df)


result_df[['company_industry', 'salary']].plot.bar(x='company_industry', y='salary', legend=False, rot=30, fontsize=8)
plt.savefig('bar_plot.png')