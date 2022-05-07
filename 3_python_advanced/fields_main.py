from fields import Example

print(Example.example_field)
object1 = Example()

print(object1.example_field)
object1.example_field = 15

print("New values:")
print(Example.example_field)
print(object1.example_field)

object1.set_example_field(-50)
print(object1.get_example_field())