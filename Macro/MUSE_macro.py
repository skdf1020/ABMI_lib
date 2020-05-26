import pyautogui as pag
import sys
import time
import pandas as pd
import pathlib


def macro(b, path, constant = 0):
    for i in b.index:
        try:
            pid = b.loc[i, 'person_id']
            print(pid)
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
            if constant != 0:
                pag.keyDown('shift')
                pag.keyDown('down')
                time.sleep(3)
                print('poop')
                pag.keyUp('down')
                pag.keyUp('shift')

            pag.click(315, 92)
            pag.click(893, 645)
        except pag.FailSafeException or KeyboardInterrupt:
            print("Stopped. please restart.")
            c = base.iloc[base.index.tolist().index(i):, :]
            c.to_csv(path/'id.csv', mode='w')
            sys.exit()
    pathlib.Path(path/'id.csv').unlink()
    print("It's done")


# while True:
#    print(pag.position())

path = pathlib.Path('/home/tj/PycharmProjects/MUSE_macro/data')
pag.FAILSAFE = True
pag.PAUSE = 1
time.sleep(5)

if __name__ == "__main__":
    constant = 0
    id_path = pathlib.Path(path/'id.csv')
    if id_path.exists():base = pd.read_csv(id_path)
    else: base = pd.read_csv(path/'AFStudy_VUNO_downsampling_combined_withcnt.csv')

    if constant == 0: b = base[base.loc[:, 'cnt'] == 1]
    else: b = base[base.loc[:, 'cnt'] > 1]

    macro(b, path, constant)
