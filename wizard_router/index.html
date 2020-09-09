<!DOCTYPE html>
<html>
<head>
    <style>
.button {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 8px 16px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
}

.green {
  background-color: white;
  color: green;
  border: 2px solid #4CAF50;
}

.green:hover {
  background-color: #4CAF50;
  color: white;
}

.blue {
  background-color: white;
  color: #008CBA;
  border: 2px solid #008CBA;
}

.blue:hover {
  background-color: #008CBA;
  color: white;
}

.red {
  background-color: white;
  color: red;
  border: 2px solid #f44336;
}

.red:hover {
  background-color: #f44336;
  color: white;
}

table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}

    </style>
</head>
<body>
<table style="margin-left: auto; margin-right: auto;">
    <caption>
        <h1 style="text-align: center;">
            <span style="color: #000080;">
                <strong>VPN Getaway</strong>
            </span>
        </h1>
    </caption>
    <tbody>
    <tr border-collapse="collapse">
        <td style="text-align: center;"><strong>Open VPN</strong></td>
        <td style="text-align: center;"><strong>Open Connect</strong></td>
    </tr>
    <tr>
        <td>
            <button class="button green" onclick="getStatus('openvpns')">Status</button>
            <button class="button red" onclick="stopVPN('openvpns')">Stop</button>
            <button class="button blue" onclick="restartVPN('openvpns')">Restart</button>
        </td>
        <td>
            <button class="button green" onclick="getStatus('openconnects')">Status</button>
            <button class="button red" onclick="stopVPN('openconnects')">Stop</button>
            <button class="button blue" onclick="restartVPN('openconnects')">Restart</button>
        </td>
    </tr>
    <tr>
        <td><label for="name">Status: </label><label id="openvpns-status" for="name">unknown</label></td>
        <td><label for="name">Status: </label><label id="openconnects-status" for="name">unknown</label></td>
    </tr>
    </tbody>
</table>

</br>

<table style="margin-left: auto; margin-right: auto;">
    <caption>
        <h1 style="text-align: center;">
            <span style="color: #000080;">
                <strong>Device Info</strong>
            </span>
        </h1>
    </caption>
    <tbody>
    <tr border-collapse="collapse">
        <td>
            <strong>IP address: ${ip}</strong>
        </td>
    </tr>
    <tr>
        <td style="text-align: center;">
            <strong >CPU temperature: </strong>
            <strong id="cpu-temperature">0</strong>
            <strong>C</strong>
            <button class="button green" onclick="getTemperature()">Refresh</button>
        </td>
    </tr>
    <tr>
        <td>
            <button class="button green" onclick="getPing()">Ping</button>
            <button class="button red" onclick="reboot()">Reboot</button>
            <p id="ping" style="text-align: center;font-size:7px;"></p>
        </td>
    </tr>
    </tbody>
</table>

<script>
function setStatus(data, key){
    console.log(key)
    console.log(data)
    label = document.getElementById(key + '-status')
    label.innerText = data.status
}

function getPing() {
  fetch('http://${ip}/apiv1/pings')
  .then(response => response.json())
  .then(function(json) {
    label = document.getElementById('ping')
    label.innerText = json.ping
  });
}

function reboot() {
  fetch('http://${ip}/apiv1/reboots')
  .then(response => response.json())
  .then(function(json) {
  });
}

function getTemperature() {
  fetch('http://${ip}/apiv1/temperatures')
  .then(response => response.json())
  .then(function(json) {
    label = document.getElementById('cpu-temperature')
    label.innerText = json.cpu
  });
}

function getStatus(key) {
console.log(key)
  fetch('http://${ip}/apiv1/' + key, {method: 'STATUS',})
  .then(response => response.json())
  .then(function(json) {
    setStatus(json, key)
  });
}

function restartVPN(key) {
  fetch('http://${ip}/apiv1/' + key, {method: 'RESTART',})
  .then(response => response.json())
  .then(function(json) {
    setStatus(json, key)
  });}

function stopVPN(key) {
  fetch('http://${ip}/apiv1/' + key, {method: 'STOP',})
  .then(response => response.json())
  .then(function(json) {
    setStatus(json, key)
  });
}
</script>
</body>
</html>
