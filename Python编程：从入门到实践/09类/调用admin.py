import sys
sys.path.append('C:\\Users\刘子桓\PycharmProjects\practice\Python编程：从入门到实践\\09类')

from user import Admin

admin_3 = Admin('liu','zihuan',23,'wuhan')
admin_3.privileges.show_privileges()
