"""

str.format_map(
  map : dict
)

- Format a string by returning a dictionary key's value

Parameters :
  map : dict = the input dictionary

"""

sample_dict : dict = {
  "name" : "demo",
  "age" : 18,
  "language" : "Python",
  "likes" : "nothing"
}

string : str = "Hi ! I'm {name}, {age} years old ! I like {likes} and I code in {language}"
print(string.format_map(sample_dict))