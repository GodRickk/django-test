
console.log("Hello world");


var socket = new WebSocket('ws://' + window.location.host + '/ws/random_number/');

socket.onmessage = function(event) {
    var data = JSON.parse(event.data);
    document.getElementById('random-number').textContent = data.number;
};

/* function logout() {
    window.location.href = '/logout/';
} */