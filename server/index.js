const WebSocket = require('ws');

const wss = new WebSocket.Server({port: 8082});

wss.on("connection", ws => {
    console.log("New client connected");

    ws.on("message", (data) => {
        console.log("Clinet has sent us : ${data}"); // 정상 프린트 안됨. -> Clinet has sent us : ${data}
    });
    ws.on("message", data => {
        console.log("Clinet has sent us : " + data);

        ws.send(data.toUpperCase() );
    });

    ws.on("close", () => {
        console.log("Clinet has disconnected");
    });

   


});

// node index.js