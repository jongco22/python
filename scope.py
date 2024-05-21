g_x = 'global' #global scope

def g_func():
    # Local Scope, g_func의 function namespace로 g_func 의 관점에선 local이라고 불림.
    l_x = 'local of g_func'

    # Non-local Scope, nested_func의 관점에서는 nonlocal 키워드가 적용되는 Non-local scope임 (global과는 구분이 된다.).
    non_local_x = 'non-local'

    print('global_variable : ',g_x)
    print('local_variables of g_func :', l_x, non_local_x)
    
    def nested_func():
        # nested_func 의 관점에선 local임.
        l_x = 'local of nested func' #g_func의 l_x와는 다른 scope이므로 동일한 name을 사용해도 namecollision이 없다.
        l_y = 'y : local of nested func'
        print('global_variable : ',g_x)
        print('nonlocal of nested_func :', non_local_x)
        print('local_variables of nested_func :', l_x)
 
    nested_func()  
    print(l_y) #nameerror발생.l_y는 이 곳에서는 정의가 되지 않음. scope이 다름.

g_func()
print(non_local_x)#nameerror발생. non_local_x는 이곳에서는 정의되지 않음. scope이 다름.
