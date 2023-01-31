# variable for small
small = True
# variable for green
green = False

# if object is small and green, print 'pea'
if small and green:
    print("pea")
# if object is small but not green, print 'cherry'
elif small and not green:
    print("cherry")
# if object is not small but is green, print 'watermelon'
elif not small and green:
    print("watermelon")
# if object is not small or green, print 'pumpkin'
elif not small and not green:
    print("pumpkin")
