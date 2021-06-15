// Import dependencies
const SerialPort = require("serialport");
const Readline = require("@serialport/parser-readline");

// Defining the serial port
const port = new SerialPort("COM18", {
    baudRate: 115200,
});

// The Serial port parser
const parser = new Readline();
port.pipe(parser);

port.write("ROBOT POWER ON \n");
// Read the data from the serial port
parser.on("data", (line) => console.log(line));

// Write the data to the serial port
port.write("ROBOT POWER ON");
port.write("ROBOT POWER ON");