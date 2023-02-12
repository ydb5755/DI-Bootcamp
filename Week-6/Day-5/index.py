sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
print(sample_dict['class']['student']['marks']['history'])

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
del sample_dict['name']
del sample_dict['salary']
print(sample_dict)
# keys_to_remove = ["name", "salary"]