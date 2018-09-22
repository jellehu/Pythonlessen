def lang_genoeg(lengte):
    if lengte >= 120:
        return 'Je bent lang genoeg voor de attractie!'
    else:
        return 'Sorry, je bent te klein!'

print('1. ' + lang_genoeg(130))
print('2. ' + lang_genoeg(110))