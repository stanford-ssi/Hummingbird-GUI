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
        arduino->open(QSerialPort::WriteOnly);
        arduino->setBaudRate(QSerialPort::Baud9600);
        arduino->setDataBits(QSerialPort::Data8);
        arduino->setParity(QSerialPort::NoParity);
        arduino->setStopBits(QSerialPort::OneStop);
        arduino->setFlowControl(QSerialPort::NoFlowControl);
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
}


void MainWindow::on_offBtn_clicked()
{
    QString command = "0";
    arduino->write(command.toStdString().c_str());
}

