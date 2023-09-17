class Cookie:
    # Create a class that is used to create cookie objects

    def __init__(self, color):
        self.color = color

    # get the color of the cookie
    def get_color(self):
        return self.color

    # set the color of the cookie
    def set_color(self, color):
        self.color = color


# cookie objects
cookie_one = Cookie('green')
cookie_two = Cookie('blue')

# print cookie.get_color()
print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

# set the color of the cookie_one
cookie_one.set_color('yellow')

# print cookie.get_color
print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())
