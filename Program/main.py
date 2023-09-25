from AnalyserFrame import AnalyserApp
import wx


def main():
    app = wx.App()
    frame = AnalyserApp()
    frame.Show(True)
    app.MainLoop()


if __name__ == "__main__":
    main()