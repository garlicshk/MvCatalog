# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_edit.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(784, 726)
        self.gridLayout_4 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_2.addWidget(self.label_21)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lineEdit_file_name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_file_name.setReadOnly(True)
        self.lineEdit_file_name.setObjectName("lineEdit_file_name")
        self.gridLayout_7.addWidget(self.lineEdit_file_name, 0, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setObjectName("label_17")
        self.gridLayout_7.addWidget(self.label_17, 4, 1, 1, 1)
        self.lineEdit_resolution = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_resolution.setReadOnly(True)
        self.lineEdit_resolution.setObjectName("lineEdit_resolution")
        self.gridLayout_7.addWidget(self.lineEdit_resolution, 2, 2, 1, 1)
        self.lineEdit_bitrate = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_bitrate.setReadOnly(True)
        self.lineEdit_bitrate.setObjectName("lineEdit_bitrate")
        self.gridLayout_7.addWidget(self.lineEdit_bitrate, 4, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setObjectName("label_15")
        self.gridLayout_7.addWidget(self.label_15, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setObjectName("label_13")
        self.gridLayout_7.addWidget(self.label_13, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setObjectName("label_14")
        self.gridLayout_7.addWidget(self.label_14, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setObjectName("label_16")
        self.gridLayout_7.addWidget(self.label_16, 3, 1, 1, 1)
        self.lineEdit_size = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_size.setReadOnly(True)
        self.lineEdit_size.setObjectName("lineEdit_size")
        self.gridLayout_7.addWidget(self.lineEdit_size, 1, 2, 1, 1)
        self.lineEdit_codec = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_codec.setReadOnly(True)
        self.lineEdit_codec.setObjectName("lineEdit_codec")
        self.gridLayout_7.addWidget(self.lineEdit_codec, 3, 2, 1, 1)
        self.lineEdit_file_length = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_file_length.setReadOnly(True)
        self.lineEdit_file_length.setObjectName("lineEdit_file_length")
        self.gridLayout_7.addWidget(self.lineEdit_file_length, 5, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setObjectName("label_19")
        self.gridLayout_7.addWidget(self.label_19, 6, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setObjectName("label_18")
        self.gridLayout_7.addWidget(self.label_18, 5, 1, 1, 1)
        self.lineEdit_audio = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_audio.setReadOnly(True)
        self.lineEdit_audio.setObjectName("lineEdit_audio")
        self.gridLayout_7.addWidget(self.lineEdit_audio, 6, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setObjectName("label_20")
        self.gridLayout_7.addWidget(self.label_20, 7, 1, 1, 1)
        self.lineEdit_subs = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_subs.setReadOnly(True)
        self.lineEdit_subs.setObjectName("lineEdit_subs")
        self.gridLayout_7.addWidget(self.lineEdit_subs, 7, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_7, 3, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 4, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 8, 0, 1, 1)
        self.lineEdit_country = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_country.setObjectName("lineEdit_country")
        self.gridLayout_3.addWidget(self.lineEdit_country, 3, 1, 1, 1)
        self.lineEdit_genre = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_genre.setObjectName("lineEdit_genre")
        self.gridLayout_3.addWidget(self.lineEdit_genre, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 10, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 9, 0, 1, 1)
        self.lineEdit_director = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_director.setObjectName("lineEdit_director")
        self.gridLayout_3.addWidget(self.lineEdit_director, 7, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 7, 0, 1, 1)
        self.lineEdit_orig_name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_orig_name.setObjectName("lineEdit_orig_name")
        self.gridLayout_3.addWidget(self.lineEdit_orig_name, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_rating = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_rating.setObjectName("lineEdit_rating")
        self.gridLayout_3.addWidget(self.lineEdit_rating, 6, 1, 1, 1)
        self.lineEdit_actors = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_actors.setObjectName("lineEdit_actors")
        self.gridLayout_3.addWidget(self.lineEdit_actors, 9, 1, 1, 1)
        self.lineEdit_movie_length = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_movie_length.setObjectName("lineEdit_movie_length")
        self.gridLayout_3.addWidget(self.lineEdit_movie_length, 5, 1, 1, 1)
        self.textEdit_description = QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_description.sizePolicy().hasHeightForWidth())
        self.textEdit_description.setSizePolicy(sizePolicy)
        self.textEdit_description.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textEdit_description.setObjectName("textEdit_description")
        self.gridLayout_3.addWidget(self.textEdit_description, 10, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_movie_name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_movie_name.setObjectName("lineEdit_movie_name")
        self.horizontalLayout_3.addWidget(self.lineEdit_movie_name)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.lineEdit_year = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_year.setObjectName("lineEdit_year")
        self.gridLayout_3.addWidget(self.lineEdit_year, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEdit_script = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_script.setObjectName("lineEdit_script")
        self.gridLayout_3.addWidget(self.lineEdit_script, 8, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.label_poster = QtWidgets.QLabel(Dialog)
        self.label_poster.setMinimumSize(QtCore.QSize(240, 426))
        self.label_poster.setMaximumSize(QtCore.QSize(240, 426))
        self.label_poster.setText("")
        self.label_poster.setPixmap(QtGui.QPixmap(":/newPrefix/placeholder.png"))
        self.label_poster.setObjectName("label_poster")
        self.gridLayout_4.addWidget(self.label_poster, 1, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_frames = QtWidgets.QLabel(Dialog)
        self.label_frames.setText("")
        self.label_frames.setPixmap(QtGui.QPixmap(":/newPrefix/placeholder.png"))
        self.label_frames.setObjectName("label_frames")
        self.verticalLayout.addWidget(self.label_frames)
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalSlider.setMaximum(0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.gridLayout_4.addLayout(self.verticalLayout, 3, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_4.addWidget(self.progressBar, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_21.setText(_translate("Dialog", "Файл"))
        self.pushButton_2.setText(_translate("Dialog", "Открыть"))
        self.lineEdit_file_name.setText(_translate("Dialog", "test.file"))
        self.label_17.setText(_translate("Dialog", "Битрейт"))
        self.lineEdit_resolution.setText(_translate("Dialog", "320x240"))
        self.lineEdit_bitrate.setText(_translate("Dialog", "1000"))
        self.label_15.setText(_translate("Dialog", "Разрешение"))
        self.label_13.setText(_translate("Dialog", "Имя файла"))
        self.label_14.setText(_translate("Dialog", "Размер"))
        self.label_16.setText(_translate("Dialog", "Кодек"))
        self.lineEdit_size.setText(_translate("Dialog", "100"))
        self.lineEdit_codec.setText(_translate("Dialog", "mpg"))
        self.lineEdit_file_length.setText(_translate("Dialog", "100"))
        self.label_19.setText(_translate("Dialog", "Аудио"))
        self.label_18.setText(_translate("Dialog", "Длительность"))
        self.lineEdit_audio.setText(_translate("Dialog", "Русский"))
        self.label_20.setText(_translate("Dialog", "Субтитры"))
        self.label_22.setText(_translate("Dialog", "Фильм"))
        self.pushButton.setText(_translate("Dialog", "Сохранить"))
        self.label_7.setText(_translate("Dialog", "Рейтинг, MPAA"))
        self.label_3.setText(_translate("Dialog", "Год"))
        self.label_9.setText(_translate("Dialog", "Сценарий"))
        self.lineEdit_country.setText(_translate("Dialog", "Россия"))
        self.lineEdit_genre.setText(_translate("Dialog", "Комедия"))
        self.label_2.setText(_translate("Dialog", "Ориг. название"))
        self.label_11.setText(_translate("Dialog", "Описание"))
        self.label_10.setText(_translate("Dialog", "Актёры"))
        self.lineEdit_director.setText(_translate("Dialog", "test"))
        self.label_8.setText(_translate("Dialog", "Режиссёр"))
        self.lineEdit_orig_name.setText(_translate("Dialog", "test name"))
        self.label.setText(_translate("Dialog", "Название"))
        self.lineEdit_rating.setText(_translate("Dialog", "test"))
        self.lineEdit_actors.setText(_translate("Dialog", "test"))
        self.lineEdit_movie_length.setText(_translate("Dialog", "100"))
        self.textEdit_description.setPlaceholderText(_translate("Dialog", "test"))
        self.lineEdit_movie_name.setText(_translate("Dialog", "test"))
        self.pushButton_3.setText(_translate("Dialog", "Поиск"))
        self.lineEdit_year.setText(_translate("Dialog", "2019"))
        self.label_6.setText(_translate("Dialog", "Длительность, мин."))
        self.label_5.setText(_translate("Dialog", "Жанр"))
        self.lineEdit_script.setText(_translate("Dialog", "test"))
        self.label_4.setText(_translate("Dialog", "Страны"))
import resource_rc
