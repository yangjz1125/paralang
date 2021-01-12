# loading tips
import os

def loadTipsPerLine(file):
  slist = file.read().split('\n')
  res = []
  for str in slist:
    res.append(str.replace('——', '\\n——'))
  return res

class loadingTips:
  'Loading tips file object'
  tipsList = []
  name = ''
  def __init__(self, name):
    self.name = name
    tipsList = []
  def loadFrom(self, src, func = loadTipsPerLine):
    with open(src, "rt") as f:
      self.tipsList.extend(func(f))
  def writeTips(self, lang, level = 0):
    with open(self.name, "wt") as f:
      sc = 'l_' + lang + ':\n'
      t = 1
      for s in self.tipsList:
        if s != '':
          sc = sc + ' LOADING_TIP_%d:%d: "%s"\n' % (t, level, s)
          t = t + 1
      f.write(sc,)

if __name__ == "__main__":
    lt = loadingTips("loading_tips_l_test.yml")
    lt.loadFrom("test.tip")
    lt.writeTips("english")