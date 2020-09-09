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
  color: black;
  border: 2px solid #4CAF50;
}

.green:hover {
  background-color: #4CAF50;
  color: white;
}

.blue {
  background-color: white;
  color: black;
  border: 2px solid #008CBA;
}

.blue:hover {
  background-color: #008CBA;
  color: white;
}

.red {
  background-color: white;
  color: black;
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

<script>
function setStatus(data, key){
    console.log(key)
    console.log(data)
    label = document.getElementById(key + '-status')
    label.innerText = data.status
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
