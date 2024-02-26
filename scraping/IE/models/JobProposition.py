from attr import dataclass

@dataclass
class Job:
    salary: str 
    name: str
    job_type: str
    location: str
    employer: str