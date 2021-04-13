class IAM:    # Idenity Access Management
    def __init__(self):
        self.master_data = {}
        self.roles = {}
    
    def add_role_to_user(self,user_name, role_name):
        self.master_data.setdefault(user_name,[])
        self.master_data[user_name].append(role_name)

    def remove_role_from_user(self,user_name, role_name):
        if role_name in self.master_data[user_name]:
            self.master_data[user_name].remove(role_name)
        else:
            print("This role doesn't exist for this user")
    
    def add_permissions_to_roles(self,role_name,permissions):
        self.roles.setdefault(role_name,[])
        self.roles[role_name].append(permissions)


    def isAllowed(self,user_name,action):
        role = self.master_data[user_name]
        action = action.lower()
        # print(role)
        if role[0] in self.roles.keys():
            if action in self.roles[role[0]]:
                # print('It is allowed to perform the action')
                return True
            else:
                print('{user} is not allowed to perform {act}'.format(user=user_name,act=action))
                return False
    
    def getRoles(self,user_name):
        return self.master_data[user_name]
    
    def getPermissionForRole(self,role_name):
        return self.roles[role_name]


    def readFile(self):
        f = open('test.txt', 'r')
        print('---Begin----')
        print(f.read())
        print('---End of----')
        f.close()

    def appendToFile(self,text):
            f = open('test.txt','a')
            f.write('\n'+ text)
            print('file has been appended')
            f.close()

    def overWriteToFile(self,text):
            f = open('test.txt','w')
            f.write(text)
            print('file has been overwriteen')
            f.close()
    
    def isValidRole(self,role_name):
        return role_name in self.roles.keys()

    

iam = IAM()

iam.add_role_to_user('Admin','FullAdminAccess')
# print(iam.getRoles('Admin'))
iam.add_permissions_to_roles('FullAdminAccess','read')
iam.add_permissions_to_roles('FullAdminAccess','write')
iam.add_permissions_to_roles('FullAdminAccess','append')
iam.add_permissions_to_roles('FullAdminAccess','delete')

iam.add_role_to_user('User1','ReadOnlyAccess')
iam.add_permissions_to_roles('ReadOnlyAccess','read')




while(1==1):
    print('Here are the list of users,select one:',list(iam.master_data.keys()))

    u = input()
    if u not in iam.master_data.keys():
        print('{user} does not exist.'.format(user=u))
    elif u=='Admin':
        while(1==1):
            print('You are logged in as Admin')
            print('Press 1 to login as another user')
            print('Press 2 to perform various actions like read,write etc')
            print('Press 3 to create user')
            print('Press 4 to create a new role')
            print('Press 0 to go back')

            n = int(input())

            if n==1:
                
                print('Here are the list of users:',list(iam.master_data.keys())[1:])
                u = input()
                while(1==1):
                    print('You are logged in as {user_name}'.format(user_name=u))
                    print('Press 1 to see the roles attached with this user')
                    print('Press 2 to access resource')
                    print('Press 0 to go back')
                    n = int(input())
                    if n==1:
                        print('Here are the roles attached with this user : ' , iam.getRoles(u))
                    elif n==2:
                        act = input('Choose one action: read,write or append:\n')
                        if(iam.isAllowed(u,act)):
                            if act.lower()=='read':
                                iam.readFile()
                            elif act.lower()=='write':
                                txt = input('Input text to overwrite your file\n')
                                iam.overWriteToFile(txt)
                            elif act.lower()=='append':
                                txt = input('Enter text to append to your file\n')
                                iam.appendToFile(txt)
                    elif n==0:
                        break
            elif n==2:
                    act = input('Choose one action: read,write or append:\n')
                    if(iam.isAllowed(u,act)):
                        if act.lower()=='read':
                            iam.readFile()
                        elif act.lower()=='write':
                            txt = input('Input text to overwrite your file:\n')
                            iam.overWriteToFile(txt)
                        elif act.lower()=='append':
                            txt = input('Enter text to append to your file\n')
                            iam.appendToFile(txt)
            
            elif n==3:
                user_name = input('Enter user name: ')
                print('Enter role from one of the following :', iam.roles)
                
                role = input()
                while not iam.isValidRole(role):
                    print('Enter a valid role from the list',iam.roles)
                    role = input()


                iam.add_role_to_user(user_name,role)
                print('{user_name} is added'.format(user_name = user_name))
                # print(iam.isValidRole(role))
                # role = input()
            elif n==4:
                role_name = input('Enter role name:')
                permissions = list(map(str, input("Enter permissions with space in between from the following : read,write,append\n").split()))
                for p in permissions:
                    iam.add_permissions_to_roles(role_name,p)
                

                print('{role_name} is been added'.format(role_name=role_name))
                print('Current list of roles : ', iam.roles)

            
            elif n==0:
                break
            
    else:
        while(1==1):
            print('You are logged in as {user_name}'.format(user_name=u))
            print('Press 1 to see the roles attached with this user')
            print('Press 2 to access resource')
            print('Press 0 to go back')
            n = int(input())
            if n==1:
                print('Here are the roles attached with this user : ' , iam.getRoles(u))
            elif n==2:
                act = input('Choose one actions: read,write or append:\n')
                if(iam.isAllowed(u,act)):
                    if act.lower()=='read':
                        iam.readFile()
                    elif act.lower()=='write':
                        txt = input('Input text to overwrite your file\n')
                        iam.overWriteToFile(txt)
                    elif act.lower()=='append':
                        txt = input('Enter text to append to your file\n')
                        iam.appendToFile(txt)
            elif n==0:
                break



# add_role_to_user('User1','FullAdminAccess')
# print(master_data)
# remove_role_from_user('User1','ReadOnlyAccess')
# print(master_data)

