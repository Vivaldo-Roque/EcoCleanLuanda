function connect() {

  const socket = new WebSocket(`wss://${window.location.host}/ws/contentor/f2ab21cb-fb3b-4ec4-8b0f-1910fb50847d/`)

  socket.onmessage = function (e) {
    console.log('Server: ' + e.data);
    updateChart();
  };

  socket.onclose = function (e) {
    console.log('Socket is closed. Reconnect will be attempted in 1 second.', e.reason);
    setTimeout(connect, 1000);
  };

  socket.onerror = function (err) {
    console.error('Socket encountered error: ', err.message, 'Closing socket');
    socket.close();
  };

}

let temperatureLevelChart
let humidityLevelChart
let trashLevelChart

const ctx1 = document.getElementById('tempChart')
const ctx2 = document.getElementById('humiChart')
const ctx3 = document.getElementById('distChart')

const fetchChartData = async () => {
  const response = await fetch(`https://${window.location.host}/chartdata/f2ab21cb-fb3b-4ec4-8b0f-1910fb50847d`)
  const data = await response.json()
  return data
}

const drawChart = async () => {

  const data = await fetchChartData()

  temperatureLevelChart = new Chart(ctx1, {
    type: 'bar',
    data: {
      labels: ['Temperatura'],
      datasets: [
        {
          label: 'Temperatura atual em ºC',
          data: [data['sensor_temperatura']],
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          max: 100,
          min: 0
        }
      }
    }
  })

  humidityLevelChart = new Chart(ctx2, {
    type: 'bar',
    data: {
      labels: ['Humidade'],
      datasets: [
        {
          label: 'Humidade atual em %',
          data: [data['sensor_umidade']],
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          max: 100,
          min: 0
        }
      }
    }
  })

  trashLevelChart = new Chart(ctx3, {
    type: 'bar',
    data: {
      labels: ['Lixo'],
      datasets: [
        {
          label: 'Nível de lixo atual',
          data: [data['sensor_distancia']],
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          max: 100,
          min: 0
        }
      }
    }
  })

}

const updateChart = async () => {

  const data = await fetchChartData()

  temperatureLevelChart.data.datasets[0].data[0] = data['sensor_temperatura']
  temperatureLevelChart.update('none')

  humidityLevelChart.data.datasets[0].data[0] = data['sensor_umidade']
  humidityLevelChart.update('none')

  trashLevelChart.data.datasets[0].data[0] = data['sensor_distancia']
  trashLevelChart.update('none')
}

connect()

drawChart()