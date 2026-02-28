#!/usr/bin/env python3
# MIT License
# 
# Copyright 2022 Broad Institute
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


TimestampKey = "Timestamp"
EmailKey = "Email"
FirstNameKey = "FirstName"
LastNameKey = "LastName"
FullNameKey = "FullName"
AffiliationKey = "Affiliation"
Affiliation2Key = "Affiliation2"
PhoneKey = "Phone"
LocationKey = "Location"
DriverKey = "Driver"
AccompanyKey = "Accompany"
SkillsKey = "Skills"
EveningsWeekendsKey = "EveningsWeekends"
WeekdaysKey = "Weekdays"
IndependentTasksKey = "IndependentTasks"
EnglishKey = "English"
SpanishKey = "Spanish"
PortugueseKey = "Portuguese"
OtherLanguageKey = "OtherLanguage"

EnumColumnKeys = frozenset([DriverKey, AccompanyKey,
                            EveningsWeekendsKey, WeekdaysKey,
                            IndependentTasksKey, EnglishKey,
                            SpanishKey, PortugueseKey])

BijanSignUpColNames = {
    TimestampKey: "Timestamp",
    EmailKey: "Email Address",
    FirstNameKey: "First Name / Primer Nombre",
    LastNameKey: "Last Name / Apellido",
    AffiliationKey: "Affiliation - congregation/organization // Afiliación - congregación/organización",
    PhoneKey: "Best phone number to reach you / el mejor número de teléfono para contactarlo                           (xxx-xxx-xxxx)",
    LocationKey: "Where do you live / Dónde vive usted? (city, town or neighborhood / ciudad, pueblo o barrio)",
    DriverKey: "Willing to provide a ride to court or visiting hours or home from the Burlington ICE office if needed / Dispuesto a llevar a la corte o al horario de visitas o a casa desde la oficina Burlington ICE si es necesario",
    AccompanyKey: "Willing to do court accompaniment in immigration court in downtown Boston / Dispuesto a acompañar las personas en la corte de inmigración en el centro de Boston",
    SkillsKey: "Special Skills (legal, medical, data entry, social work, counseling, education, ESL, organizing etc.) / Habilidades especiales (pericia legal, medical, la entrada de datos, trabajo social, terapia, educación, experiencia en organizaciones, etc.)",
    EveningsWeekendsKey: "Evening and weekend / noches y fines de semana",
    WeekdaysKey: "Daytime during the week / durante el día, los días de semana",
    IndependentTasksKey: "Available for email, writing, phone tasks on my own time / Disponible para hacer email, llamadas o escribir durante en mi horario",
    EnglishKey: "English / ingles",
    SpanishKey: "Spanish / español",
    PortugueseKey: "Portuguese / portugués",
    OtherLanguageKey: "Other languages / Otras idiomas",
}

TeamsForGSuiteColNames = {
    FirstNameKey: "First Name / Primer Nombre",
    LastNameKey: "Last Name / Apellido",
    AffiliationKey: "Affiliation - congregation/organization // Afiliación - congregación/organización",
    Affiliation2Key: "Affiliation2",
    EmailKey: "Best email to reach you / mejor email para contactarlo",
    PhoneKey: "Best phone number to reach you / el mejor número de teléfono para contactarlo                           (xxx-xxx-xxxx)",
    SkillsKey: "Special Skills (legal expertise, languages other than English, etc.) / Habilis especiales (pericia legal, idiomas que no sean inglés, etc.)",
    WeekdaysKey: "Daytime Weekday Availability",
    IndependentTasksKey: "Available for email, writing, phone tasks on my own time / Disponible para hacer email, llamadas o escribir durante en mi horario",
    DriverKey: "Willing to provide a ride to court or visiting hours or home from the Burlington ICE office if needed / Dispuesto a llevar a la corte o al horario de visitas o a casa desde la oficina Burlington ICE si es necesario",
    AccompanyKey: "Willing to do court accompaniment in immigration court in downtown Boston / Dispuesto a acompañar las personas en la corte de inmigración en el centro de Boston",
    LocationKey: "Where do you live / Dónde vive usted? (city, town or neighborhood / ciudad, pueblo o barrio)",
    EveningsWeekendsKey: "Evenings and Weekends?",
    EnglishKey: "English",
    SpanishKey: "Spanish",
    PortugueseKey: "Portuguese",
    OtherLanguageKey: "Other languages",
    TimestampKey: "Timestamp",
}

TeamsForGSuiteIgnoredColNames = [
    "Solidarity Rallies (Boston, daytime) / Manifestacions Públicas de solidaridad (Boston, durante el día)",
    "Solidarity Rallies (Boston, evening) / Manifestacions Públicas de solidaridad (Boston, durante noche)",
    "Organization(s)",
    "Timestamp",
    "Unnamed: 20",
    "Unnamed: 21",
    "Unnamed: 22",
    "Bos",
    "Check which teams you'd like to join:",
    "Your name",
    "City/Town where you live",
    "Team you're connected with (example: a congregation, a neighborhood group, SURJ, etc.)",
    "Email",
    "Phone number",

]

AirTableVolunteersColNames = {
    TimestampKey: "Sign-Up Date",
    EmailKey: "Email",
    FullNameKey: "Full Name",
    FirstNameKey: "First Name",
    LastNameKey: "Last Name",
    PhoneKey: "Phone",
    DriverKey: "Drivers/Transportation",
    AccompanyKey: ("In-Person Accompaniment", "Burlington Accompaniment?","Lowell Court Accompaniment?"),
    SkillsKey: "Special Skills?",
    EveningsWeekendsKey: "Evening/Weekend Availability",
    WeekdaysKey: "Weekday Availability",
    IndependentTasksKey: "Email, Writing, Phone Tasks?",
    EnglishKey: "English proficiency",
    SpanishKey: "Spanish proficiency",
    PortugueseKey: "Portuguese proficiency",
    OtherLanguageKey: "Other Languages",
}

InputTypeBijanSignUpGoogleForm = "form"
InputTypeTeamsForGSuite = "gsuite"
InputTypeAirTableVolunteers = "airtable"

LetterWritingVolunteersColNames = {
    TimestampKey: "Letter Writing Sign-up Date",
    EmailKey: "Email"
}