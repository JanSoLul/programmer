def is_complete_parenthesis(p):
    stack = []
    for i in range(len(p)):
        if p[i] == '(':
            stack.append(p[i])
        else:
            if stack:
                stack.pop()
            else:
                return False
    return True

def is_balanced_parenthesis(p):
    left, right = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
    return left == right

def conversion(p):
    if is_complete_parenthesis(p):
        return p
    else:
        for i in range(1, len(p)//2+1):
            new_parenthesis = ''
            u = p[:i*2]
            if is_balanced_parenthesis(u):
                v = p[i*2:]
                v = conversion(v)
                if is_complete_parenthesis(u):
                    new_parenthesis += u + v
                else:
                    new_parenthesis += '(' + v + ')'
                    new_u = ''
                    for i in range(1, len(u)-1):
                        if u[i] == ')':
                            new_u += '('
                        else:
                            new_u += ')'
                    new_parenthesis += new_u
            if new_parenthesis != '':
                return new_parenthesis

def solution(p):
    answer = conversion(p)
    return answer

if __name__ == '__main__':
    p_l = ["(()())()", ")(", "()))((()"]
    for i in range(len(p_l)):
        print(solution(p_l[i]))
