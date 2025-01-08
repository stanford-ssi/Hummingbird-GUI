#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    // setup QSerialPort
    arduino = new QSerialPort;
    arduino_is_available = false;
    arduino_port_name = "";     // to be populated later

    // check product and vendor ID and ports
    qDebug() << "Number of Ports: " << QSerialPortInfo::availablePorts().length();
    foreach (const QSerialPortInfo &serialPortInfo, QSerialPortInfo::availablePorts()){
        if (serialPortInfo.hasVendorIdentifier() && serialPortInfo.hasProductIdentifier()) {
            qDebug() << "Vendor ID: " << serialPortInfo.vendorIdentifier();
            qDebug() << "Product ID: " << serialPortInfo.productIdentifier();
        }
    }

    // check which port connection is on
    foreach (const QSerialPortInfo &serialPortInfo, QSerialPortInfo::availablePorts()){
        if (serialPortInfo.hasVendorIdentifier() && serialPortInfo.hasProductIdentifier()) {
            if (serialPortInfo.vendorIdentifier() == arduino_uno_vendorID && serialPortInfo.productIdentifier() == arduino_uno_productID) {
                arduino_port_name = serialPortInfo.portName();
                arduino_is_available = true;
                qDebug() << "Port available!";
            }
        }
    }

    // setup port
    if (arduino_is_available) {
        arduino->setPortName(arduino_port_name);
        arduino->open(QIODevice::ReadWrite);
        arduino->setBaudRate(QSerialPort::Baud9600);
        arduino->setDataBits(QSerialPort::Data8);
        arduino->setParity(QSerialPort::NoParity);
        arduino->setStopBits(QSerialPort::OneStop);
        arduino->setFlowControl(QSerialPort::NoFlowControl);

        // following line taken from https://forum.qt.io/topic/132487/sending-and-receiving-data-from-to-pc-arduino-through-serial-port-using-qt
        QObject::connect(arduino, SIGNAL(readyRead()), this, SLOT(readSerial()));

    } else {
        QMessageBox::warning(this, "Port error", "Couldn't find arduino");
    }
}

MainWindow::~MainWindow()
{
    // close port with destructor
    if (arduino->isOpen()) {
        qDebug() << "closing port";
        arduino->close();
    }

    delete ui;
}

void MainWindow::on_onBtn_clicked()
{
    QString command = "1";
    arduino->write(command.toStdString().c_str());
    readSerial();
}


void MainWindow::on_offBtn_clicked()
{
    QString command = "0";
    arduino->write(command.toStdString().c_str());
    readSerial();
}

// following function taken from https://stackoverflow.com/questions/59862831/qt-and-arduino-serial-communication-read-and-write
void MainWindow::readSerial() {
    // qDebug() << "Serial Port Works!!\n";
    // QMessageBox::information(this, "Serial Port Works", "Opened serial port to arduino.");
    QByteArray serialData = arduino->readAll();
    QString temp = QString::fromStdString(serialData.toStdString());
    qDebug() << "MSG:" << temp;
    /*
     * There seems to be some issues with passing the temp QString to the other GUI functions.
     * Could be a timing issue. Sometimes message will also be split into two, most likely because of
     * bit width limit of 8 bits.
     * This is a temporary solution that keeps temp to readSerial instead of passing it out.
     */
    ui->msgBox->setText(temp);
}

