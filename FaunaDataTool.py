import sqlite3

conn = sqlite3.connect('SpecimenData.db')
c = conn.cursor()
cursor = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS catalog (
       number integer NOT NULL PRIMARY KEY autoincrement,
       type text NOT NULL,
       taxon text,
       species text NOT NULL,
       part text NOT NULL,
       age integer,
       layer text,
       notes text
       )""")

while True:
    print('Please enter individual specimen data: ')
    print("Type 'Exit' at anytime to save and quit.")
    input_prompts = [
        'Catalog #: ',
        'Type of Specimen: ',
        'Taxon: ',
        'Species: ',
        'Body Part: ',
        'Estimated Age: ',
        'Strata: ',
        'Notes: '
    ]
    responses = []
    response = ''
    for prompt in input_prompts:  # loop over our prompts
        response = input(prompt)

        if response == 'exit' or 'Exit':
            break  # break out of for loop
        responses.append(response)

    if response == 'exit' or 'Exit':
        break  # break out of while loop

    # we do list destructuring below to get the different responses from the list
    c_number, c_type, c_taxon, c_species, c_part, c_age, c_layer, c_notes = responses

    cursor.execute("""
                INSERT OR IGNORE INTO catalog(number, type, taxon, species, part, age, layer, notes)
                VALUES (?,?,?,?,?,?,?,?)
                """,
                   (
                       c_number,
                       c_type,
                       c_taxon,
                       c_species,
                       c_part,
                       c_age,
                       c_layer,
                       c_notes,
                   ))
    conn.commit()
    responses.clear()  # clear our responses, before we start our new while loop iteration
    print('Specimen data entered successfully.')
    print('Your data is stored in the file titled SpecimenData.db')
conn.close()
