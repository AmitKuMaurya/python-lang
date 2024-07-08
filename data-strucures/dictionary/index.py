# dictionary are key value type of data type.
# does not support indexing.
# dictionary.


dictionary = {
    "age" : 1,
    "name" : ""
};

# dictionary has key value pair of data storage.
# doesn't support indexing.
# data can be accessed using key.


# create empty dicionary.
d = {}
print(type(d),d);

di = dict();
print(type(di),di);

# zip
name = ["Amit","Charu","Ragini","Aditya"];
prices = [10,20,30,40];

make_zip = dict(zip(name,prices));
print(make_zip);

# accessing keys or values of make_zip;

# 1  make_zip["value"]       2. make_zip.get("value").

# they both are accessable of key only.
print(make_zip["Charu"]);

# this won't gives error,if unable to find something. just return none fo default return you below commented syntax.
print(make_zip.get("Ragini","Not Available")); # if value if not be present then only second argumnet value will be printed
print(make_zip.get("Ramanujan","Not Available"));
print(make_zip.get("Aditya"));

# update a dictionary.

# updating existing value.
update = make_zip['Charu'] = { "student_1" : 1, "student_2" : 2 };
# print(update);
print(make_zip);

# add a new value in dictionary.
update1 = make_zip["Gudiya"] = 80;
print(make_zip);

# to update a dictionary with multiple key and values.
newValues = { "Student_3" :  3, "Student_4" : 4 , "Student_5" : 5};
make_zip.update(newValues);
print(make_zip);


# citizenship check.
citizenship = "Student_2" in make_zip;
print(citizenship);

# deleteing data from dictionary.

# pop : this, method removes the key and return its value;

pop_dict = make_zip.pop("Aditya"); # 1 arument is required, else throw error.
print(pop_dict);

# popItem() : this remove the item of dict from last.
# if empty, throws error.

# make_zip.popitem();
print(make_zip);

# you could delete the whole dict.

# del make_zip;
# print(make_zip);

#  iterate in dict

# for in

# for person in make_zip :
#     print(person,make_zip[person]);

# dict.tiem()

for key, value in make_zip.items():
    print(key, value);

# more methods in dictonary.

# keys() :
# values() :
# items() :



