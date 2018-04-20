import sys
import os
def gen_project(name,target_dir='.'):
    dir = '%s/%s' % (target_dir,name)
    os.system('mkdir %s' % dir)

    os.system('cp .gitignore %s' % dir)
    os.system('cp gradlew %s' % dir)
    os.system('cp gradlew.bat %s' % dir)
    os.system('cp build.gradle %s' % dir)
    # os.system('cp settings.gradle %s' % dir)
    os.system('cp -r src %s' % dir)
    os.system('cp -r gradle %s' % dir)
    os.system('echo "rootProject.name = \'%s\'" >> %s/%s/settings.gradle' % (name,target_dir,name))

if __name__ == '__main__':
    arg_len = len(sys.argv)
    if (arg_len == 1):
        print("please input project name")
    else:
        pro_name = sys.argv[1]
        if arg_len == 2:
            gen_project(pro_name)
        else:
            gen_project(pro_name,sys.argv[2])
