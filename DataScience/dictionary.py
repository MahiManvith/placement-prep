#phone_number = {'Manvith' : 9100242203, 'Sudhanvi' : 8124234323, 'Laxmi' : 9676656722}
#print(phone_number)

#phone_number = dict([('Mahi', 9100), ('Sudhu', 8145), ('Laxmi', 9676)])
#print(phone_number)

#student_details = dict([('Lucky', 4), ('Sudhu', 9), ('Sandeep',7)])
#print(student_details)

trip_details = {'Mahi': 10000, 'Sandy': 12000, 'Shannu': 13000, 'Cheruku': 20000, 'Neeshanth': 30000}
trip_details['Sandy'] = 35000
trip_details['Mahi'] = {'Online':22500, 'Cash':22500}
trip_details['Shannu'] = 30000
trip_details['Cheruku'] = 25000
trip_details['Neeshanth'] =  22500
print(trip_details['Sandy'])
print(trip_details['Mahi']['Online'])
print(trip_details.get('Shannu'))
print(trip_details.get('Shivanad'))