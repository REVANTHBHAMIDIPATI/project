from models.AuthModel import AuthModel

class AuthController:

    def login(self,username,password):

        if len(username) == 0:
            message = "Username cannot be empty"
            return message

        if len(password) == 0:
            message = "password cannot be empty"
            return message

        am = AuthModel()
        result = am.getUser(username,password)
    # def detection(self):
    #     dv = detect_drowsiness()
    #       dv.load()
        if result:
            message = 1
            # message = f'Hello {result[1]}'
            return message
            
        else:
            message = 'User not found'
            return message

    def register(self,name,phone,email,username,password):

        if len(name) == 0:
            message = "Name cannot be empty"
            return message

        am = AuthModel()
        # result = am.createUser(name,phone,email,username,password)

        if result == 1:
            message = 'User is successfully registered. You can login now'
        else:
            message = 'Some database error. Kindly retry'

        return message