import pyautogui as pag
import sys
import time
import pandas as pd

#while True:
#    print(pag.position())

if __name__ == "__main__":

    a = pd.read_csv('/Users/yn02/Downloads/AFStudy_VUNO_downsampling_combined_withcnt.csv')
    b = a[a.loc[:, 'cnt'] == 1]
    c = a[a.loc[:, 'cnt'] > 1]

    pag.FAILSAFE = True
    pag.PAUSE = 0.5
    time.sleep(5)

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
