import QtQuick 1.1

Rectangle {
  id: root
  width: 100; height: 60
  Column {
    Rectangle {
      width: 100; height: 20
      color: "grey"
      Text {
        anchors.horizontalCenter: parent.horizontalCenter
        text: "<공지사항>"
      }
    }
    Rectangle {
      width: 100; height: 20
      color: "darkgrey"
      Text {
        anchors.horizontalCenter: parent.horizontalCenter
        text: "월요일 10시는"
      }
    }
    Rectangle {
      width: 100; height: 20
      color: "lightgrey"
      Text {
        anchors.horizontalCenter: parent.horizontalCenter
        text: "커피타임!"
      }
    }
  }
}
