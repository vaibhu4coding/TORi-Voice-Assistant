def __init__(self):
        
        self.ui = Ui_TORiUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

def startTask(self):
        self.ui.movie = QtGui.QMovie("image_processing20200620-21668-36w7bn.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("Jarvis_Loading_Screen.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("loader_sci-fi.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("loader_sci-fi.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("loader_sci-fi.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("voice effect 2.gif")
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("8871.gif")
        self.ui.label_9.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        startExecution.start()

def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser_2.setText(label_date)
        self.ui.textBrowser_3.setText(label_time)
app = QApplication(sys.argv)
tori = Main()
tori.show()
exit(app.exec_())   