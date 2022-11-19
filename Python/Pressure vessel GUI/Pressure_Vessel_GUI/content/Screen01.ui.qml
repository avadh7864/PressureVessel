

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.2
import QtQuick.Controls 6.2
import Pressure_Vessel_GUI

Rectangle {
    id: rectangle
    width: Constants.width
    height: Constants.height

    color: Constants.backgroundColor

    Button {
        id: button
        text: qsTr("Press me")
        anchors.verticalCenter: parent.verticalCenter
        checkable: true
        anchors.horizontalCenter: parent.horizontalCenter

        Connections {
            target: button
            onClicked: animation.start()
        }
    }

    Text {
        id: label
        text: qsTr("Hello Pressure_Vessel_GUI")
        anchors.top: button.bottom
        font.family: Constants.font.family
        anchors.topMargin: 45
        anchors.horizontalCenter: parent.horizontalCenter

        SequentialAnimation {
            id: animation

            ColorAnimation {
                id: colorAnimation1
                target: rectangle
                property: "color"
                to: "#2294c6"
                from: Constants.backgroundColor
            }

            ColorAnimation {
                id: colorAnimation2
                target: rectangle
                property: "color"
                to: Constants.backgroundColor
                from: "#2294c6"
            }
        }
    }

    TabButton {
        id: tabButton
        x: 0
        y: -31
        width: 103
        height: 30
        text: qsTr("Internal Pressure")
    }
    states: [
        State {
            name: "clicked"
            when: button.checked

            PropertyChanges {
                target: label
                text: qsTr("Button Checked")
            }
        }
    ]
}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
