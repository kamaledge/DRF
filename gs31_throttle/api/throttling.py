from rest_framework.throttling import UserRateThrottle

# Throttle for scope of Jack, Jack defined in settings, and useed in views file, replacing User
# Jack is just a random name much like a vairable

class JackRateThrottle(UserRateThrottle):
    scope = 'Jack'

# Apart from code here, we also added Jack in Setting file's throttle rate to get out work done