import os
def func(path):
    if os.path.isfile(path) and path.endswith('.py'):
        os.system('python %s' % path)
    elif os.path.isdir(path):
        for name in os.listdir(path):
            abs_path = os.path.join(path,name)
            print(abs_path)
            if abs_path.endswith('.py'):
                os.system('python %s' % abs_path)
func(r'求职之路')