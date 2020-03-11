# just_scraping_by
“Just Scraping By” Data Deliverable

Hypothesis: After ACA’s major provisions went into effect in 2014, there was a statistically significant difference in preventative care for low income Americans. 

—————————————————————————————————————————————

I. Where the Health Data is From 
The health data in this file is a collection of phone polls from the years 2014-2018 from the Behavioral Risk Factor Surveillance System. Each row represents a voluntary participant in the phone poll that asked an upwards of 450 questions. The participant could end the call at any time or opt out of a question. 

—————————————————————————————————————————————

II. Format of the Rows

Each line in the file contains one participant in the phone interview. Below is an example:

xstate = 1 imonth = 5 Genhealth = 1…etc.

a. Xstate - the state the interviewee is from (1= Alabama, 2 = Alaska, 3 = Arizona, etc.)

b. Imonth - the month of the interview(1 = January, 2 = February… etc.)

c. Genhlth - general health of the participant (integer value 1-7,9 where 1 is excellent and 5 is poor, 7 is not sure and 9 is refused)

d. Physhlth- physical health : for how many days in the past 30 days was your health not good (integer between 1-30, 88 = None, 77 = not sure, 99 = refused)

e. Poorhlth- poor physical or mental health: how many days did your poor physical or mental keep you from doing your usual activities (integer between 1 and 30, 88 = None, 77 = not sure, 99 = refused )

f. Hlthpln1 - health plan: do you have any health care coverage? (1 = yes, 2 = no, 7 = not sure, 9 = refused)

g. Persdoc2- personal doctor: Do you have one person you think of as your personal doctor or health care provider? (1= yes, one, 2= more than one, 3 = no, 7 = not sure, 9 = refused)

h. medcost- could not see doctor because of cost: Was there a time in the past 12 months when you needed to see a doctor but could not because of cost? (1 = yes, 2 = no, 7 = not sure, 9 = refused)

I. Checkup1- length of time between last checkup (1 = less than 12 months ago, 2 = over 1 year but less than 2, 3= over 2 years but less than 5 years, 4 = 5 or more years, 7 = not sure, 8 = never, 9 = refused)

j. Exerany2- exercise: did you participate in any physical activity besides your job in the past month?(1= yes, one, 2= more than one, 3 = no, 7 = not sure, 9 = refused)

k. sex- what is your sex: (1 = male, 2 = female, 7 = not sure, 9 = refused)

l. educa- education level: What is the highest grade or year of school you completed? ( 1 = never attended school, 2 = elementary/middle school(grades 1 -8), 3 = high school (grades 9-11), 4 = high school graduate(12 or GED), 5 = college (1-3 years), 6 = college ( 4 years or more), 9 = refused)

m. Employ1- employent status: what is your current employment status? (1 = employed for wages, 2 = self-employed, 3 = out of work for 1 year or more, 4 = out of work for less than 1 year, 5 = a homemaker, 6 = a student, 7 = retired, 8 = unable to work, 9 = refused)

n. Income2- income level: what is your annual household income? (1 = less than $10,000, 2 =. Less than 15,000, 3 = less than $20,00, 4= less than $25,000, 5 = less than $35,000, 6 = less than $50,000, 7 = less than $75,000, 8 = $75,000 or more)

O. Flushot6- adult flu shot: During the past 12 months, have you had either a flu shot or a flu vaccine that was sprayed in your nose? (1 = yes, 2 = no, 7 = not sure, 9 = refused)

p. Howlong: mammogram: how long has it been since your last mammogram? ( 1 = less than 12 months, 2 = within past 2 years, 3 = within past 3 years, 4 = within the past 5 years, 5 = 5 or more years ago, 7 = not sure, 9 = refused)

Q. lastpap2: How long has it been since your last Pap test? (1 = within 12 months, 2 = within the past 2 years, 3 = within the past 3 years, 4 = within the past 5 years, 5 = 5 or more years ago, 7 = not sure, 9 = refused)

r. lastsig3: sigmoidoscopy/colonoscopy: How long has it been since your last sigmoidoscopy to colonoscopy? ( 1 = less than 12 months, 2 = within past 2 years, 3 = within past 3 years, 4 = within the past 5 years, 5 = within past 10 years, 6 = 10 or more years ago, 7 = not sure, 9 = refused)

s. hadsigm3: sigmoidoscopy/colonoscopy: Have you ever had a sigmoidoscopy or colonoscopy? (1 = yes, 2 = no, 7 = not sure, 9 = refused)

t. xhchvu651- health care coverage (ages 18-64): Do you have any form of health care coverage? (1 = yes, 2 = no, 9 = not sure, refused, or missing) 

U. xtotinda- leisure time physical activity: Adults who reported doing physical activity or exercise during the past 30 days other than their regular job (1 = yes, 2 = no, 9 = not sure, refused, missing)

v. Year- a column we created that indicates the year the participant answered the phone survey (integer between 2014 and 2018)

w. drvisits- How many times have you been to a doctor, nurse, or other health professional in the past 12 months? (Integer 1- 76, 88 = None, 77 = not sure)

x. medicare- Do you have Medicare? (1 = yes, 2 = no, 7 = not sure, 9 = refused)

y. hlthcvr1- Primary Health Care Coverage: What is the primary source of your health care coverage? (1 = plan through employer, 2 = a plan bought by you or another family member, 3 = medicare, 4 = medicaid or other state program, 5 = tricare, VA, or Military, 6 = Alaska Native, Indian Health Service. Tribal Health Services, 7 = some other source, 8 = no coverage, 77 = not sure, 99 = refused)

Z. nocov121: In the PAST 12 MONTHS was there any time when you did NOT have ANY health insurance or coverage? ( 1 = yes, 2 = no, 7 = not sure, 9 = refused)

aa. medscos1- Not including over-the-counter (OTC) medications, was there a time in the past 12 months when you did not take your medication as prescribed because of cost?( 1 = yes, 2 = no, 3 = no medication was prescribed, 7 = not sure, 9 = refused)

bb. carercvd- n general, how satisfied are you with the health care you received? (1 = very satisfied, 2 = somewhat satisfied, 3 = not at all satisfied, 7 = not sure, 8 = not applicable, 9 refused)
