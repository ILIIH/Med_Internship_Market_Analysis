from dataclasses import dataclass

@dataclass
class LaborMarket:
    avg_salary: float 
    avg_additional_sal: float
    offers_amount: float

@dataclass
class JobEntity:
    salary: String 
    title: String
    country: String
    company_name: String