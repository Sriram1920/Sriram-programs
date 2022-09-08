

direct=input("Enter the Direction: ").lower()
angle=int(input("Enter the Angle: "))
rot=input("Enter the Rotation Type[CCW/CW]: ").lower()

if direct=='south':
    if rot=='cw':
        if angle>=0 and angle<=90:
            print("SouthWest")
        elif angle>90 and angle<=180:
            print("Northwest")
        elif angle>180 and angle<=270:
            print("NorthEast")
        elif angle>270 and angle<=360:
            print("SouthEast")
        else:
            print("invali Input")
    elif rot=='ccw':
        if angle>=0 and angle<=90:
            print("SouthEast")
        elif angle>90 and angle<=180:
            print("NorthEast")
        elif angle>180 and angle<=270:
            print("NorthWest")
        elif angle>270 and angle<=360:
            print("SouthWest")
        else:
            print("invali Input")        

elif direct=='north':
    if rot=='cw':
        if angle>=0 and angle<=90:
            print("NorthEast")
        elif angle>90 and angle<=180:
            print("SouthEast")
        elif angle>180 and angle<=270:
            print("SouthWest")
        elif angle>270 and angle<=360:
            print("NorthWest")
        else:
            print("invali Input")
    elif rot=='ccw':
        if angle>=0 and angle<=90:
            print("NorthWest")
        elif angle>90 and angle<=180:
            print("SouthWest")
        elif angle>180 and angle<=270:
            print("SouthEast")
        elif angle>270 and angle<=360:
            print("NorthEast")
        else:
            print("invali Input")

elif direct=='west':
    if rot=='cw':
        if angle>=0 and angle<=90:
            print("NorthWest")
        elif angle>90 and angle<=180:
            print("NorthEast")
        elif angle>180 and angle<=270:
            print("SouthEast")
        elif angle>270 and angle<=360:
            print("SouthWest")
        else:
            print("invali Input")
    elif rot=='ccw':
        if angle>=0 and angle<=90:
            print("SouthWest")
        elif angle>90 and angle<=180:
            print("SouthEast")
        elif angle>180 and angle<=270:
            print("NorthEast")
        elif angle>270 and angle<=360:
            print("NorthWest")
        else:
            print("invali Input")        

elif direct=='east':
    if rot=='cw':
        if angle>=0 and angle<=90:
            print("SouthEast")
        elif angle>90 and angle<=180:
            print("SouthWest")
        elif angle>180 and angle<=270:
            print("NorthWest")
        elif angle>270 and angle<=360:
            print("NorthEast")
        else:
            print("invali Input")
    elif rot=='ccw':
        if angle>=0 and angle<=90:
            print("NorthEast")
        elif angle>90 and angle<=180:
            print("NorthWest")
        elif angle>180 and angle<=270:
            print("SouthWest")
        elif angle>270 and angle<=360:
            print("SouthEast")
        else:
            print("invali Input")
else:
    print("Invalid Input")
