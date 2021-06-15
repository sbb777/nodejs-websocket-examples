const WebSocket = require('ws');

const wss = new WebSocket.Server({port: 9000});

wss.on("connection", ws => {
    console.log("New client connected");

let value1 =0;
    ws.on("message", data => {
        console.log("Clinet has sent us : " + data);
        

        const data1 =JSON.parse(data);
        console.log("Client sent command : " + data1.command);

        ws.send(data.toUpperCase() );

        value1 += 200;
        console.log("value1 : " + value1);

       const mssg = JSON.stringify( {'report': 'analog_input', 'pin': 0, 'value': value1, 'timestamp': 1623650704.2288637});
       ws.send(mssg);

    });

    ws.on("close", () => {
        console.log("Clinet has disconnected");
    });

   


});

// node index.js

//window.socket.send("Hello1111");