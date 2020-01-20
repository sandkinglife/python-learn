
student = {
"id":"1",
"First_name":"Vinay",
"Last_name":"kp"
}
try:
    name=student["First_name"]+student["Last_"]
    print("Name is {0}".format(name))
except Exception as e:
    print("Suppose to be Last_name")
    print("Exception {0}".format(e))
