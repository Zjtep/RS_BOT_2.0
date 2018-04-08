import win32gui

class RunescapeWindow():
    """ Finds Runeloader Game Window"""
    def __init__(self):
        self.game_coord = 0
        self.setCoordinates()

    def setCoordinates(self):
        win32gui.EnumWindows(self._enumHandler, None)

        #offset the runeloader task bar
        off_set=[4,50,-4,-4]
        self.game_coord[0] += off_set[0]
        self.game_coord[1] += off_set[1]
        self.game_coord[2] += off_set[2]
        self.game_coord[3] += off_set[3]

    def _enumHandler(self,hwnd, lParam):
        if win32gui.IsWindowVisible(hwnd):
            if 'RuneLoader' in win32gui.GetWindowText(hwnd):
                # win32gui.MoveWindow(hwnd, 0, 0, 760, 500, True)
                rect = win32gui.GetWindowRect(hwnd)
                x = rect[0]
                y = rect[1]
                w = rect[2]
                h = rect[3]
                # w = rect[2] - x
                # h = rect[3] - y
                # print "\tLocation: (%d, %d)" % (x, y)
                # print "\t    Size: (%d, %d)" % (w, h)
                self.game_coord = [x, y, w, h]

    def getCoordinates(self):
        return self.game_coord