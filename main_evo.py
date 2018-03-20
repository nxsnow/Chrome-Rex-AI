import time
import rex_finder
import win32api
import win32con
import  random

def main():
    GA = []
    for i in range(0,12):
        GA.append([random.uniform(0,5),0,random.uniform(30,100)])

    #GA = [[0.9051558349846207, -2.6589938361217076, 52.37312013349952], [1.9710084982161624, -2.626491221686305, 53.93351058580019], [0.5018264961594234, -2.925780807440422, 51.57174681038255], [1.6152855126045509, -2.8668250912978177, 52.43783172499788], [1.7251924694674587, -2.6693387526320844, 53.722308880963915], [1.9373517910678455, -3.604531258454716, 51.538952927792565], [0.6417958328586509, -3.0276117529042854, 52.20959232692945], [2.170452824433818, -1.9811136833564373, 54.24180299996323], [1.9787112198378494, -3.339947229348282, 51.471306554219275], [1.9286564777625916, -3.3377673077732, 52.69507530486896], [1.071852273288901, -2.818208829341147, 53.022714298039965], [2.241193838729653, -2.776178359629721, 54.78274655315092]]
    RES = []
    for i in range(0,12):
        RES.append([0,i])
    seed = 1.05
    turn = 0
    print("inited. Start.")
    while True:
        seed *= 0.9999
        if (seed < 0.01 and random.uniform(0,1000)<=0.5):
            seed = seed*5 + 0.01
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