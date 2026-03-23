const dgram = require('dgram');
const http = require('http');
const udp = dgram.createSocket('udp4');
let messages = [];
let id = 0;

udp.on('message', (msg) => {
    let data;
    try { data = JSON.parse(msg); } catch(e) { data = {raw: msg.toString()}; }
    messages.push({id: id++, data: data});
    console.log("UDP:", data);
});

udp.bind(8080);

http.createServer((req, res) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    if(req.url === '/poll') {
        const lastId = parseInt(new URL(req.url, 'http://l').searchParams.get('lastId') || '-1');
        res.end(JSON.stringify({messages: messages.filter(m => m.id > lastId)}));
    } else {
        res.end('ok');
    }
}).listen(8081);

console.log("Bridge: UDP 8080, HTTP 8081");