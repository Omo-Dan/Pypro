#AND operator, used where both/all conditions are true.
has_high_income=True
has_good_credit =False
if has_good_credit and has_high_income:
    print('Eligible for loan')

#OR used where atleast one of  condition is true

if has_good_credit or has_high_income:
    print('Eligible for loan')

#NOT-coverts boolean to true or false
#eg. if apllicant has good credit and doesnt have criminal record 

has_good_credit:True
has_criminal_record:False
if has_good_credit and not has_criminal_record:
    print( 'Applicant Eligble for loan')