from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QTimer, QUrl
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
import image
import random
import os

class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.fhelp = 1
        self.fmusic = 1


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1222, 658)
        MainWindow.setMinimumSize(QtCore.QSize(1222, 658))
        MainWindow.setMaximumSize(QtCore.QSize(1222, 658))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/egg_leg_break_broken_chicken_icon_219659.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1222, 658))
        self.centralwidget.setMaximumSize(QtCore.QSize(1222, 658))
        self.centralwidget.setObjectName("centralwidget")
        self.VUL = QtWidgets.QLabel(self.centralwidget)
        self.VUL.setGeometry(QtCore.QRect(310, 260, 291, 271))
        self.VUL.setText("")
        self.VUL.setPixmap(QtGui.QPixmap(":/newPrefix/VUL.png"))
        self.VUL.setObjectName("VUL")
        self.VDL = QtWidgets.QLabel(self.centralwidget)
        self.VDL.setGeometry(QtCore.QRect(300, 300, 291, 271))
        self.VDL.setText("")
        self.VDL.setPixmap(QtGui.QPixmap(":/newPrefix/VDL.png"))
        self.VDL.setObjectName("VDL")
        self.VUR = QtWidgets.QLabel(self.centralwidget)
        self.VUR.setGeometry(QtCore.QRect(530, 260, 291, 271))
        self.VUR.setText("")
        self.VUR.setPixmap(QtGui.QPixmap(":/newPrefix/VUR.png"))
        self.VUR.setObjectName("VUR")
        self.VDR = QtWidgets.QLabel(self.centralwidget)
        self.VDR.setGeometry(QtCore.QRect(530, 300, 291, 271))
        self.VDR.setText("")
        self.VDR.setPixmap(QtGui.QPixmap(":/newPrefix/VDR.png"))
        self.VDR.setObjectName("VDR")
        self.ELU1 = QtWidgets.QLabel(self.centralwidget)
        self.ELU1.setGeometry(QtCore.QRect(310, 257, 41, 31))
        self.ELU1.setText("")
        self.ELU1.setPixmap(QtGui.QPixmap(":/newPrefix/EGG.png"))
        self.ELU1.setObjectName("ELU1")
        self.ELD1 = QtWidgets.QLabel(self.centralwidget)
        self.ELD1.setGeometry(QtCore.QRect(310, 357, 41, 31))
        self.ELD1.setText("")
        self.ELD1.setPixmap(QtGui.QPixmap(":/newPrefix/EGG.png"))
        self.ELD1.setObjectName("ELD1")
        self.ERU1 = QtWidgets.QLabel(self.centralwidget)
        self.ERU1.setGeometry(QtCore.QRect(860, 257, 41, 31))
        self.ERU1.setText("")
        self.ERU1.setPixmap(QtGui.QPixmap(":/newPrefix/EGG.png"))
        self.ERU1.setObjectName("ERU1")
        self.ERD1 = QtWidgets.QLabel(self.centralwidget)
        self.ERD1.setGeometry(QtCore.QRect(860, 357, 41, 31))
        self.ERD1.setText("")
        self.ERD1.setPixmap(QtGui.QPixmap(":/newPrefix/EGG.png"))
        self.ERD1.setObjectName("ERD1")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1222, 658))
        self.background.setToolTipDuration(0)
        self.background.setAutoFillBackground(False)
        self.background.setStyleSheet("")
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/fon2.png"))
        self.background.setObjectName("background")
        self.count = QtWidgets.QLCDNumber(self.centralwidget)
        self.count.setGeometry(QtCore.QRect(530, 170, 141, 41))
        self.count.setLineWidth(0)
        self.count.setMode(QtWidgets.QLCDNumber.Dec)
        self.count.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.count.setProperty("intValue", 0)
        self.count.setObjectName("count")
        self.lvl1 = QtWidgets.QPushButton(self.centralwidget)
        self.lvl1.setGeometry(QtCore.QRect(1030, 110, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lvl1.setFont(font)
        self.lvl1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lvl1.setCheckable(False)
        self.lvl1.setChecked(False)
        self.lvl1.setObjectName("lvl1")
        self.lvl2 = QtWidgets.QPushButton(self.centralwidget)
        self.lvl2.setGeometry(QtCore.QRect(1120, 110, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lvl2.setFont(font)
        self.lvl2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lvl2.setCheckable(False)
        self.lvl2.setChecked(False)
        self.lvl2.setObjectName("lvl2")
        self.labelLVL = QtWidgets.QLabel(self.centralwidget)
        self.labelLVL.setGeometry(QtCore.QRect(1030, 70, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.labelLVL.setFont(font)
        self.labelLVL.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.labelLVL.setStyleSheet("color: rgb(144, 29, 9);")
        self.labelLVL.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLVL.setObjectName("labelLVL")
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(410, 590, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.play.setFont(font)
        self.play.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.play.setStyleSheet("color: rgb(149, 11, 11);")
        self.play.setCheckable(False)
        self.play.setChecked(False)
        self.play.setObjectName("play")
        self.volume = QtWidgets.QPushButton(self.centralwidget)
        self.volume.setGeometry(QtCore.QRect(40, 210, 81, 71))
        self.volume.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.volume.setStyleSheet("")
        self.volume.setText("")
        self.icon1 = QtGui.QIcon()
        self.icon1.addPixmap(QtGui.QPixmap(":/newPrefix/volume.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.volume.setIcon(self.icon1)
        self.volume.setIconSize(QtCore.QSize(40, 40))
        self.volume.setCheckable(False)
        self.volume.setChecked(False)
        self.volume.setObjectName("volume")
        self.pravila = QtWidgets.QListWidget(self.centralwidget)
        self.pravila.setGeometry(QtCore.QRect(1020, 260, 201, 281))
        self.pravila.setObjectName("pravila")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.pravila.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.pravila.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.pravila.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.pravila.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.pravila.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.pravila.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.pravila.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.pravila.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.pravila.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.pravila.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.pravila.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.pravila.addItem(item)
        self.ButPravila = QtWidgets.QPushButton(self.centralwidget)
        self.ButPravila.setGeometry(QtCore.QRect(1090, 570, 71, 71))
        self.ButPravila.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButPravila.setStyleSheet("")
        self.ButPravila.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-question-mark-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButPravila.setIcon(icon2)
        self.ButPravila.setIconSize(QtCore.QSize(40, 40))
        self.ButPravila.setCheckable(False)
        self.ButPravila.setChecked(False)
        self.ButPravila.setObjectName("ButPravila")
        self.urlicon = QtWidgets.QLabel(self.centralwidget)
        self.urlicon.setGeometry(QtCore.QRect(10000, 480, 55, 16))
        self.urlicon.setObjectName("urlicon")
        self.labelgame = QtWidgets.QLabel(self.centralwidget)
        self.labelgame.setGeometry(QtCore.QRect(330, 160, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelgame.setFont(font)
        self.labelgame.setObjectName("labelgame")
        self.labelgame1 = QtWidgets.QLabel(self.centralwidget)
        self.labelgame1.setGeometry(QtCore.QRect(380, 160, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelgame1.setFont(font)
        self.labelgame1.setObjectName("labelgame1")
        self.labelgame2 = QtWidgets.QLabel(self.centralwidget)
        self.labelgame2.setGeometry(QtCore.QRect(390, 160, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelgame2.setFont(font)
        self.labelgame2.setObjectName("labelgame2")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(139, 17, 14))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 17, 14))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 17, 14))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 17, 14))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 17, 14))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 17, 14))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 17, 14))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 17, 14))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 17, 14))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.labelPomer = QtWidgets.QLabel(self.centralwidget)
        self.labelPomer.setGeometry(QtCore.QRect(420, 210, 391, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.labelPomer.setFont(font)
        self.labelPomer.setObjectName("label")
        # self.butFullScreen = QtWidgets.QPushButton(self.centralwidget)
        # self.butFullScreen.setGeometry(QtCore.QRect(40, 130, 81, 71))
        # self.butFullScreen.setText("")
        # icon3 = QtGui.QIcon()
        # icon3.addPixmap(QtGui.QPixmap(":/newPrefix/full-screen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.butFullScreen.setIcon(icon3)
        # self.butFullScreen.setIconSize(QtCore.QSize(50, 50))
        # self.butFullScreen.setObjectName("butFullScreen")
        self.butVihod = QtWidgets.QPushButton(self.centralwidget)
        self.butVihod.setGeometry(QtCore.QRect(40, 50, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.butVihod.setFont(font)
        self.butVihod.setStyleSheet("color: rgb(165, 55, 66);")
        self.butVihod.setObjectName("butVihod")
        self.background.raise_()
        self.VUL.raise_()
        self.VUR.raise_()
        self.VDR.raise_()
        self.ELU1.raise_()
        self.ELD1.raise_()
        self.ERU1.raise_()
        self.ERD1.raise_()
        self.count.raise_()
        self.lvl1.raise_()
        self.lvl2.raise_()
        self.labelLVL.raise_()
        self.play.raise_()
        self.volume.raise_()
        self.pravila.raise_()
        self.ButPravila.raise_()
        self.urlicon.raise_()
        self.labelgame.raise_()
        self.labelgame1.raise_()
        self.labelgame2.raise_()
        self.VDL.raise_()
        self.labelPomer.raise_()
        # self.butFullScreen.raise_()
        self.butVihod.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.egg1_x = 310
        self.egg1_y = 257

        self.egg2_x = 310
        self.egg2_y = 357

        self.egg3_x = 860
        self.egg3_y = 257

        self.egg4_x = 860
        self.egg4_y = 357

        self.egg_speed_x = 2
        self.egg_speed_y = 1


        self.VDR.grabKeyboard() #перевод фокуса на волка для стрелок

        # Визуализация виджетов
        self.EVUl = False
        self.EVDL = True
        self.EVDR = False
        self.EVUR = False
        self.VDR.setVisible(False)
        self.VUR.setVisible(False)
        self.VUL.setVisible(False)
        self.ELD1.setVisible(False)
        self.ELU1.setVisible(False)
        self.ERD1.setVisible(False)
        self.ERU1.setVisible(False)
        self.pravila.setVisible(False)
        self.labelPomer.setVisible(False)



        #Таймеры кнопок
        self.et1 = False
        self.et2 = False
        self.et3 = False
        self.et4 = False

        self.labelgame1.setVisible(True)
        self.labelgame2.setVisible(False)
        self.game_over = True
        self.lv = True

        # Исполение нажатий кнопок
        self.ButPravila.clicked.connect(self.vopros)
        self.play.clicked.connect(self.play_Game)
        self.lvl1.clicked.connect(self.play_lvl1)
        self.lvl2.clicked.connect(self.play_lvl2)
        self.volume.clicked.connect(self.playAudio)
        self.butVihod.clicked.connect(self.closeWindow)


        #Музыка
        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile("music\Atomic Heart OST — Trava u Doma (Geoffrey Day Remix, Земляне) (www.lightaudio.ru).mp3")))
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile("music\Mujuice_Pesnyary_Atomic_Heart_-_Kosil_Jas_Konjushinu_Mujuice_Acid_Rework_75479749.mp3")))
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile("music\DVRST, Игорь Скляр, Atomic Heart — Комарово(Phonk Remix) (www.lightaudio.ru).mp3")))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)# устанавливаем режим воспроизведения на циклический
        self.player = QMediaPlayer()
        self.player.setPlaylist(self.playlist)
        self.player.play()

        #Объявление таймеров
        self.timer1 = QTimer(self)
        self.timer1.setInterval(60)
        self.timer1.timeout.connect(self.updateEggPosition1)

        self.timer2 = QTimer(self)
        self.timer2.setInterval(60)
        self.timer2.timeout.connect(self.updateEggPosition2)

        self.timer3 = QTimer(self)
        self.timer3.setInterval(60)
        self.timer3.timeout.connect(self.updateEggPosition3)

        self.timer4 = QTimer(self)
        self.timer4.setInterval(60)
        self.timer4.timeout.connect(self.updateEggPosition4)

        self.timer = QTimer(self)
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.egg_time)


    def closeWindow(self):
        QtCore.QCoreApplication.quit()

    def play_lvl1(self):
        self.labelgame1.setVisible(True)
        self.labelgame2.setVisible(False)
        self.game_over = True
        self.lv = True
        self.timer.stop()
        self.play.setText('Играть')
        self.badshet = 3

    def play_lvl2(self):
        self.labelgame2.setVisible(True)
        self.labelgame1.setVisible(False)
        self.game_over = True
        self.lv = False
        self.timer.stop()
        self.play.setText('Играть')
        self.badshet = 3

    def play_Game(self):
        if self.game_over == True:
            self.game_over = False
            self.play.setText('Закончить')
            self.labelPomer.setVisible(False)
        else:
            self.game_over = True
            self.play.setText('Играть')

        if ((self.game_over == False) and (self.lv == True)):
            self.timer.setInterval(2000)
            self.timer.start()
            self.chet = 0
            self.badshet = 0
        elif ((self.game_over == False) and (self.lv == False)):
            self.timer.setInterval(1000)
            self.timer.start()
            self.chet = 0
            self.badshet = 0
        elif self.game_over == True:
            self.badshet = 3


    def vopros (self):
        self.fhelp += 1
        if self.fhelp % 2 == 0:
            self.pravila.setVisible(True)
            self.fhelp = 0
        else:
            self.pravila.setVisible(False)

    def playAudio (self):
        self.fmusic += 1
        if self.fmusic % 2 == 0:
            self.player.pause()
            self.fmusic = 0
            self.icon1.addPixmap(QtGui.QPixmap(":/newPrefix/mute.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.volume.setIcon(self.icon1)
        else:
            self.player.play()
            self.icon1.addPixmap(QtGui.QPixmap(":/newPrefix/volume.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.volume.setIcon(self.icon1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ну, Погоди!"))
        self.lvl1.setText(_translate("MainWindow", "1"))
        self.lvl2.setText(_translate("MainWindow", "2"))
        self.labelLVL.setText(_translate("MainWindow", "Уровень сложности"))
        self.play.setText(_translate("MainWindow", "Играть"))
        __sortingEnabled = self.pravila.isSortingEnabled()
        self.pravila.setSortingEnabled(False)
        item = self.pravila.item(0)
        item.setText(_translate("MainWindow", "Правила игры"))
        item = self.pravila.item(2)
        item.setText(_translate("MainWindow", "Управление волком "))
        item = self.pravila.item(3)
        item.setText(_translate("MainWindow", "производится с помощью "))
        item = self.pravila.item(4)
        item.setText(_translate("MainWindow", "стрелок на клавиатуре."))
        item = self.pravila.item(6)
        item.setText(_translate("MainWindow", "Цель: собрать как можно"))
        item = self.pravila.item(7)
        item.setText(_translate("MainWindow", "больше яиц."))
        item = self.pravila.item(9)
        item.setText(_translate("MainWindow", "Выберете уровень "))
        item = self.pravila.item(10)
        item.setText(_translate("MainWindow", "(1 - легкий, 2 - сложный)"))
        item = self.pravila.item(11)
        item.setText(_translate("MainWindow", "и нажмите кнопку \"Играть\""))
        self.pravila.setSortingEnabled(__sortingEnabled)
        self.urlicon.setText(_translate("MainWindow",
                                        "<a target=\"_blank\" href=\"https://icons8.com/icon/10568/question-mark\">Question Mark</a> icon by <a target=\"_blank\" href=\"https://icons8.com\">Icons8</a>"))
        self.labelgame.setText(_translate("MainWindow", "ИГРА"))
        self.labelgame1.setText(_translate("MainWindow", "1"))
        self.labelgame2.setText(_translate("MainWindow", "2"))
        self.labelPomer.setText(_translate("MainWindow", "Игра окончена"))
        self.butVihod.setText(_translate("MainWindow", "Выход"))


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Up:
            self.VUL.setVisible(True)
            self.VDL.setVisible(False)
            self.VDR.setVisible(False)
            self.VUR.setVisible(False)
            self.EVUl = True
            self.EVDL = False
            self.EVDR = False
            self.EVUR = False
        if e.key() == Qt.Key_Left:
            self.VUL.setVisible(False)
            self.VDL.setVisible(True)
            self.VDR.setVisible(False)
            self.VUR.setVisible(False)
            self.EVUl = False
            self.EVDL = True
            self.EVDR = False
            self.EVUR = False
        if e.key() == Qt.Key_Down:
            self.VUL.setVisible(False)
            self.VDL.setVisible(False)
            self.VDR.setVisible(True)
            self.VUR.setVisible(False)
            self.EVUl = False
            self.EVDL = False
            self.EVDR = True
            self.EVUR = False
        if e.key() == Qt.Key_Right:
            self.VUL.setVisible(False)
            self.VDL.setVisible(False)
            self.VDR.setVisible(False)
            self.VUR.setVisible(True)
            self.EVUl = False
            self.EVDL = False
            self.EVDR = False
            self.EVUR = True

    def egg_time(self):
        self.count.setProperty("intValue", self.chet)
        e = random.randint(0,1000000)
        if 0 <= e <= 250000:
            self.egg_spawn = 1
        elif 250001 <= e <= 500000:
            self.egg_spawn = 2
        elif 500001 <= e <= 750000:
            self.egg_spawn = 3
        else:
            self.egg_spawn = 4

        if self.chet <= 10:
            self.timer1.setInterval(60)
            self.timer2.setInterval(60)
            self.timer3.setInterval(60)
            self.timer4.setInterval(60)
        elif 10 < self.chet <= 30:
            self.timer1.setInterval(45)
            self.timer2.setInterval(45)
            self.timer3.setInterval(45)
            self.timer4.setInterval(45)
        elif 30 < self.chet <= 40:
            self.timer1.setInterval(30)
            self.timer2.setInterval(30)
            self.timer3.setInterval(30)
            self.timer4.setInterval(30)
        elif 40 < self.chet <= 50:
            self.timer1.setInterval(15)
            self.timer2.setInterval(15)
            self.timer3.setInterval(15)
            self.timer4.setInterval(15)
        elif 50 < self.chet <= 60:
            self.timer1.setInterval(60)
            self.timer2.setInterval(60)
            self.timer3.setInterval(60)
            self.timer4.setInterval(60)
        elif 60 < self.chet <= 70:
            self.timer1.setInterval(30)
            self.timer2.setInterval(30)
            self.timer3.setInterval(30)
            self.timer4.setInterval(30)
        elif 70 < self.chet <= 80:
            self.timer1.setInterval(15)
            self.timer2.setInterval(15)
            self.timer3.setInterval(15)
            self.timer4.setInterval(15)
        elif 80 < self.chet:
            self.timer1.setInterval(20)
            self.timer2.setInterval(20)
            self.timer3.setInterval(20)
            self.timer4.setInterval(20)

        if self.egg_spawn == 1:

            self.et1 = True
            self.timer1.start()

        if self.egg_spawn == 2:

            self.et2 = True
            self.timer2.start()

        if self.egg_spawn == 3:

            self.et3 = True
            self.timer3.start()

        if self.egg_spawn == 4:

            self.et4 = True
            self.timer4.start()

    def updateEggPosition1(self):
        self.count.setProperty("intValue", self.chet)
        self.ELU1.move(self.egg1_x, self.egg1_y)
        self.ELU1.setVisible(True)
        self.egg1_x += self.egg_speed_x
        self.egg1_y += self.egg_speed_y  # (390;297)

        if self.egg1_x >= 390 and self.egg1_y >= 297 and self.EVUl == True :
            self.chet += 1
            self.egg1_x = 310
            self.egg1_y = 257
            self.ELU1.setVisible(False)
            self.timer1.stop()
            self.et1 = False
        elif self.egg1_x >= 390 and self.egg1_y >= 297 and self.EVUl == False:
            self.badshet +=1
            self.egg1_x = 310
            self.egg1_y = 257
            self.ELU1.move(self.egg1_x, self.egg1_y)
            self.ELU1.setVisible(False)
            self.timer1.stop()
            self.et1 = False
        else:
            self.ELU1.move(self.egg1_x, self.egg1_y)

        if self.badshet == 3:
            self.End()

    def updateEggPosition2(self):
        self.count.setProperty("intValue", self.chet)
        self.ELD1.move(self.egg2_x, self.egg2_y)
        self.ELD1.setVisible(True)
        self.egg2_x += self.egg_speed_x
        self.egg2_y += self.egg_speed_y #(390;397)


        if self.egg2_x >= 390 and self.egg2_y >= 397 and self.EVDL == True:
            self.chet += 1
            self.egg2_x = 310
            self.egg2_y = 357
            self.ELD1.setVisible(False)
            self.timer2.stop()
            self.et2 = False
        elif self.egg2_x >= 390 and self.egg2_y >= 397 and self.EVDL == False:
            self.badshet += 1
            self.egg2_x = 310
            self.egg2_y = 357
            self.ELD1.setVisible(False)
            self.timer2.stop()
            self.et2 = False
        else:
            self.ELD1.move(self.egg2_x, self.egg2_y)

        if self.badshet == 3:
            self.End()

    def updateEggPosition3(self):
        self.count.setProperty("intValue", self.chet)
        self.ERU1.move(self.egg3_x, self.egg3_y)
        self.ERU1.setVisible(True)
        self.egg3_x -= self.egg_speed_x
        self.egg3_y += self.egg_speed_y #(780;297)

        if self.egg3_x <= 780 and self.egg3_y >= 297 and self.EVUR == True:
            self.chet += 1
            self.egg3_x = 860
            self.egg3_y = 257
            self.ERU1.setVisible(False)
            self.timer3.stop()
            self.et3 = False
        elif self.egg3_x <= 780 and self.egg3_y >= 297 and self.EVUR == False:
            self.badshet += 1
            self.egg3_x = 860
            self.egg3_y = 257
            self.ERU1.setVisible(False)
            self.timer3.stop()
            self.et3 = False
        else:
            self.ERU1.move(self.egg3_x, self.egg3_y)

        if self.badshet == 3:
            self.End()

    def updateEggPosition4(self):
        self.count.setProperty("intValue", self.chet)
        self.ERD1.move(self.egg4_x, self.egg4_y)
        self.ERD1.setVisible(True)
        self.egg4_x -= self.egg_speed_x
        self.egg4_y += self.egg_speed_y #(780;397)

        if self.egg4_x <= 780 and self.egg4_y >= 397 and self.EVDR == True:
            self.chet += 1
            self.egg4_x = 860
            self.egg4_y = 357
            self.ERD1.setVisible(False)
            self.timer4.stop()
            self.et4 = False
        elif self.egg4_x <= 780 and self.egg4_y >= 397 and self.EVDR == False:
            self.badshet += 1
            self.egg4_x = 860
            self.egg4_y = 357
            self.ERD1.setVisible(False)
            self.timer4.stop()
            self.et4 = False
        else:
            self.ERD1.move(self.egg4_x, self.egg4_y)

        if self.badshet == 3:
            self.End()

    def End(self):
        self.timer.stop()
        self.labelPomer.setVisible(True)
        self.game_over = True
        self.play.setText('Играть')
        self.timer1.stop()
        self.timer2.stop()
        self.timer3.stop()
        self.timer4.stop()
        self.ELU1.setVisible(False)
        self.ELD1.setVisible(False)
        self.ERU1.setVisible(False)
        self.ERD1.setVisible(False)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = Ui_MainWindow()

    ui.show()
    sys.exit(app.exec_())