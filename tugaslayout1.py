from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QLabel, QLineEdit, QRadioButton, QComboBox, QPushButton, QGroupBox


class TugasLayout1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        self.setFixedSize(500, 500)
        layout = QVBoxLayout()

        iden_group = QGroupBox("Identitas")
        iden_layout = QVBoxLayout()
        iden_layout.addWidget(QLabel("Nama  : Apta Mahogra Bhamakerti"))
        iden_layout.addWidget(QLabel("NIM   : F1D022035"))
        iden_layout.addWidget(QLabel("Kelas : C"))
        iden_group.setLayout(iden_layout)
        

        nav_group = QGroupBox("Navigation")
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QPushButton("Home"))
        nav_layout.addWidget(QPushButton("About"))
        nav_layout.addWidget(QPushButton("Contact"))
        nav_group.setLayout(nav_layout)
        

        form_group = QGroupBox("User Registration")
        form_layout = QFormLayout()

        self.full_name = QLineEdit()
        self.email = QLineEdit()
        self.phone = QLineEdit()
        self.gender_male = QRadioButton("Male")
        self.gender_female = QRadioButton("Female")
        self.country = QComboBox()
        self.country.addItems(["", "Indonesia", "Jepang", "China", "Australia"])

        gender_layout = QHBoxLayout()
        gender_layout.addWidget(self.gender_male)
        gender_layout.addWidget(self.gender_female)

        form_layout.addRow("Full Name:", self.full_name)
        form_layout.addRow("Email:", self.email)
        form_layout.addRow("Phone:", self.phone)
        form_layout.addRow("Gender:", gender_layout)
        form_layout.addRow("Country:", self.country)
        form_group.setLayout(form_layout)
        

        actions_group = QGroupBox("Actions")
        actions_layout = QHBoxLayout()
        actions_layout.addWidget(QPushButton("Submit"))
        actions_layout.addWidget(QPushButton("Cancel"))
        actions_group.setLayout(actions_layout)
        

        layout.addWidget(iden_group)
        layout.addWidget(nav_group)
        layout.addWidget(form_group)
        layout.addWidget(actions_group)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    window = TugasLayout1()
    window.show()
    app.exec()