from utils import makeDetection

def main():
    modelpaths = [ '.\\model\\svc-linear-8b953d.pkl']
    rawpaths = ['.\\test-linear\\raw']
    boxedpaths = ['.\\test-linear\\boxed']

    cnt = len(modelpaths)
    for i in range(cnt):
        m = modelpaths[i]
        r = rawpaths[i]
        b = boxedpaths[i]
        print(f'Using {m} for detection ......')
        makeDetection(m, r, b)
        print('')

if __name__ == '__main__':
    main()