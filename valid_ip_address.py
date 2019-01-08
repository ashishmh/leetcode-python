import sys

# https://leetcode.com/problems/validate-ip-address/

def validIPAddress(IP):
    if len(IP) < 7 or len(IP) > 39:
        return 'Neither'
    
    isIPv4 = False
    isIPv6 = False
    if '.' in IP:
        IPv4Parts = IP.split('.')
        isIPv4 = isValidIPv4(IPv4Parts)
        # print('ipv4 parts: ', IPv4Parts)
        # print('validating ipv4: ', isIPv4)
    elif ':' in IP:
        IPv6Parts = IP.split(':')
        isIPv6 = isValidIPv6(IPv6Parts)
        # print('ipv6 parts: ', IPv6Parts)
        # print('validating ipv6: ', isIPv6)
    else:
        return 'Neither'

    if isIPv4:
        return 'IPv4'
    elif isIPv6:
        return 'IPv6'
    else:
        return 'Neither'


def isValidIPv4(IPv4Parts):
    if len(IPv4Parts) != 4:
        return False

    for part in IPv4Parts:
        try:
            if '-' in part or '+' in part:
                return False
            if part[0] == '0' and len(part) != 1:
                return False
            part = int(part)
            if part < 0 or part > 255:
                return False
        except:
            return False
    return True


def isValidIPv6(IPv6Parts):
    if len(IPv6Parts) != 8:
        return False

    for part in IPv6Parts:
        if len(part) < 1 or len(part) > 4:
            return False
        for char in part:
            if char.isalnum() == False:
                return False
            if char.isalpha():
                if char.lower() not in ['a', 'b' ,'c', 'd', 'e', 'f']:
                    return False
    return True


def main():
	str = input('input: ')
	output = validIPAddress(str)
	print('output: ', output)


if __name__ == '__main__':
    main()