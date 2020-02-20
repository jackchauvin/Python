from Vector import Vector        
            
#Test for __init__            
vec=Vector(1.356,2.434)

#Test for __str__
print("vec:",vec)

#Test for __repr__
print('vec.__repr__():',vec.__repr__())

vec2=Vector(3.65576,1.4785)
#Test for __add__
vec3 = vec + vec2
print(vec,'+',vec2,'=',vec3)

#Tests for __sub__
vec3 = vec - vec2
print(vec,'-',vec2,'=',vec3)

#Test for __mul__
vec4 = vec * 3
print(vec,'* 3 =',vec4)

#Test for __rmul__
vec4 = 3 * vec
print('3 *',vec,'=',vec4)

#Tests for __eq__
print('vec==vec3:',vec==vec3)
print('vec==vec:',vec==vec)

#Test for magnitude
print('Magnitude of vec:', vec.magnitude())

#Test for unit
print('Unit vector of vec:', vec.unit())

#Test for unit vector of zero
zero=Vector()
print('Unit vector of <0,0>:',zero.unit())