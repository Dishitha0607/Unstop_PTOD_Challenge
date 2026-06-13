def userLogic(bob, alice):
    def process(s):
        stack = []

        for ch in s:
            if ch == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
    return process(bob) == process(alice)

if __name__ == "__main__":
    bob = input()
    alice = input()
    result = userLogic(bob, alice)
    print("YES" if result else "NO")