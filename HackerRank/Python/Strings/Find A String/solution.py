#https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    x = 0
    count = 0
    for x in range (len(string) - len(sub_string) + 1)
        temp = x
        y = 0
        while(x<len(string) and y<len(sub_string) and string[x] == sub_string[y]):
            x = x + 1
            y = y + 1
        if (y == len(sub_string)):
            count = count + 1
        x = temp
    return count
            

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    count = count_substring(string, sub_string)
    print count
