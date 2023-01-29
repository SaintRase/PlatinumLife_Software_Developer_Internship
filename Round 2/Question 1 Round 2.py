import pandas as pd #dependency
import numpy as np #dependency

df_teacher = pd.DataFrame({
    "name": ["Pep Guardiola", "Jurgen Klopp", "Mikel Arteta", "Zinadine Zidane"],
    "married": [True, True, False, True],
    "school": ["Manchester High School", "Liverpool High School", "Arsenal High", np.nan]
    })

df_student = pd.DataFrame({
"teacher": ["Mikel Arteta", "Mikel Arteta", "Pep Guardiola", "Jurgen Klopp", "Jurgen Klopp", "Jurgen Klopp", "Pep Guardiola","Pep Guardiola","Mikel Arteta"],
"name": ["Bukayo Saka", "Gabriel Martinelli", "Jack Grealish", "Roberto Firmino", "Andrew Robertson", "Darwin Nunez", "Ederson Moraes", "Manuel Akanji", "Thomas Partey"],
"age": [21, 21, 27, 31, 28, 23, 29, 27, 29],
"height": ['2.1m','2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m']
})

def create_list_of_dicts(df_teacher, df_student):
    list_of_dicts = []
    for i, row in df_teacher.iterrows():
        teacher_dict = {}
        teacher_dict['teacher'] = row['name']
        teacher_dict['school'] = row['school']
        teacher_dict['married'] = row['married']
        teacher_dict['students'] = []
        for j, row in df_student.iterrows():
            if row['teacher'] == teacher_dict['teacher']:
                student_dict = {}
                student_dict['student'] = row['name']
                student_dict['age'] = row['age']
                student_dict['height'] = row['height']
                #Loop through all columns in df_student and add them to the student_dict 
                for column in df_student.columns:
                    if column not in ["teacher", "name", "age", "height"]:
                        student_dict[column] = row[column]
                teacher_dict['students'].append(student_dict)
        list_of_dicts.append(teacher_dict)
    return list_of_dicts

print(create_list_of_dicts(df_teacher, df_student))