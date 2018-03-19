import time
import rex_finder
import win32api
import win32con
import  random

def main():
    GA = []
    for i in range(0,12):
        GA.append([random.uniform(0,5),0,random.uniform(30,100)])

    #GA = [[1.0076871758146888, -0.4448246824543481, 74.70994291686364], [1.5989524803222888, -0.0013449443743635547, 72.76835547376734], [1.644528657638396, 0.004535354317682483, 73.48497501785039], [2.118996362057874, -0.0935634326550836, 75.10398848776747], [0.3392016231899708, -0.7725425093478439, 74.30987535287234], [1.296185933144637, -0.40816812505789213, 74.47974978746403], [0.5863167271647641, 0.643580513237205, 74.1869136002575], [0.5254716284131703, -0.24252765744133786, 73.78797457073503], [1.6032111523908386, -0.7259590314058956, 75.13941519621567], [0.6732967225150893, -0.11446902802618131, 73.57241807576155], [1.7266754972680545, -1.1924497915742063, 74.21472313534748], [1.2911012127784112, 0.7142745787547158, 74.83159770019002]]
    RES = []
    for i in range(0,12):
        RES.append([0,i])
    seed = 1
    turn = 0
    print("inited. Start.")
    while True:
        seed *= 0.9999
        for i in range(12):
            time_start = time.time()
            while True:
                win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
                if (rex_finder.get_over()):
                    break
                dis,direct = (rex_finder.get_dis())
                t = time.time()-time_start
                if ((GA[i][0]*dis+GA[i][1]*t)<=GA[i][2]):
                    win32api.keybd_event(38, 0, 0, 0)
            time_total = time.time()-time_start
            RES[i][0] = time_total
            win32api.keybd_event(13, 0, 0, 0)
            win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
        RES.sort(key= lambda x:x[0],reverse=True)
        f = GA[RES[0][1]]
        m = GA[RES[1][1]]
        for i in range(12):
            GA.pop()
        GA.append(f)
        GA.append(m)
        avg_0 = (GA[0][0] + GA[1][0]) / 2
        avg_1 = (GA[0][1] + GA[1][1]) / 2
        avg_2 = (GA[0][2] + GA[1][2]) / 2
        for i in range(10):
            GA.append([avg_0+random.uniform(-seed, seed),avg_1+random.uniform(-seed, seed),avg_2+2*random.uniform(-seed, seed)])
        print(RES)
        print(GA)
        print("Finish:",turn)
        turn +=1




if __name__ == '__main__':
    main()