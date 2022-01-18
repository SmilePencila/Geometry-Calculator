import os
import sys
import math



#Here is the definition of the dictionary
shape_dictionary = {'pentagon': [0.7265, 5], 'hexagon': [0.5774, 6], 'heptagon': [0.4877, 7], 'octogon': [0.4245, 8],
                    'nonagon': [0.3640, 9], 'decagon': [0.3249, 10]}
shapeinput_dictionary = {'circle': [1, 'radius'], 'rectangle': [2, 'length', 'width'], 'triangle': [3, 'side1', 'side2', 'side3'],
'right triangle': [2, 'base', 'height'], 'square': [1, 'side'], 'trapezoid': [3, 'side1', 'side2', 'height'], 'polygon': [1, 'side1'], 
'cube': [1, 'side'], 'sphere': [1, 'radius'], 'cuboid': [3, 'length', 'breadth', 'height'], 'cylinder': [2, 'radius', 'height'], 
'cone': [3, 'radius', 'height', 'slant_heights']}




#Here is the definition of functions
def getShapeinput(shape):
    arg = []
    if shape in shapeinput_dictionary.keys():
        print('>>>' +  str(shapeinput_dictionary[shape]))
        num_of_arg = shapeinput_dictionary[shape][0]
        for i in range(num_of_arg):
            num = input('Type Input ' + shapeinput_dictionary[shape][i + 1] + ' please:')
            tmp = num.replace('.', '')
            if tmp.isnumeric():
                arg.append(float(num))
            else:
                print('The input should be either a number or floating point and greater than 0.')
                arg = []
                break
    return arg



#Here is the main program
print('\n')
print('********************************************************************')
print('*                         Geometry Calculator                      *')
print('*                        _____________________                     *')
print('*                               Begin                              *')
print('********************************************************************')
print('                          Pick a shape below                        ')
print('____________________________________________________________________')
print('   Circle, Rectangle, Triangle, Right Triangle, Square, Trapezoid   ')
print('       Pentagon, Hexagon, Heptagon, Octagon, Nonagon, Decagon       ')
print('                Cube, Sphere, Cuboid, Cylinder, Cone                ')
print('********************************************************************')
print('                      Type "exit" to exit program                   ')

print('\n')
while True:
    shape = input('Type the shape: ')
    if shape == 'circle':
        print('circle')
        ll = getShapeinput('circle')
        if len(ll) > 0:
            radius = ll[0]
            perimeter = 2 * radius * 3.14
            area = radius * radius * 3.14
            print('The perimeter is ' + str(perimeter))
            print('The area is ' + str(area))
    elif shape == 'rectangle':
        print('rectangle')
        ll = getShapeinput('rectangle')
    
        if len(ll) > 0:
            length = ll[0]
            width = ll[1]
            perimeter = 2 * length + 2 * width
            area = length * width
            print('The perimeter is ' + str(perimeter))
            print('The area is ' + str(area))
    elif shape == 'triangle':
        print('triangle')
        ll = getShapeinput('triangle')
        if len(ll) > 0:
            side1 = ll[0]
            side2 = ll[1]
            base = ll[2]
            if side1 + side2 > base and side1 + base > side2 and side2 + base > side1:
                perimeter = side1 + side2 + base
                print('The perimeter is ' + str(perimeter))
                s = perimeter/2
                tmp = s * (s - base) * (s - side1) * (s - side2)
                area = math.sqrt(int(tmp))
                print('The area is ' + str(area))
            else:
                print('That is not a triangle. Fix it.')
    elif shape == 'right triangle':
        print('right triangle')
        ll = getShapeinput('right riangle')
        if len(ll) > 0:
            base = ll[0]
            height = ll[1]
            area = base * height / 2 
            side = math.sqrt(base * base + height * height)
            print('The area is ' + str(area))
            print('The perimeter is ' + str(side + base + height))
    elif shape == 'square':
        print('square')
        ll = getShapeinput('square')
        if len(ll) > 0:
            side = ll[0]
            perimeter = side * 4
            area = side * side
            print('The perimeter is ' + str(perimeter))
            print('The area is ' + str(area))
    elif shape == 'trapezoid':
        print('trapezoid')
        ll = getShapeinput('trapezoid')
        if len(ll) > 0:
            side1 = ll[0]
            side2 = ll[1]
            height = ll[2]
            area = (side1 + side2) / 2 * height
            print('The area is ' + str(area))
    #elif shape == 'pentagon' or shape == 'hexagon' or shape == 'heptagon' or shape == 'octogon' or shape == 'nonagon' or shape == 'decagon':
    elif shape in shape_dictionary.keys():
        ll = getShapeinput('polygon')
        if len(ll) > 0:
            side1 = ll[0]
            coff = shape_dictionary[shape][0]
            at = ((side1 / 2) / coff) * (side1 / 2)
            area = at * shape_dictionary[shape][1]
            print('The area is ' + str(area))
    elif shape == 'cube':
        ll = getShapeinput('cube')
        if len(ll) > 0:
            side=ll[0]
            area = 6*side*side
            volume = side*side*side
            print('The area is ' + str(area))
            print('The volume is ' + str(volume))
    elif shape == 'sphere': 
        ll = getShapeinput('sphere')
        if len(ll) > 0:
            radius=ll[0]
            area = 4*3.14*radius*radius
            volume = 4/3*3.14*radius*radius*radius
            print('The area is ' + str(area))
            print('The volume is ' + str(volume))
    elif shape == 'cuboid':
        ll = getShapeinput('cuboid')
        if len(ll) > 0:
            length = ll[0]
            breadth = ll[1]
            height = ll[2]
            area = 2*(length * breadth + breadth * height + length * height)
            volume = length*breadth*height
            print('The area is ' + str(area))
            print('The volume is ' + str(volume))
    elif shape == 'cylinder':
        ll = getShapeinput('cylinder')
        if len(ll) > 0:
            radius = ll[0]
            height = ll[1]
            area = 2*3.14*radius*(radius + height) 
            volume = 3.14*radius*radius*height
            print('The area is ' + str(area))
            print('The volume is ' + str(volume)) 
    elif shape == 'cone':
        ll = getShapeinput('cone')
        if len(ll) > 0:
            radius = ll[0]
            height = ll[1]
            slant_height = ll[2]
            area = 3.14*radius*(slant_height + radius)
            volume = 1/3*3.14*radius*radius*height
            print('The area is ' + str(area))
            print('The volume is ' + str(volume)) 

    elif shape == 'exit' or shape == 'Exit' or shape == 'EXIT':
        break
    else:
        print('Not a real shape')
    


