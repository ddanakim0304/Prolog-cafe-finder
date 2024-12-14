from PyQt5 import QtCore, QtGui, QtWidgets
from pyswip import Prolog

# Initialize Prolog interface
prolog = Prolog()
prolog.consult("cafes.pl")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(771, 851)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Cafe Name Label
        self.cafe_name = QtWidgets.QLabel(self.centralwidget)
        self.cafe_name.setGeometry(QtCore.QRect(20, 350, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.cafe_name.setFont(font)
        self.cafe_name.setObjectName("cafe_name")
        self.cafe_name.setText("Dandy Cafe")  # Default text

        # Cafe Address Label
        self.cafe_address = QtWidgets.QLabel(self.centralwidget)
        self.cafe_address.setGeometry(QtCore.QRect(20, 420, 271, 61))
        self.cafe_address.setWordWrap(True)
        self.cafe_address.setObjectName("cafe_address")
        self.cafe_address.setText("")  # Default text

        # Results Info Label
        self.result_info = QtWidgets.QLabel(self.centralwidget)
        self.result_info.setEnabled(False)
        self.result_info.setGeometry(QtCore.QRect(20, 460, 400, 40))
        self.result_info.setObjectName("result_info")
        self.result_info.setText("Results will be displayed here.")  # Default text

        # Other UI components...
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 40, 281, 291))
        self.graphicsView.setObjectName("graphicsView")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(260, 0, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        # Previous Button
        self.previous_button = QtWidgets.QPushButton(self.centralwidget)
        self.previous_button.setGeometry(QtCore.QRect(50, 590, 100, 32))
        self.previous_button.setObjectName("previous_button")
        self.previous_button.setText("Previous")
        self.previous_button.clicked.connect(self.show_previous_cafe)

        # Next Button
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(170, 590, 100, 32))
        self.next_button.setObjectName("next_button")
        self.next_button.setText("Next")
        self.next_button.clicked.connect(self.show_next_cafe)

        self.manage_constraints = QtWidgets.QGroupBox(self.centralwidget)
        self.manage_constraints.setGeometry(QtCore.QRect(330, 590, 371, 61))
        self.manage_constraints.setObjectName("manage_constraints")
        self.comboBox = QtWidgets.QComboBox(self.manage_constraints)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 211, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.manage_constraints)
        self.pushButton.setGeometry(QtCore.QRect(260, 20, 100, 32))
        self.pushButton.setObjectName("pushButton")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(330, 110, 371, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setAlignment(QtCore.Qt.AlignTop)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Opening/Closing Times Group Box
        self.opening_closing = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.opening_closing.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.opening_closing.sizePolicy().hasHeightForWidth()
        )
        self.opening_closing.setSizePolicy(sizePolicy)
        self.opening_closing.setMinimumSize(QtCore.QSize(356, 143))
        self.opening_closing.setBaseSize(QtCore.QSize(0, 120))
        self.opening_closing.setObjectName("opening_closing")
        self.label_9 = QtWidgets.QLabel(self.opening_closing)
        self.label_9.setGeometry(QtCore.QRect(20, 60, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.daySelect = QtWidgets.QComboBox(self.opening_closing)
        self.daySelect.setGeometry(QtCore.QRect(10, 30, 211, 32))
        self.daySelect.setObjectName("daySelect")
        self.daySelect.addItem("")
        self.daySelect.addItem("")
        self.daySelect.addItem("")
        self.daySelect.addItem("")
        self.daySelect.addItem("")
        self.daySelect.addItem("")
        self.daySelect.addItem("")
        self.label_10 = QtWidgets.QLabel(self.opening_closing)
        self.label_10.setGeometry(QtCore.QRect(20, 90, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.remove_opening_closing = QtWidgets.QPushButton(self.opening_closing)
        self.remove_opening_closing.setGeometry(QtCore.QRect(250, 30, 100, 32))
        self.remove_opening_closing.setObjectName("remove_opening_closing")
        self.from_time = QtWidgets.QTimeEdit(self.opening_closing)
        self.from_time.setGeometry(QtCore.QRect(100, 60, 118, 22))
        self.from_time.setObjectName("from_time")
        self.to_time = QtWidgets.QTimeEdit(self.opening_closing)
        self.to_time.setGeometry(QtCore.QRect(100, 90, 118, 22))
        self.to_time.setObjectName("to_time")
        self.label_12 = QtWidgets.QLabel(self.opening_closing)
        self.label_12.setEnabled(False)
        self.label_12.setGeometry(QtCore.QRect(110, 120, 131, 16))
        self.label_12.setStyleSheet("")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.opening_closing)

        # Transportation Group Box
        self.transportation = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.transportation.sizePolicy().hasHeightForWidth()
        )
        self.transportation.setSizePolicy(sizePolicy)
        self.transportation.setMinimumSize(QtCore.QSize(357, 114))
        self.transportation.setObjectName("transportation")
        self.transportType = QtWidgets.QComboBox(self.transportation)
        self.transportType.setGeometry(QtCore.QRect(10, 30, 131, 21))
        self.transportType.setMaxVisibleItems(3)
        self.transportType.setPlaceholderText("")
        self.transportType.setObjectName("transportType")
        self.transportType.addItem("")
        self.transportType.addItem("")
        self.transportType.addItem("")
        self.travel_time = QtWidgets.QLineEdit(self.transportation)
        self.travel_time.setGeometry(QtCore.QRect(50, 60, 81, 21))
        self.travel_time.setObjectName("travel_time")
        self.label_7 = QtWidgets.QLabel(self.transportation)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 31, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.transportation)
        self.label_8.setGeometry(QtCore.QRect(140, 60, 71, 16))
        self.label_8.setObjectName("label_8")
        self.remove_transportation = QtWidgets.QPushButton(self.transportation)
        self.remove_transportation.setGeometry(QtCore.QRect(250, 30, 100, 32))
        self.remove_transportation.setObjectName("remove_transportation")
        self.transportation_warning = QtWidgets.QLabel(self.transportation)
        self.transportation_warning.setEnabled(False)
        self.transportation_warning.setGeometry(QtCore.QRect(110, 90, 131, 16))
        self.transportation_warning.setStyleSheet("")
        self.transportation_warning.setObjectName("transportation_warning")
        self.verticalLayout_2.addWidget(self.transportation)

        # Power Sockets Group Box
        self.power_sockets = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.power_sockets.sizePolicy().hasHeightForWidth()
        )
        self.power_sockets.setSizePolicy(sizePolicy)
        self.power_sockets.setMinimumSize(QtCore.QSize(0, 60))
        self.power_sockets.setObjectName("power_sockets")
        self.socketCheck = QtWidgets.QCheckBox(self.power_sockets)
        self.socketCheck.setEnabled(True)
        self.socketCheck.setGeometry(QtCore.QRect(10, 30, 171, 20))
        self.socketCheck.setCheckable(True)
        self.socketCheck.setChecked(True)
        self.socketCheck.setObjectName("socketCheck")
        self.remove_power_sockets = QtWidgets.QPushButton(self.power_sockets)
        self.remove_power_sockets.setGeometry(QtCore.QRect(250, 20, 100, 32))
        self.remove_power_sockets.setObjectName("remove_power_sockets")
        self.verticalLayout_2.addWidget(self.power_sockets)

        # Wifi Group Box
        self.wifi = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wifi.sizePolicy().hasHeightForWidth())
        self.wifi.setSizePolicy(sizePolicy)
        self.wifi.setMinimumSize(QtCore.QSize(0, 60))
        self.wifi.setObjectName("wifi")
        self.wifi_check = QtWidgets.QCheckBox(self.wifi)
        self.wifi_check.setEnabled(True)
        self.wifi_check.setGeometry(QtCore.QRect(10, 30, 171, 20))
        self.wifi_check.setCheckable(True)
        self.wifi_check.setChecked(True)
        self.wifi_check.setObjectName("wifi_check")
        self.remove_wifi = QtWidgets.QPushButton(self.wifi)
        self.remove_wifi.setGeometry(QtCore.QRect(250, 20, 100, 32))
        self.remove_wifi.setObjectName("remove_wifi")
        self.verticalLayout_2.addWidget(self.wifi)

        # Dietary Preference Group Box
        self.dietary_pref = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dietary_pref.sizePolicy().hasHeightForWidth())
        self.dietary_pref.setSizePolicy(sizePolicy)
        self.dietary_pref.setMinimumSize(QtCore.QSize(357, 67))
        self.dietary_pref.setObjectName("dietary_pref")
        self.dietaryPreference = QtWidgets.QComboBox(self.dietary_pref)
        self.dietaryPreference.setGeometry(QtCore.QRect(10, 30, 211, 32))
        self.dietaryPreference.setObjectName("dietaryPreference")
        self.dietaryPreference.addItem("")
        self.dietaryPreference.addItem("")
        self.dietaryPreference.addItem("")
        self.remove_diet = QtWidgets.QPushButton(self.dietary_pref)
        self.remove_diet.setGeometry(QtCore.QRect(250, 30, 100, 32))
        self.remove_diet.setObjectName("remove_diet")
        self.verticalLayout_2.addWidget(self.dietary_pref)

        # Price Group Box
        self.price = QtWidgets.QGroupBox(self.centralwidget)
        self.price.setGeometry(QtCore.QRect(330, 40, 371, 61))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Ignored
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.price.sizePolicy().hasHeightForWidth())
        self.price.setSizePolicy(sizePolicy)
        self.price.setMinimumSize(QtCore.QSize(357, 0))
        self.price.setMaximumSize(QtCore.QSize(500, 440))
        self.price.setObjectName("price")
        self.label_6 = QtWidgets.QLabel(self.price)
        self.label_6.setGeometry(QtCore.QRect(140, 30, 58, 16))
        self.label_6.setObjectName("label_6")
        self.maximumPrice = QtWidgets.QLineEdit(self.price)
        self.maximumPrice.setGeometry(QtCore.QRect(10, 30, 113, 21))
        self.maximumPrice.setObjectName("maximumPrice")
        self.maximumPrice.textChanged.connect(self.updateMaximumPrice)

        # Cafe Name Label
        self.cafe_name_label = QtWidgets.QLabel(self.centralwidget)
        self.cafe_name_label.setGeometry(QtCore.QRect(70, 340, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.cafe_name_label.setFont(font)
        self.cafe_name_label.setObjectName("cafe_name_label")

        # Cafe Address Label
        self.cafe_address_label = QtWidgets.QLabel(self.centralwidget)
        self.cafe_address_label.setGeometry(QtCore.QRect(50, 400, 221, 51))
        self.cafe_address_label.setWordWrap(True)
        self.cafe_address_label.setObjectName("cafe_address_label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 771, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.clear_vertical_layout()

        # Define data handlers
        self.cafe_results = []
        self.current_index = 0

        # Initialize constraint variables with 'any' to represent no constraints initially
        self.transportVar = "any"
        self.maxTimeVar = "any"
        self.priceVar = "any"
        self.wifiVar = "any"                      
        self.socketsVar = "any"                   
        self.veganPreferenceVar = "none"          
        self.needsMealsVar = "any"                
        self.visitDayVar = "any"                   
        self.fromVar = "any"                       
        self.toVar = "any"                         
        self.dayOptions = {}

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cafe Finder"))
        self.cafe_name.setText(_translate("MainWindow", ""))
        self.label_11.setText(_translate("MainWindow", "CAFE FINDER"))
        self.previous_button.setText(_translate("MainWindow", "Previous"))
        self.manage_constraints.setTitle(_translate("MainWindow", "Manage Constraints"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Travel Time"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Must have wifi"))
        self.comboBox.setItemText(
            2, _translate("MainWindow", "Must have power sockets")
        )
        self.comboBox.setItemText(3, _translate("MainWindow", "Dietary Preference"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Meals"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Opening Time"))

        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.pushButton.clicked.connect(self.re_add_constraint)
        self.next_button.setText(_translate("MainWindow", "Next"))
        self.result_info.setText(_translate("MainWindow", "Input Time is in 24hrs"))
        self.opening_closing.setTitle(_translate("MainWindow", "Opening/Closing times"))
        self.label_9.setText(_translate("MainWindow", "From"))
        self.daySelect.setItemText(0, _translate("MainWindow", "monday"))
        self.daySelect.setItemText(1, _translate("MainWindow", "tuesday"))
        self.daySelect.setItemText(2, _translate("MainWindow", "wednesday"))
        self.daySelect.setItemText(3, _translate("MainWindow", "thursday"))
        self.daySelect.setItemText(4, _translate("MainWindow", "friday"))
        self.daySelect.setItemText(5, _translate("MainWindow", "saturday"))
        self.daySelect.setItemText(6, _translate("MainWindow", "sunday"))
        self.label_10.setText(_translate("MainWindow", "To"))
        self.remove_opening_closing.setText(_translate("MainWindow", "Remove"))
        self.label_12.setText(_translate("MainWindow", ""))
        self.transportation.setTitle(_translate("MainWindow", "Transportation"))
        self.transportType.setItemText(0, _translate("MainWindow", "Walk"))
        self.transportType.setItemText(1, _translate("MainWindow", "Public Transport"))
        self.transportType.setItemText(2, _translate("MainWindow", "Taxi/Moto"))
        self.label_7.setText(_translate("MainWindow", "for"))
        self.label_8.setText(_translate("MainWindow", "minutes"))
        self.remove_transportation.setText(_translate("MainWindow", "Remove"))
        self.transportation_warning.setText(
            _translate("MainWindow", "Input Time is in 24hrs")
        )
        self.power_sockets.setTitle(_translate("MainWindow", "Power sockets"))
        self.socketCheck.setText(_translate("MainWindow", "Must have power sockets"))
        self.remove_power_sockets.setText(_translate("MainWindow", "Remove"))
        self.wifi.setTitle(_translate("MainWindow", "Wifi"))
        self.wifi_check.setText(_translate("MainWindow", "Must have wifi"))
        self.remove_wifi.setText(_translate("MainWindow", "Remove"))
        self.dietary_pref.setTitle(_translate("MainWindow", "Dietary Preference"))
        self.dietaryPreference.setItemText(0, _translate("MainWindow", "vegan"))
        self.dietaryPreference.setItemText(1, _translate("MainWindow", "vegetarian"))
        self.dietaryPreference.setItemText(2, _translate("MainWindow", "none"))
        self.remove_diet.setText(_translate("MainWindow", "Remove"))
        self.price.setTitle(_translate("MainWindow", "What is the maximum price"))
        self.label_6.setText(_translate("MainWindow", "pesos"))

        # Connect all remove buttons to their respective handlers
        self.remove_opening_closing.clicked.connect(self.remove_opening_closing_widget)
        self.remove_transportation.clicked.connect(self.remove_transportation_widget)
        self.remove_power_sockets.clicked.connect(self.remove_power_sockets_widget)
        self.remove_wifi.clicked.connect(self.remove_wifi_widget)
        self.remove_diet.clicked.connect(self.remove_diet_widget)

        self.from_time.timeChanged.connect(self.check_correct_from_to_time)
        self.to_time.timeChanged.connect(self.check_correct_from_to_time)

    def remove_transportation_widget(self):
        self.transportVar = "any"
        self.maxTimeVar = "any"
        self.getCafes()
        self.verticalLayout_2.removeWidget(self.transportation)
        self.transportation.hide()

    def remove_power_sockets_widget(self):
        self.socketsVar = "any"
        self.getCafes()
        self.verticalLayout_2.removeWidget(self.power_sockets)
        self.power_sockets.hide()

    def remove_diet_widget(self):
        self.veganPreferenceVar = "any"
        self.needsMealsVar = "any"
        self.getCafes()
        self.verticalLayout_2.removeWidget(self.dietary_pref)
        self.dietary_pref.hide()

    def remove_opening_closing_widget(self):
        # Reset to 'any' to ignore day and time constraints
        self.visitDayVar = "any"
        self.fromVar = "any"
        self.toVar = "any"
        self.getCafes()
        self.verticalLayout_2.removeWidget(self.opening_closing)
        self.opening_closing.hide()

    def remove_wifi_widget(self):
        self.wifiVar = "any"  # Set to 'any' to ignore wifi constraint
        self.getCafes()
        self.verticalLayout_2.removeWidget(self.wifi)
        self.wifi.hide()

    def getMealOptions(self):
        try:
            query = f"""findall(
                Cafe,
                suitable_cafe(
                    Cafe,
                    '{self.transportVar}', 
                    {self.maxTimeVar if self.transportVar != "any" else 'any'}, 
                    {self.priceVar if self.priceVar != "any" else 'any'}, 
                    '{self.wifiVar}', 
                    '{self.socketsVar}', 
                    '{self.veganPreferenceVar}', 
                    '{self.needsMealsVar}', 
                    '{self.visitDayVar}', 
                    {self.fromVar}, 
                    {self.toVar}
                ),
                Cafes
            )."""
            
            result = list(prolog.query(query))
            
            if result:
                cafes = [entry['Cafe'] for entry in result]
            else:
                cafes = []
            
            meal_options = set()
            for cafe in cafes:
                meal_query = f"meals('{cafe}', MealOpt)."
                meal_result = list(prolog.query(meal_query))
                if meal_result:
                    meal_opt = meal_result[0]['MealOpt']
                    meal_options.add(meal_opt)
            
            if "yes" in meal_options:
                return True
            else:
                return False
        
        except Exception as e:
            print(f"Error in getMealOptions: {e}")
            return False


    def getSocketOptions(self):
        try:
            query = f"""findall(
                Cafe,
                suitable_cafe(
                    Cafe,
                    '{self.transportVar}', 
                    {self.maxTimeVar if self.transportVar != "any" else 'any'}, 
                    {self.priceVar if self.priceVar != "any" else 'any'}, 
                    '{self.wifiVar}', 
                    '{self.socketsVar}', 
                    '{self.veganPreferenceVar}', 
                    '{self.needsMealsVar}', 
                    '{self.visitDayVar}', 
                    {self.fromVar}, 
                    {self.toVar}
                ),
                Cafes
            )."""
            
            result = list(prolog.query(query))
            
            if result:
                cafes = [entry['Cafe'] for entry in result]
            else:
                cafes = []
            
            socket_options = set()
            for cafe in cafes:
                socket_query = f"sockets('{cafe}', Socket)."
                socket_result = list(prolog.query(socket_query))
                if socket_result:
                    socket = socket_result[0]['Socket']
                    socket_options.add(socket)

            if "yes" in socket_options:
                return True
            else:
                return False
        
        except Exception as e:
            print(f"Error in getSocketOptions: {e}")
            return False


    def getWifiOptions(self):
        try:
            query = f"""findall(
                Cafe,
                suitable_cafe(
                    Cafe,
                    '{self.transportVar}', 
                    {self.maxTimeVar if self.transportVar != "any" else 'any'}, 
                    {self.priceVar if self.priceVar != "any" else 'any'}, 
                    '{self.wifiVar}', 
                    '{self.socketsVar}', 
                    '{self.veganPreferenceVar}', 
                    '{self.needsMealsVar}', 
                    '{self.visitDayVar}', 
                    {self.fromVar}, 
                    {self.toVar}
                ),
                Cafes
            )."""
            
            result = list(prolog.query(query))
            
            if result:
                cafes = [entry['Cafe'] for entry in result]
            else:
                cafes = []

            wifi_options = set()
            for cafe in cafes:
                wifi_query = f"wifi('{cafe}', WifiStatus)."
                wifi_result = list(prolog.query(wifi_query))
                if wifi_result:
                    wifi_status = wifi_result[0]['WifiStatus']
                    wifi_options.add(wifi_status)
            
            if "yes" in wifi_options:
                return True
            else:
                return False
        
        except Exception as e:
            print(f"Error in getWifiOptions: {e}")
            return False


    def getOpenDays(self):
        try:
            query = f"""findall(
                Cafe,
                suitable_cafe(
                    Cafe,
                    '{self.transportVar}', 
                    {self.maxTimeVar if self.transportVar != "any" else 'any'}, 
                    {self.priceVar if self.priceVar != "any" else 'any'}, 
                    '{self.wifiVar}', 
                    '{self.socketsVar}', 
                    '{self.veganPreferenceVar}', 
                    '{self.needsMealsVar}', 
                    '{self.visitDayVar}', 
                    {self.fromVar}, 
                    {self.toVar}
                ),
                Cafes
            )."""
            
            print("Prolog Query for Suitable Cafes (Open Days):", query)  # Debug
            result = list(prolog.query(query))
            
            if result:
                cafes = [entry['Cafe'] for entry in result]
            else:
                cafes = []
            
            day_open_close = {}
            for cafe in cafes:
                days_query = f"days_opened('{cafe}', DaysOpened)."
                days_result = list(prolog.query(days_query))
                if days_result:
                    days_opened = days_result[0]['DaysOpened']
                    day_open_close[cafe] = days_opened
                else:
                    day_open_close[cafe] = []
            
            return day_open_close
        except Exception as e:
            print(f"Error in getOpenDays: {e}")
            return {}

    def re_add_constraint(self):
        selected = self.comboBox.currentText()

        if selected == "Travel Time":
            # Set specific transport constraints based on user input
            transport = self.transportType.currentText().lower().replace('/', '_')  # e.g., "walk", "public_transport", "taxi_moto"
            self.transportVar = transport
            try:
                max_time = int(self.travel_time.text())
                self.maxTimeVar = max_time
            except ValueError:
                self.transportVar = "any"
                self.maxTimeVar = "any"
                print("Invalid transport time input. Constraint not added.")
                return
            self.transportation.show()
            self.verticalLayout_2.addWidget(self.transportation)
            self.getCafes()

        elif selected == "Must have wifi":
            self.wifiVar = "yes"
            self.getCafes()
            self.wifi.show()
            self.verticalLayout_2.addWidget(self.wifi)

        elif selected == "Must have power sockets":
            self.socketsVar = "yes"
            self.getCafes()
            self.power_sockets.show()
            self.verticalLayout_2.addWidget(self.power_sockets)

        elif selected == "Dietary Preference":
            preference = self.dietaryPreference.currentText().lower()
            if preference in ["vegan", "vegetarian", "none"]:
                self.veganPreferenceVar = preference
            else:
                self.veganPreferenceVar = "any"
            needs_meals = "yes"  # Assuming user selects to have meals; modify as needed
            self.needsMealsVar = needs_meals
            self.dietary_pref.show()
            self.verticalLayout_2.addWidget(self.dietary_pref)
            self.getCafes()

        elif selected == "Meals":
            needs_meals = "yes"  # Or "no" based on user input
            self.needsMealsVar = needs_meals
            self.getCafes()

        elif selected == "Opening Time":
            days_options = self.getOpenDays()
            if days_options:
                self.dayOptions = days_options
            else:
                return
            self.setupDaySelect()
            self.opening_closing.show()
            self.verticalLayout_2.addWidget(self.opening_closing)
            self.getCafes()

    def clear_vertical_layout(self):
        widgets = [
            self.transportation,
            self.wifi,
            self.power_sockets,
            self.dietary_pref,
            self.opening_closing,
        ]

        for widget in widgets:
            self.verticalLayout_2.removeWidget(widget)
            widget.hide()

    def updateMaximumPrice(self, text):
        try:
            if text.strip().lower() == "any":
                self.priceVar = "any"
                self.label_6.setText("pesos")  # Reset the message
            else:
                price = float(text)
                if price < 2000:
                    self.label_6.setText("Min 2000 pesos")  # Show error in GUI
                    self.priceVar = 'any'
                else:
                    self.priceVar = int(price)
                    self.label_6.setText("pesos")  # Reset the message
            self.getCafes()
        except ValueError:
            self.priceVar = "any"
            self.getCafes()
        except ValueError:
            print("Invalid price input. Please enter a numerical value or 'any'.")
            self.priceVar = "any"
            self.getCafes()

    def getCafes(self):
        try:
            # Prepare constraint values for the Prolog query
            transport = f"'{self.transportVar}'" if self.transportVar != "any" else "'any'"
            max_time = self.maxTimeVar if self.transportVar != "any" and self.maxTimeVar != "any" else 'any'
            price = self.priceVar if self.priceVar != "any" else 'any'
            wifi = f"'{self.wifiVar}'" if self.wifiVar != "any" else "'any'"
            sockets = f"'{self.socketsVar}'" if self.socketsVar != "any" else "'any'"
            vegan_pref = f"'{self.veganPreferenceVar}'" if self.veganPreferenceVar != "any" else "'any'"
            needs_meals = f"'{self.needsMealsVar}'" if self.needsMealsVar != "any" else "'any'"
            visit_day = f"'{self.visitDayVar}'" if self.visitDayVar != "any" else "'any'"
            from_time = self.fromVar if self.fromVar != "any" else 'any'
            to_time = self.toVar if self.toVar != "any" else 'any'

            # Construct the Prolog query with active constraints or 'any'
            query = f"""findall(
                Cafe,
                suitable_cafe(
                    Cafe, 
                    {transport}, 
                    {max_time}, 
                    {price}, 
                    {wifi}, 
                    {sockets}, 
                    {vegan_pref}, 
                    {needs_meals}, 
                    {visit_day}, 
                    {from_time}, 
                    {to_time}
                ),
                Cafes
            )."""
            
            print("Prolog Query for Suitable Cafes:", query)  # Debug statement
            result = list(prolog.query(query))
            
            # Extract the list of Cafes
            cafes = []
            if result and 'Cafes' in result[0]:
                cafes = result[0]['Cafes']  # Retrieve the Cafes list from the result
            
            # Handle case when no cafes are found
            if not cafes:
                self.cafe_results = []
                self.current_index = 0
                self.update_cafe_info(nodata=True)
                self.update_button_visibility()
                self.update_result_info("Found no cafes matching your criteria.")
                return
            
            # Retrieve addresses for each Cafe
            cafe_results = []
            for cafe in cafes:
                if isinstance(cafe, str):  # Ensure cafe is a string
                    address_query = f"address('{cafe}', Address)."
                    address_result = list(prolog.query(address_query))
                    if address_result:
                        address = address_result[0]['Address']
                        cafe_results.append((cafe, address))
                    else:
                        cafe_results.append((cafe, "Address not found"))
            
            # Remove duplicates and prepare final results
            set_results = set(cafe_results)
            print("Suitable Cafes Found:", set_results)  # Debug statement
            
            if set_results:
                self.cafe_results = list(set_results)
                self.current_index = 0
                self.update_cafe_info()
                self.update_button_visibility()
                self.update_result_info(f"Found {len(self.cafe_results)} cafes matching your criteria.")
            else:
                self.cafe_results = []
                self.current_index = 0
                self.update_cafe_info(nodata=True)
                self.update_button_visibility()
                self.update_result_info("Found no cafes matching your criteria.")
                
        except Exception as e:
            print(f"Error querying Prolog: {e}")
            self.cafe_results = []
            self.current_index = 0
            self.update_cafe_info(nodata=True)
            self.update_button_visibility()
            self.update_result_info("Found no cafes matching your criteria.")

    def update_cafe_info(self, nodata=False):
        if nodata:
            self.cafe_name.setText("None Found")
            self.cafe_address_label.setText("Sorry, we could not find any cafes matching that description.")
            return

        if not self.cafe_results:
            self.cafe_name.setText("None Found")
            self.cafe_address_label.setText("Sorry, we could not find any cafes matching that description.")
            return

        cafe, address = self.cafe_results[self.current_index]
        self.cafe_name.setText(cafe.replace('_', ' '))
        self.cafe_address_label.setText(address.replace('_', ' '))


    def update_result_info(self, message):
        """Update the results information label."""
        self.result_info.setText(message)

    def show_previous_cafe(self):
        """Show the previous cafe in the list."""
        if self.cafe_results and self.current_index > 0:
            self.current_index -= 1
            self.update_cafe_info()
            self.update_button_visibility()

    def show_next_cafe(self):
        """Show the next cafe in the list."""
        if self.cafe_results and self.current_index < len(self.cafe_results) - 1:
            self.current_index += 1
            self.update_cafe_info()
            self.update_button_visibility()

    def update_button_visibility(self):
        """Update the visibility of the Previous and Next buttons."""
        self.previous_button.setVisible(self.current_index > 0)
        self.next_button.setVisible(self.current_index < len(self.cafe_results) - 1)

    def setupDaySelect(self):
        """Set up the day selection combo box with available days."""
        # Clear existing items
        self.daySelect.clear()

        # Add only the days that are in day_options
        for day in self.dayOptions.keys():
            self.daySelect.addItem(day)

    def check_correct_from_to_time(self):
        if self.visitDayVar == "any":
            # If VisitDay is 'any', ignore time constraints
            self.fromVar = "any"
            self.toVar = "any"
            self.getCafes()
            self.label_12.setText("")
            return

        from_timeSelected = (
            self.from_time.time().hour() + self.from_time.time().minute() / 60
        )
        to_timeSelected = self.to_time.time().hour() + self.to_time.time().minute() / 60
        opening_time = self.dayOptions[self.daySelect.currentText()][0]
        closing_time = self.dayOptions[self.daySelect.currentText()][1]

        print(opening_time, from_timeSelected, to_timeSelected, closing_time)

        if opening_time <= from_timeSelected < to_timeSelected <= closing_time:
            self.fromVar = from_timeSelected
            self.toVar = to_timeSelected
            self.getCafes()
            self.label_12.setText("")
        else:
            self.label_12.setText("No cafe's will be open at this time")

    # add methods for get options


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
