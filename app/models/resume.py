from typing import List, Optional
from pydantic import BaseModel, field_validator
from enum import Enum


class ExpertiseLevel(str, Enum):
    beginner = 'beginner'
    intermediate = 'intermediate'
    advanced = 'advanced'
    expert = 'expert'


class Language(BaseModel):
    language: str
    fluency: Optional[str]

    @field_validator("fluency")
    def check_fluency(cls, v):
        if isinstance(v, str) and v != '':
            valid_inputs = [el.value for el in ExpertiseLevel]
            if v.lower() in valid_inputs:
                return v.lower()
        return ""


class Certification(BaseModel):
    title: str
    issuer: Optional[str]
    issue_date: Optional[str]
    expiry_date: Optional[str]


class Publication(BaseModel):
    title: str
    publisher: Optional[str]
    publication_date: Optional[str]


class Project(BaseModel):
    title: str
    description: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    duration: Optional[str]


class Award(BaseModel):
    name: str
    date_received: Optional[str]


class Reference(BaseModel):
    name: str
    designation: Optional[str]
    contact_info: Optional[str]


class Skill(BaseModel):
    skill_name: str
    expertise_level: Optional[str]

    @field_validator("expertise_level")
    def check_expertise_level(cls, v):
        if isinstance(v, str) and v != '':
            valid_inputs = [el.value for el in ExpertiseLevel]
            if v.lower() in valid_inputs:
                return v.lower()
        return ""


class Experience(BaseModel):
    title: str
    company: str
    start_date: Optional[str]
    end_date: Optional[str]
    description: Optional[str]


class Education(BaseModel):
    institution: str
    degree: str
    field_of_study: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    grade: Optional[str]


class Person(BaseModel):
    first_name: str
    last_name: str
    email: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    objective: Optional[str]
    skills: List[Skill]
    experience: List[Experience]
    education: List[Education]
    certifications: Optional[List[Certification]]
    languages: Optional[List[Language]]
    publications: Optional[List[Publication]]
    projects: Optional[List[Project]]
    awards: Optional[List[Award]]
    references: Optional[List[Reference]]

    @classmethod
    def from_json_str(cls, json_str: str) -> "Person":
        return Person.model_validate_json(json_str)
