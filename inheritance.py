class parent():
	def __init__(self, last_name , eye_color):
		print("parent constructor called")
		self.last_name = last_name
		self.eye_color = eye_color

	def show_info(self):
		print("last name"+self.last_name)
		print("eye color"+self.eye_color)

class child(parent):
	def __init__(self,last_name, eye_color ,number_of_toys):
		print("child constructor called")
		parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys	

	def show_info(self, last_name, eye_color , number_of_toys):
		print("last name"+self.last_name)
		print("eye color"+self.eye_color)
		print("number of toys"+self.number_of_toys)
billy_cyrus = parent("cyrus" , "blue")
billy_cyrus.show_info()
milley_cyrus = child("cyrus", "blue", 5)
print(billy_cyrus.last_name)
