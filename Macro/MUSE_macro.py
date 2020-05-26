import pyautogui as pag
import sys
import time
import pandas as pd

#while True:
#    print(pag.position())

pag.FAILSAFE = True
pag.PAUSE = 2
time.sleep(5)

if __name__ == "__main__":
    constant = 0
    a = pd.read_csv('/home/tj/PycharmProjects/MUSE_macro/data/AFStudy_VUNO_downsampling_combined_withcnt.csv')

    if constant == 0:
        b = a[a.loc[:, 'cnt'] == 1]
        try:
            for i in b.index:
                pid = b.loc[i, 'person_id']
                day = b.loc[i, 'day']
                month = b.loc[i, 'month']
                year = b.loc[i, 'year']

                pag.click(143, 659)
                pag.typewrite(str(pid))
                pag.click(106, 736)
                pag.typewrite(str(day))
                pag.press('right')
                pag.typewrite(str(month))
                pag.press('right')
                pag.typewrite(str(year))
                pag.click(55, 795)
                pag.click(314, 653)
                pag.click(315, 92)
                pag.click(893, 645)
        except pag.FailSafeException or KeyboardInterrupt:
            print("Exit program")
            sys.exit()

    elif constant == 1:
        c = a[a.loc[:, 'cnt'] > 1]
        try:
            for i in c.index:
                pid = c.loc[i, 'person_id']
                day = c.loc[i, 'day']
                month = c.loc[i, 'month']
                year = c.loc[i, 'year']

                pag.click(143, 659)
                pag.typewrite(str(pid))

                pag.click(106, 736)
                pag.typewrite(str(day))
                pag.press('right')
                pag.typewrite(str(month))
                pag.press('right')
                pag.typewrite(str(year))

                pag.click(55, 795)

                pag.click(314, 653)
                pag.keyDown('shift')
                pag.keyDown('down')
                time.sleep(3)
                pag.keyUp('down')
                pag.keyUp('shift')

                pag.click(315, 92)
                pag.click(893, 645)
        except pag.FailSafeException or KeyboardInterrupt:
            print("Exit program")
            sys.exit()
