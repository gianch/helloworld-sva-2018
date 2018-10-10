var serial; // variable to hold an instance of the serialport library
var portName = '/dev/cu.usbserial-DN050GXX';  // fill in your serial port name here
var inData;
var xPos = 0;

function setup() {
 createCanvas(1440, 700);
 background('#0D0D0D');
 
 serial = new p5.SerialPort();    // make a new instance of the serialport library
 serial.on('list', printList);    // set a callback function for the serialport list event
 serial.on('data', serialEvent);    // callback for when new data arrives
 
 // change the data rate to whatever you wish
 var options = { baudrate: 9600};
 serial.open(portName, options);


}

function draw() {
  // printValue();
  graphData(inData);
}


function graphData(newData) {

  background('#0D0D0D');
  fill(255);
  noStroke();
  // print out the sensor value
  textSize(32);
  text("Stress level: " + inData, xPos, 80);
  // map the range of the input to the window height:
  var yPos = map(newData, 0, 255, 0, height);
  // draw the line in a pretty color:
  stroke('#07F8B6');
  strokeWeight(140);
  line(xPos, height, xPos, height - yPos);
  // at the edge of the screen, go back to the beginning:
  if (xPos >= width) {
    xPos = 0;
    // clear the screen by resetting the background:
    background('#0D0D0D');
  } else {
    // increment the horizontal position for the next reading:
    xPos++;
  }
}


function serialEvent() {
  // retreive value from serial port
  inData = Number(serial.read());
}


// function printValue(){
//   background('#0D0D0D');
//   fill(255);
//   noStroke();
//   // print out the sensor value
//   text("sensor value: " + inData, 30, 30);
// }

// print list of ports for debugging
function printList(portList) {
  // portList is an array of serial port names
  for (var i = 0; i < portList.length; i++) {
    // Display the list the console:
  print(i + " " + portList[i]);
   }
}

