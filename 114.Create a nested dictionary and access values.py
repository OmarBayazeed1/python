#Create a nested dictionary and access values
students={
    'omar':{
        'age':23,
        'subjects':{
            'math':90,
            'arabic':34,
            'english':99
        }
    },
    'ali':{
        'age':21,
        'subjects':{
            'math':60,
            'arabic':88,
            'english':75
        }
    }
}
print('omar grade in english is:',students['omar']['subjects']['english'])
print('ali age is:',students['ali']['age'])

