#2017/12/29
#author:Tan
#今日学习'类'的日记

class f1:
    def __init__(self):   #构造方法将在对象化的同时进行执行  #不能被子类调用
        self.name=1
        self.age=2
        print(self.name)
    def opp(self):       #函数参数中有SELF 允许函数访问实例化对象中的属性
        print('opp')
        print(self.name)

class s2(f1):
    def opp(self):
        print('lpp')

class s1(f1):
    def opp(self):      #重写父类中的函数，不执行父类中的
        print('app')
        super(s1,self).opp() #执行父类中的方法之一
        f1.opp(self)       #执行父类中的方法之一

class ss(s1,s2):           #继承多类时，调用同名函数，从左到右，从外到里。
    def pp(self):
        print('pp')

if __name__=='__main__': #作为测试的逻辑步骤，只在模块文件内调用的时候才执行。
   F=f1()  #结果会赋予F.NAME,F.AGE并打印F.NAME
   F.opp() #结果会打印OPP和SELF.NAME
   S=s1()
   S.opp()
   SS=ss()
   SS.opp()  #将会调用S1中的OPP函数 如果S1中没有OPP函数将会执行S2中的OPP，如果S2中再没有才会执行F1的OPP函数